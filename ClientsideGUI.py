import re
import logging
from pathlib import Path
from tkinter import messagebox, Tk

import customtkinter as ctk

from csv_rw import read_csv, write_csv
import account_maker

# --- Logging Configuration ---
LOG_FILE = Path(__file__).parent / "scms_client.log"
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
MENU_CSV     = Path(__file__).parent / "today_menu.csv"
STUDENTS_CSV = Path(__file__).parent / "students.csv"
PWD_FILE     = Path(__file__).parent / "password.txt"
ADMIN_PWD    = "123456"
MAX_MEALS    = 10


class SCMSClient(ctk.CTk):
    def __init__(self):
        super().__init__()
        logger.info("Launching SCMSClient")

        # Window setup
        self.title("SCMS-Client")
        self.geometry("800x450")
        self.configure(bg_color="white")
        ctk.set_appearance_mode("light")

        # State variables
        self.single_or_combo = ctk.IntVar(value=0)
        self.meal_vars       = [ctk.IntVar(value=0) for _ in range(MAX_MEALS)]
        self.soup_var        = ctk.IntVar(value=0)
        self.price_var       = ctk.StringVar(value="$0.00")
        self.student_id_var  = ctk.StringVar()
        self.password_var    = ctk.StringVar()

        # Build + place
        self._build_title()
        self._build_login_section()
        self._build_order_section()
        self._toggle_order_widgets(enabled=False)

    def _build_title(self):
        self.lbl_title = ctk.CTkLabel(
            master=self,
            text="School Canteen Management System - Order",
            font=("Arial", 16, "bold"),
            text_color="#333",
            bg_color="white"
        )
        self.lbl_title.grid(row=0, column=0, columnspan=4, pady=(10, 20))

    def _build_login_section(self):
        # Student Number
        self.lbl_student = ctk.CTkLabel(
            master=self,
            text="Student Number",
            anchor="w",
            text_color="#333",
            bg_color="white",
            font=("Arial", 12)
        )
        self.entry_student = ctk.CTkEntry(
            master=self,
            textvariable=self.student_id_var,
            width=200,
            font=("Arial", 12)
        )

        # Password
        self.lbl_password = ctk.CTkLabel(
            master=self,
            text="Password",
            anchor="w",
            text_color="#333",
            bg_color="white",
            font=("Arial", 12)
        )
        self.entry_password = ctk.CTkEntry(
            master=self,
            textvariable=self.password_var,
            show="*",
            width=200,
            font=("Arial", 12)
        )

        # Login button
        self.btn_login = ctk.CTkButton(
            master=self,
            text="Login",
            command=self._handle_login
        )

        self.lbl_student.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_student.grid(row=1, column=1, padx=5, pady=5)
        self.lbl_password.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_password.grid(row=2, column=1, padx=5, pady=5)
        self.btn_login.grid(row=3, column=1, pady=(10, 15))

    def _build_order_section(self):
        # Single / Combo radio buttons
        self.rdo_single = ctk.CTkRadioButton(
            master=self,
            variable=self.single_or_combo,
            value=1,
            text="Single"
        )
        self.rdo_combo = ctk.CTkRadioButton(
            master=self,
            variable=self.single_or_combo,
            value=2,
            text="Combo"
        )
        self.rdo_single.grid(row=1, column=2, sticky="w")
        self.rdo_combo.grid(row=1, column=3, sticky="w")

        # Meal checkboxes
        self.chk_meals = []
        for idx in range(MAX_MEALS):
            chk = ctk.CTkCheckBox(
                master=self,
                text=f"Meal {idx+1}",
                variable=self.meal_vars[idx],
                command=self._update_price
            )
            row = 4 + idx // 2
            col = 2 + (idx % 2)
            chk.grid(row=row, column=col, sticky="w", padx=10, pady=2)
            self.chk_meals.append(chk)

        # Soup checkbox & price label
        self.chk_soup = ctk.CTkCheckBox(
            master=self,
            text="Soup",
            variable=self.soup_var,
            command=self._update_price
        )
        self.lbl_price = ctk.CTkLabel(
            master=self,
            textvariable=self.price_var,
            font=("Arial", 12),
            text_color="#333",
            bg_color="white"
        )
        self.chk_soup.grid(row=10, column=2, sticky="w", padx=10, pady=5)
        self.lbl_price.grid(row=10, column=3, sticky="e", padx=10, pady=5)

        # Action buttons
        self.btn_done   = ctk.CTkButton(master=self, text="Done",   command=self._save_order)
        self.btn_cancel = ctk.CTkButton(master=self, text="Cancel", command=self._reset_ui)
        self.btn_done.grid(row=11, column=2, pady=(15, 10))
        self.btn_cancel.grid(row=11, column=3, pady=(15, 10))

    def _toggle_order_widgets(self, enabled: bool):
        state = "normal" if enabled else "disabled"
        for widget in self.grid_slaves():
            info = widget.grid_info()
            if int(info["row"]) >= 1 and int(info["column"]) >= 2:
                widget.configure(state=state)

    def _handle_login(self):
        sid = self.student_id_var.get().strip()
        pwd = self.password_var.get().strip()

        # Admin shortcut
        if sid == "admin" and pwd == ADMIN_PWD:
            account_maker.am()
            return

        if not re.fullmatch(r"\d{8}", sid):
            messagebox.showerror("Error", "Student number must be exactly 8 digits.")
            return

        rows = read_csv(STUDENTS_CSV)[0]
        for num, pw in ((r[0], r[1]) for r in rows):
            if sid == num:
                if pwd == pw:
                    self._load_menu()
                    self._toggle_order_widgets(enabled=True)
                    return
                messagebox.showerror("Error", "Wrong password.")
                return

        messagebox.showerror("Error", "Student not found.")

    def _load_menu(self):
        menu = read_csv(MENU_CSV)[0]
        for chk in self.chk_meals:
            idx = int(chk.cget("text").split()[1])
            chk.configure(text=menu[idx][1])

        self.chk_soup.configure(text=f"Soup: {menu[11][1]}")
        logger.info("Menu loaded and UI updated")

    def _update_price(self):
        menu     = read_csv(MENU_CSV)[0]
        selected = [i for i, var in enumerate(self.meal_vars, 1) if var.get()]
        price    = 0

        for idx in selected:
            col = 3 if len(selected) == 1 else 4
            price += int(menu[idx][col])

        if self.soup_var.get():
            price += int(menu[11][3])

        self.price_var.set(f"${price:.2f}")
        logger.debug("Price updated: %s", self.price_var.get())

    def _save_order(self):
        choice   = self.single_or_combo.get()
        selected = [i for i, var in enumerate(self.meal_vars, 1) if var.get()]

        if choice == 1 and len(selected) != 1:
            messagebox.showwarning("Error", "Single must select exactly 1 meal.")
            return

        if choice == 2 and len(selected) != 2:
            messagebox.showwarning("Error", "Combo must select exactly 2 meals.")
            return

        if choice not in (1, 2):
            messagebox.showwarning("Error", "Please select Single or Combo.")
            return

        data = read_csv(MENU_CSV)[0]
        for idx in selected:
            data[idx][2] = str(int(data[idx][2]) + 1)

        if self.soup_var.get():
            data[11][2] = str(int(data[11][2]) + 1)

        write_csv(MENU_CSV, data)
        messagebox.showinfo("Success", "Your order has been saved!")
        logger.info("Order saved for meals %s with soup=%s", selected, self.soup_var.get())

        self._reset_ui()

    def _reset_ui(self):
        self.student_id_var.set("")
        self.password_var.set("")
        self.single_or_combo.set(0)

        for var in self.meal_vars:
            var.set(0)

        self.soup_var.set(0)
        self.price_var.set("$0.00")
        self._toggle_order_widgets(enabled=False)
        logger.info("UI reset to login state")


if __name__ == "__main__":
    app = SCMSClient()
    app.mainloop()
