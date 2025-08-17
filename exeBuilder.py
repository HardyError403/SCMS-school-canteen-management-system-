import os
import shutil
import subprocess
import threading
import time
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

FINISHED_DIR = "converted"

class PyToExeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Py → EXE Converter")
        self.geometry("600x480")
        self.resizable(False, False)

        # Top label
        self.label = ctk.CTkLabel(self, text="Select Python files to convert:")
        self.label.pack(pady=(20, 5))

        # Scrollable list container
        self.file_frame = ctk.CTkScrollableFrame(self, width=560, height=300)
        self.file_frame.pack(pady=(0, 10))

        # Convert button
        self.convert_btn = ctk.CTkButton(
            self,
            text="Convert Selected",
            command=self.start_conversion
        )
        self.convert_btn.pack(pady=(0, 10))

        # Status bar
        self.status = ctk.CTkLabel(self, text="")
        self.status.pack(pady=(5, 20))

        os.makedirs(FINISHED_DIR, exist_ok=True)
        self.populate_file_list()

    def populate_file_list(self):
        """Scan for .py files and create a row with checkbox + hidden progress bar."""
        self.file_widgets = []
        this_script = os.path.basename(__file__)
        py_files = [
            f for f in os.listdir('.') 
            if f.endswith('.py') and f != this_script
        ]

        for fname in py_files:
            row = ctk.CTkFrame(self.file_frame)
            row.pack(fill="x", padx=10, pady=5)

            var = ctk.BooleanVar(value=False)
            cb = ctk.CTkCheckBox(row, text=fname, variable=var)
            cb.pack(side="left", padx=(0, 10))

            prog = ctk.CTkProgressBar(row, width=350, mode="determinate")
            prog.set(0)
            prog.pack(side="left", padx=(0, 10))
            prog.pack_forget()  # hidden until needed

            self.file_widgets.append({
                "name": fname,
                "var": var,
                "frame": row,
                "prog": prog
            })

    def start_conversion(self):
        """Disable UI, show bars for selected files, and kick off conversion thread."""
        self.convert_btn.configure(state="disabled")
        selected = [fw for fw in self.file_widgets if fw["var"].get()]

        if not selected:
            self.status.configure(text="⚠️ No files selected.")
            self.convert_btn.configure(state="normal")
            return

        # Show progress bars only for selected files
        for fw in self.file_widgets:
            if fw["var"].get():
                fw["prog"].pack(side="left", padx=(0, 10))
            else:
                fw["prog"].pack_forget()

        self.status.configure(text="Starting conversions…")
        threading.Thread(target=self.convert_all, daemon=True).start()

    def convert_all(self):
        """Convert each selected .py file, updating progress based on exe size."""
        for fw in self.file_widgets:
            if not fw["var"].get():
                continue

            fname = fw["name"]
            prog = fw["prog"]
            exe_name = os.path.splitext(fname)[0] + ".exe"
            exe_path = os.path.join("dist", exe_name)

            # Reset progress bar
            self.update_prog(prog, 0)

            # Ensure no old exe lingers
            if os.path.isfile(exe_path):
                os.remove(exe_path)

            # Launch PyInstaller
            proc = subprocess.Popen(
                ["pyinstaller", "--onefile", "--windowed", fname],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            final_size = 1
            max_seen = 0

            # Poll until process finishes
            while proc.poll() is None:
                if os.path.isfile(exe_path):
                    size = os.path.getsize(exe_path)
                    max_seen = max(max_seen, size)
                    # Estimate progress as size relative to the maximum seen so far
                    percent = min(99, int((size / max_seen) * 100)) if max_seen > 0 else 1
                    self.update_prog(prog, percent)
                time.sleep(0.3)

            # Final update to 100% if exe exists
            if proc.returncode == 0 and os.path.isfile(exe_path):
                self.update_prog(prog, 100)
                self.move_and_cleanup(fname, exe_name)
            else:
                self.status.configure(text=f"❌ Failed to convert {fname}")

        self.status.configure(text="✅ All done! Check the converted folder.")
        self.convert_btn.configure(state="normal")

    def update_prog(self, prog_widget, value):
        """Thread-safe progress bar update."""
        self.after(0, lambda: prog_widget.set(value))

    def move_and_cleanup(self, script_name, exe_name):
        """Move the .exe into finished/ and remove build artifacts."""
        src = os.path.join("dist", exe_name)
        dst = os.path.join(FINISHED_DIR, exe_name)
        shutil.move(src, dst)

        # Clean build/ and spec
        if os.path.isdir("build"):
            shutil.rmtree("build")
        spec_file = os.path.splitext(script_name)[0] + ".spec"
        if os.path.isfile(spec_file):
            os.remove(spec_file)

if __name__ == "__main__":
    app = PyToExeApp()
    app.mainloop()
