import customtkinter as ctk
from tkinter import messagebox
import ServerMain

class CanteenUI:
    def __init__(self, root):
        self.brain = ServerMain.Brain()
        self.root = root
        self.root.title("SCMS - Canteen Side")
        # Don’t set a fixed geometry; we’ll size it to fit.

        self.entries = {}
        self._build_header()
        self._build_food_entries()
        self._build_soup_section()
        self._build_price_section()
        self._build_done_button()

        # After all widgets are laid out, force an update
        self.root.update_idletasks()
        # Query the size needed to display everything
        # width  = self.root.winfo_reqwidth()
        # height = self.root.winfo_reqheight()
        # Apply that as the window’s geometry
        self.root.geometry("700x600")

    def _build_header(self):
        title = ctk.CTkLabel(
            master=self.root,
            text="School Canteen Management System",
            font=("Arial", 20)
        )
        title.grid(row=0, column=0, columnspan=4, pady=(10, 20))

    def _build_food_entries(self):
        frame = ctk.CTkFrame(master=self.root)
        frame.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10)

        for idx in range(1, 10):
            lbl = ctk.CTkLabel(frame, text=f"{idx}.", font=("Arial", 14))
            ent = ctk.CTkEntry(frame, placeholder_text="Type food name...", font=("Arial", 14))
            lbl.grid(row=idx-1, column=0, padx=5, pady=3, sticky="e")
            ent.grid(row=idx-1, column=1, padx=5, pady=3, sticky="w")
            self.entries[f"food{idx}"] = ent

        # Tenth food with checkbox
        self.enable_10th = ctk.CTkCheckBox(frame, text="Enable 10.", command=self._toggle_10th)
        self.enable_10th.grid(row=9, column=0, padx=5, pady=3, sticky="e")
        tenth_ent = ctk.CTkEntry(frame, placeholder_text="Type food name...", font=("Arial", 14))
        tenth_ent.configure(state="disabled")
        tenth_ent.grid(row=9, column=1, padx=5, pady=3, sticky="w")
        self.entries["food10"] = tenth_ent

    def _toggle_10th(self):
        state = "normal" if self.enable_10th.get() else "disabled"
        self.entries["food10"].configure(state=state)

    def _build_soup_section(self):
        ctk.CTkLabel(self.root, text="Soup", font=("Arial", 14))\
            .grid(row=1, column=4, padx=5, pady=3, sticky="e")
        self.entries["soup_name"] = ctk.CTkEntry(self.root, placeholder_text="Soup name", font=("Arial", 14))
        self.entries["soup_name"].grid(row=1, column=5, padx=5, pady=3)

        ctk.CTkLabel(self.root, text="Soup ($)", font=("Arial", 14))\
            .grid(row=2, column=4, padx=5, pady=3, sticky="e")
        self.entries["soup_price"] = ctk.CTkEntry(self.root, placeholder_text="Soup Price", font=("Arial", 14))
        self.entries["soup_price"].grid(row=2, column=5, padx=5, pady=3)

    def _build_price_section(self):
        ctk.CTkLabel(self.root, text="Price ($)", font=("Arial", 14))\
            .grid(row=4, column=0, padx=5, pady=20, sticky="e")
        self.entries["meal_price"] = ctk.CTkEntry(self.root, placeholder_text="Each meal price", font=("Arial", 14))
        self.entries["meal_price"].grid(row=4, column=1, padx=5, pady=20)

        ctk.CTkLabel(self.root, text="Combo", font=("Arial", 14))\
            .grid(row=4, column=2, padx=5, pady=20, sticky="e")
        self.entries["combo_add"] = ctk.CTkEntry(self.root, placeholder_text="$+?", font=("Arial", 14))
        self.entries["combo_add"].grid(row=4, column=3, padx=5, pady=20)

    def _build_done_button(self):
        btn = ctk.CTkButton(self.root, text="Done", command=self.save)
        btn.grid(row=5, column=1, columnspan=2, pady=10)

    def save(self):
        data = self.brain.set_up()
        try:
            # Food names
            for i in range(1, 11):
                key = f"food{i}"
                name = self.entries[key].get()
                if i == 10 and not self.enable_10th.get():
                    name = "No tenth food for today!"
                data[i][1] = name

            # Soup
            data[11][1] = self.entries["soup_name"].get()
            data[11][3] = float(self.entries["soup_price"].get())

            # Prices
            price = float(self.entries["meal_price"].get())
            combo = float(self.entries["combo_add"].get())
            for i in range(1, 11):
                data[i][3], data[i][4] = price, combo

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for prices.")
            return

        if self.brain.save(data):
            messagebox.showinfo("Saved", "Today's meal has been saved.")

if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # or "dark"
    root = ctk.CTk()
    app = CanteenUI(root)
    root.mainloop()
