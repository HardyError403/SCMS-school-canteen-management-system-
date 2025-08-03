import logging
from pathlib import Path
from tkinter import messagebox
import customtkinter as ctk

from csv_rw import write_txt

# --- Logging Configuration ---
LOG_FILE = Path(__file__).parent / "password_enter.log"
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PasswordEntryApp(ctk.CTk):
    PWD_FILE = Path(__file__).parent / "password.txt"

    def __init__(self):
        super().__init__()
        logger.info("Launching PasswordEntryApp")

        # Window setup
        self.title("Enter Password")
        self.geometry("250x200")
        self.configure(bg_color="#D3D3D3")          # light grey background
        ctk.set_appearance_mode("light")           # ensure light theme

        # State variable
        self.password = ctk.StringVar()

        # Build + place widgets
        self._build_widgets()
        self._place_widgets()

    def _build_widgets(self):
        # Title label
        self.lbl_title = ctk.CTkLabel(
            master=self,
            text="Enter Password Here",
            font=("Arial", 14),
            text_color="#333333",                   # dark text
            bg_color="#D3D3D3"                      # match window bg
        )

        # Password entry
        self.entry_password = ctk.CTkEntry(
            master=self,
            textvariable=self.password,
            placeholder_text="Password",
            placeholder_text_color="#666666",
            font=("Arial", 14),
            text_color="#333333",
            show="•",
            width=195,
            border_width=2,
            corner_radius=6,
            border_color="#666666",
            fg_color="#FFFFFF",                     # white field
            bg_color="#D3D3D3"
        )

        # Done button
        self.btn_done = ctk.CTkButton(
            master=self,
            text="Done",
            font=("Arial", 14),
            text_color="#333333",
            width=95,
            height=30,
            border_width=2,
            corner_radius=6,
            border_color="#666666",
            fg_color="#EFEFEF",                     # very light grey
            hover_color="#CCCCCC",
            command=self._on_done
        )

    def _place_widgets(self):
        pad = {"padx": 20, "pady": 10}

        self.lbl_title.grid(row=0, column=0, columnspan=2, **pad)
        self.entry_password.grid(row=1, column=0, columnspan=2, **pad)
        self.btn_done.grid(row=2, column=0, columnspan=2, **pad)

        self.entry_password.focus_force()

    def _on_done(self):
        pw = self.password.get()
        write_txt(self.PWD_FILE, pw)
        messagebox.showinfo("Password entered", "You may close this window")
        logger.info("Password written to %s", self.PWD_FILE)

if __name__ == "__main__":
    app = PasswordEntryApp()
    app.mainloop()
