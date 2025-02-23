# libraries Import
from tkinter import *
from tkinter import messagebox
import customtkinter
from csv_rw import *
import re

# Main Window Properties
def am():
    window = Tk()
    window.title("Tkinter")
    window.geometry("375x400")
    window.configure(bg="#ffea00")


    # brain
    def format_data_in_menu(input_list):
        counter = [0, 0]
        for i in input_list:
            # print(i)
            for j in i:
                input_list[counter[0]][counter[1]] = re.sub('\t', '', j)
                counter[1] += 1
            counter[0] += 1
            counter[1] = 0
        # print(input_list)
        return input_list


    def save_to_file():
        if new_password_entry.get() != confirm_password_entry.get():
            messagebox.showwarning('Re-enter Password', 'Confirm Password and new password does not match.')
            return False
        if len(student_number_entry.get()) != 8 or re.search(r'(\d{8})', student_number_entry.get()) is None:
            messagebox.showwarning('Re-enter student number', 'The student number should be 00000000~99999999')
            return False
        if student_number_entry.get() == confirm_password_entry.get():
            messagebox.showwarning('Safety Reminder', 'The password is too weak')
            return False

        data_in_file = read_csv('students.csv')
        data_in_file = data_in_file[0]

        # print(data_in_file)
        data_in_file = format_data_in_menu(data_in_file)
        print(data_in_file)

        for i in data_in_file:
            print(1, i)
            print(2, old_password_entry.get())
            if student_number_entry.get() in i:
                print(True)
                if old_password_entry.get() == i[1]:
                    i[1] = confirm_password_entry.get()
                    print(i[1])

                    write_csv('students.csv', data_in_file)

                    messagebox.showinfo('Saved', 'Password and/or student number saved.')
                    return True
                else:
                    messagebox.showerror('Error!', 'Password does not match!')
                    return False
        data_in_file.append([student_number_entry.get(), confirm_password_entry.get()])
        messagebox.showinfo('Saved', 'Password and/or student number saved.')
        write_csv('students.csv', data_in_file)

        print(data_in_file)
        return True


    # title
    title_label = customtkinter.CTkLabel(
        master=window,
        text="Student Register",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=118,
        corner_radius=0,
        bg_color="#ffea00",
        fg_color="#ffea00",
    )
    title_label.place(x=90, y=30)

    # Student number
    student_number_label = customtkinter.CTkLabel(
        master=window,
        text="Student Number",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=110,
        corner_radius=0,
        bg_color="#ffea00",
        fg_color="#ffea00",
    )
    student_number_label.place(x=0, y=110)

    # Student number entry
    student_number_entry = customtkinter.CTkEntry(
        master=window,
        placeholder_text="20XXXXXX",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=195,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ffea00",
        fg_color="#F0F0F0",
    )
    student_number_entry.place(x=130, y=110)

    # Old password label
    old_password_label = customtkinter.CTkLabel(
        master=window,
        text="Old password",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=95,
        corner_radius=0,
        bg_color="#ffea00",
        fg_color="#ffea00",
    )
    old_password_label.place(x=0, y=170)

    # Old password Entry
    old_password_entry = customtkinter.CTkEntry(
        master=window,
        placeholder_text="Placeholder",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=195,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ffea00",
        fg_color="#F0F0F0",
    )
    old_password_entry.place(x=130, y=170)

    # New password label
    new_password_label = customtkinter.CTkLabel(
        master=window,
        text="Password",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=95,
        corner_radius=0,
        bg_color="#ffea00",
        fg_color="#ffea00",
    )
    new_password_label.place(x=0, y=230)

    # New password Entry
    new_password_entry = customtkinter.CTkEntry(
        master=window,
        placeholder_text="New password",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=195,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ffea00",
        fg_color="#F0F0F0",
    )
    new_password_entry.place(x=130, y=230)

    # Confirm password label
    confirm_password_label = customtkinter.CTkLabel(
        master=window,
        text="Confirm Password",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=121,
        corner_radius=0,
        bg_color="#ffea00",
        fg_color="#ffea00",
    )
    confirm_password_label.place(x=0, y=290)

    # Confirm password entry
    confirm_password_entry = customtkinter.CTkEntry(
        master=window,
        placeholder_text="Confirm password",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=195,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ffea00",
        fg_color="#F0F0F0",
    )
    confirm_password_entry.place(x=130, y=290)

    # Done
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
        bg_color="#ffea00",
        fg_color="#F0F0F0",
        command=save_to_file
    )
    done_button.place(x=110, y=360)

    # run the main loop
    window.mainloop()


if __name__ == '__main__':
    am()
