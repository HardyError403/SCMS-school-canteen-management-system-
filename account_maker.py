import re
import csv
import hashlib
import logging
from pathlib import Path
from tkinter import messagebox
import customtkinter as ctk

# --- Logging Configuration ---
LOG_FILE = Path(__file__).parent / "account_maker.log"
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# --- Constants ---
DATA_FILE = Path(__file__).parent / "students.csv"
SALT = b"some_static_salt"

def hash_password(password: str) -> str:
    hasher = hashlib.sha256()
    hasher.update(SALT + password.encode("utf-8"))
    digest = hasher.hexdigest()
    logger.debug("Hashed password: %s…", digest[:8])
    return digest

def ensure_data_file():
    if not DATA_FILE.exists():
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["student_number", "password_hash"])
        logger.info("Created data file: %s", DATA_FILE)
    else:
        logger.debug("Data file exists: %s", DATA_FILE)

class StudentRegisterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        logger.info("Launching StudentRegisterApp")
        ensure_data_file()

        # Window setup
        self.title("Student Register")
        self.geometry("800x480")
        self.configure(bg_color="white")

        ctk.set_appearance_mode("light")
        # keep default accent, but window is white

        # State variables
        self.student_number   = ctk.StringVar()
        self.old_password     = ctk.StringVar()
        self.new_password     = ctk.StringVar()
        self.confirm_password = ctk.StringVar()
        self.show_password    = ctk.BooleanVar(value=False)

        # Build + place
        self._build_widgets()
        self._place_widgets()

    def _build_widgets(self):
        # Title
        self.lbl_title = ctk.CTkLabel(
            master=self,
            text="Student Register",
            font=("Arial", 18, "bold"),
            text_color="#333",
            bg_color="white"
        )

        # Input fields
        self._add_field("Student Number:",  self.student_number,   row=0,
                        placeholder="8 digits (e.g. 20001234)")
        self._add_field("Old Password:",     self.old_password,     row=1, show="*")
        self._add_field("New Password:",     self.new_password,     row=2, show="*")
        self._add_field("Confirm Password:", self.confirm_password, row=3, show="*")

        # Password strength meter
        self.strength_label = ctk.CTkLabel(
            master=self,
            text="Strength: Empty",
            anchor="w",
            text_color="#333",
            bg_color="white"
        )
        self.strength_bar = ctk.CTkProgressBar(
            master=self,
            width=200
        )
        self.new_password.trace_add("write", self._update_strength_widgets)

        # Show/hide passwords
        self.chk_show = ctk.CTkCheckBox(
            master=self,
            text="Show Passwords",
            variable=self.show_password,
            text_color="#333",
            bg_color="white",
            command=self._toggle_password_visibility
        )

        # Action buttons
        self.btn_save = ctk.CTkButton(
            master=self,
            text="Save",
            width=100,
            font=("Arial", 12),
            command=self._on_save
        )
        self.btn_quit = ctk.CTkButton(
            master=self,
            text="Quit",
            fg_color="#e74c3c",
            hover_color="#ff4d4d",
            width=100,
            font=("Arial", 12),
            command=self.destroy
        )

    def _add_field(self, label_text, var, row, show=None, placeholder=None):
        lbl = ctk.CTkLabel(
            master=self,
            text=label_text,
            anchor="w",
            text_color="#333",
            bg_color="white",
            font=("Arial", 12)
        )
        entry = ctk.CTkEntry(
            master=self,
            textvariable=var,
            show=show or "",
            placeholder_text=placeholder or "",
            width=250,
            font=("Arial", 12)
        )
        setattr(self, f"lbl_{row}", lbl)
        setattr(self, f"entry_{row}", entry)

    def _place_widgets(self):
        pad = {"padx": 20, "pady": 10}

        self.lbl_title.grid(row=0, column=0, columnspan=3, pady=(20, 5))

        for row in range(4):
            getattr(self, f"lbl_{row}").grid(
                row=row+1, column=0, sticky="w", **pad
            )
            getattr(self, f"entry_{row}").grid(
                row=row+1, column=1, columnspan=2, **pad
            )

        self.strength_label.grid(row=3, column=3, sticky="w", padx=(10, 0))
        self.strength_bar.grid(row=3, column=4, sticky="w", padx=10)

        self.chk_show.grid(row=5, column=1, sticky="w", **pad)

        self.btn_save.grid(row=6, column=1, **pad)
        self.btn_quit.grid(row=6, column=2, **pad)

    def _update_strength_widgets(self, *_):
        pwd = self.new_password.get()
        score = sum([
            len(pwd) >= 8,
            bool(re.search(r"[A-Z]", pwd)),
            bool(re.search(r"[a-z]", pwd)),
            bool(re.search(r"\d", pwd)),
            bool(re.search(r"\W", pwd)),
        ])
        texts  = {0:"Empty",1:"Very Weak",2:"Weak",3:"Fair",4:"Good",5:"Excellent"}
        colors = {0:"gray",1:"red",2:"red",3:"orange",4:"green",5:"green"}
        frac   = score / 5.0

        self.strength_label.configure(
            text=f"Strength: {texts[score]}",
            text_color=colors[score]
        )
        self.strength_bar.set(frac)
        self.strength_bar.configure(progress_color=colors[score])

        logger.debug("Password strength %d/5 → %s", score, texts[score])

    def _toggle_password_visibility(self):
        show_char = "" if self.show_password.get() else "*"
        for r in (1, 2, 3):
            getattr(self, f"entry_{r}").configure(show=show_char)
        state = "visible" if show_char == "" else "hidden"
        logger.info("Passwords are now %s", state)

    def _validate_inputs(self):
        sn = self.student_number.get()
        if not re.fullmatch(r"\d{8}", sn):
            messagebox.showwarning("Invalid", "Enter exactly 8 digits.")
            return False
        if self.new_password.get() != self.confirm_password.get():
            messagebox.showwarning("Mismatch", "Passwords must match.")
            return False
        if sn == self.new_password.get():
            messagebox.showwarning("Weak Password", "Password should not match student number.")
            return False
        return True

    def _read_students(self):
        with open(DATA_FILE, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        logger.info("Loaded %d records", len(rows))
        return rows

    def _write_students(self, rows):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["student_number","password_hash"])
            writer.writeheader()
            writer.writerows(rows)
        logger.info("Save complete")

    def _on_save(self):
        if not self._validate_inputs():
            return

        sn, old_pwd, new_pwd = (
            self.student_number.get(),
            self.old_password.get(),
            self.new_password.get()
        )
        new_hash = hash_password(new_pwd)
        rows     = self._read_students()

        for row in rows:
            if row["student_number"] == sn:
                if row["password_hash"] != hash_password(old_pwd):
                    messagebox.showerror("Auth Failed", "Old password is incorrect.")
                    logger.error("Auth fail for %s", sn)
                    return
                row["password_hash"] = new_hash
                self._write_students(rows)
                messagebox.showinfo("Updated", "Password updated.")
                logger.info("Password updated for %s", sn)
                return

        rows.append({"student_number": sn, "password_hash": new_hash})
        self._write_students(rows)
        messagebox.showinfo("Registered", "Student registered.")
        logger.info("New registration: %s", sn)

if __name__ == "__main__":
    app = StudentRegisterApp()
    app.mainloop()
