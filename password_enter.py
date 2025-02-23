# libraries Import
from tkinter import *
import customtkinter
from csv_rw import *
from tkinter import messagebox


def pe():
    # Main Window Properties

    window = Tk()
    window.title("Tkinter")
    window.geometry("250x200")
    window.configure(bg="#5e5e5e")

    def done():
        write_txt('password.txt', password_entry.get())
        messagebox.showinfo('Password entered', 'You may close this window')


    done_button = customtkinter.CTkButton(
        master=window,
        text="Done",
        font=("undefined", 14),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=30,
        width=95,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#5e5e5e",
        fg_color="#F0F0F0",
        command=done
    )
    done_button.place(x=70, y=140)
    title_label = customtkinter.CTkLabel(
        master=window,
        text="Enter Password Here",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=150,
        corner_radius=0,
        bg_color="#5e5e5e",
        fg_color="#5e5e5e",
    )
    title_label.place(x=50, y=20)
    password_entry = customtkinter.CTkEntry(
        master=window,
        placeholder_text="Password",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=195,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#5e5e5e",
        fg_color="#F0F0F0",
        show='•'
    )
    password_entry.place(x=20, y=80)
    password_entry.focus_force()

    # run the main loop
    window.mainloop()


if __name__ == '__main__':
    pe()
