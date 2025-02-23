# libraries Import
from tkinter import *
import customtkinter
from tkinter import messagebox
import re
from csv_rw import *
import account_maker
import password_enter

# Main Window Properties

window = Tk()
window.title("SCMS-Client")
window.geometry("800x350")

window.configure(bg="#0091ff")

single_or_combo = IntVar()
pwd1 = '123456'
entered_password = ''


def pwd():
    global entered_password
    password_enter.pe()
    entered_password = read_txt('password.txt')[0]


def update_price(meal_number):
    print(meal_number)
    data = read_csv('today_menu.csv')
    data = data[0]
    # print(data)
    foods = num_of_food()[1]
    price = 0
    if len(foods) == 1:
        price += int(data[foods[0]][3])
    if len(foods) == 2:
        price += int(data[foods[0]][3]) + int(data[foods[0]][4])
    if soup_checkbox.get() == 1:
        price += int(data[11][3])
    if price == 0:
        Price_shower.configure(text='$...')
        return
    Price_shower.configure(text='$' + str(price))


def num_of_food():
    n = 0
    foods = []
    if meal_1_choice.get():
        n += 1
        foods.append(1)
    if meal_2_choice.get():
        n += 1
        foods.append(2)
    if meal_3_choice.get():
        n += 1
        foods.append(3)
    if meal_4_choice.get():
        n += 1
        foods.append(4)
    if meal_5_choice.get():
        n += 1
        foods.append(5)
    if meal_6_choice.get():
        n += 1
        foods.append(6)
    if meal_7_choice.get():
        n += 1
        foods.append(7)
    if meal_8_choice.get():
        n += 1
        foods.append(8)
    if meal_9_choice.get():
        n += 1
        foods.append(9)
    if meal_10_choice.get():
        n += 1
        foods.append(10)
    return n, foods


def save():
    print(single_or_combo.get())
    if single_or_combo.get() == 1:
        if num_of_food()[0] == 1:
            data_in_menu = read_csv('today_menu.csv')
            data_in_menu[num_of_food()[1][0]][2] = int(data_in_menu[num_of_food()[1][0]][2]) + 1
            if soup_checkbox.get() == 1:
                data_in_menu[11][2] = int(data_in_menu[11][2]) + 1
            write_csv('today_menu.csv', data_in_menu)
            messagebox.showinfo('Success', 'Your order have been saved!')
            frost()
        else:
            messagebox.showwarning('Error', 'You can only choose one food for single! \n If you want two, consider '
                                            'choosing combo')
    elif single_or_combo.get() == 2:
        if num_of_food()[0] == 2:
            print(num_of_food())
            data_in_menu = read_csv('today_menu.csv')
            data_in_menu = data_in_menu[0]
            data_in_menu[num_of_food()[1][0]][2] = int(data_in_menu[num_of_food()[1][0]][2]) + 1
            data_in_menu[num_of_food()[1][1]][2] = int(data_in_menu[num_of_food()[1][1]][2]) + 1
            if soup_checkbox.get() == 1:
                data_in_menu[11][2] = int(data_in_menu[11][2]) + 1
            write_csv('today_menu.csv', data_in_menu)
            messagebox.showinfo('Success', 'Your order have been saved!')
            frost()
        else:
            messagebox.showwarning('Error', 'You can only choose two food for combo! \n if you want less, consider '
                                            'choosing single')
    else:
        messagebox.showwarning('Error', 'Please choose for Single or combo')


def defrost():
    print('hi')
    data_in_menu = read_csv('today_menu.csv')
    data_in_menu = data_in_menu[0]
    print(data_in_menu)

    RadioButton_single.configure(state='normal')
    RadioButton_combo.configure(state='normal')
    meal_1_choice.configure(state='normal')
    meal_1_choice.configure(text=data_in_menu[1][1])

    meal_2_choice.configure(state='normal')
    meal_2_choice.configure(text=data_in_menu[2][1])

    meal_3_choice.configure(state='normal')
    meal_3_choice.configure(text=data_in_menu[3][1])

    meal_4_choice.configure(state='normal')
    meal_4_choice.configure(text=data_in_menu[4][1])

    meal_5_choice.configure(state='normal')
    meal_5_choice.configure(text=data_in_menu[5][1])

    meal_6_choice.configure(state='normal')
    meal_6_choice.configure(text=data_in_menu[6][1])

    meal_7_choice.configure(state='normal')
    meal_7_choice.configure(text=data_in_menu[7][1])

    meal_8_choice.configure(state='normal')
    meal_8_choice.configure(text=data_in_menu[8][1])

    meal_9_choice.configure(state='normal')
    meal_9_choice.configure(text=data_in_menu[9][1])

    if data_in_menu[10][1] != 'No tenth food for today!':
        meal_10_choice.configure(state='normal')
        meal_10_choice.configure(text=data_in_menu[10][1])
    else:
        meal_10_choice.configure(text='No tenth food for today!')

    soup_checkbox.configure(state='normal')
    soup_checkbox.configure(text='Soup:' + data_in_menu[11][1])
    done_button.configure(state='normal')
    cancel_button.configure(state='normal')
    Login_button.configure(state='disabled')
    student_number_entry.configure(state='disabled')
    password_entry.configure(state='disabled')


def frost():
    RadioButton_single.configure(state='disabled')
    RadioButton_combo.configure(state='disabled')
    meal_1_choice.configure(state='disabled')
    meal_1_choice.deselect()

    meal_2_choice.configure(state='disabled')
    meal_2_choice.deselect()

    meal_3_choice.configure(state='disabled')
    meal_3_choice.deselect()

    meal_4_choice.configure(state='disabled')
    meal_4_choice.deselect()

    meal_5_choice.configure(state='disabled')
    meal_5_choice.deselect()

    meal_6_choice.configure(state='disabled')
    meal_6_choice.deselect()

    meal_7_choice.configure(state='disabled')
    meal_7_choice.deselect()

    meal_8_choice.configure(state='disabled')
    meal_8_choice.deselect()

    meal_9_choice.configure(state='disabled')
    meal_9_choice.deselect()

    meal_10_choice.configure(state='disabled')
    meal_10_choice.deselect()

    soup_checkbox.configure(state='disabled')
    done_button.configure(state='disabled')
    cancel_button.configure(state='disabled')
    student_number_entry.configure(state='normal')
    student_number_entry.configure(textvariable='')
    password_entry.configure(state='normal')
    Login_button.configure(state='normal')
    student_number_entry.focus()


def start():
    print(student_number_entry.get(), password_entry.get())
    if student_number_entry.get() == 'admin' and password_entry.get() == pwd1:
        account_maker.am()
    else:
        data_in_file = read_csv('students.csv')
        data_in_file = data_in_file[0]
        if len(student_number_entry.get()) != 8 or re.search(r'(\d{8})', student_number_entry.get()) is None:
            messagebox.showerror('Wrong student number', 'Please try again')
            return
        for i in data_in_file:
            print(i)
            if student_number_entry.get() in i:
                if password_entry.get() == i[1]:
                    defrost()
                else:
                    messagebox.showerror('Wrong password', 'Please try again')
                    return


# Title
titleLabel = customtkinter.CTkLabel(
    master=window,
    text="School Canteen Management System - Order",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=300,
    corner_radius=0,
    bg_color="#0091ff",
    fg_color="#0091ff",
)
titleLabel.place(x=250, y=10)

# Student number label & password
student_number_label = customtkinter.CTkLabel(
    master=window,
    text="Student Number",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=110,
    corner_radius=0,
    bg_color="#0091ff",
    fg_color="#0091ff",
)
student_number_label.place(x=380, y=90)

password_number_label = customtkinter.CTkLabel(
    master=window,
    text="Password",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#0091ff",
    fg_color="#0091ff",
)
password_number_label.place(x=380, y=130)

# Student Number & password entry
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
    bg_color="#0091ff",
    fg_color="#F0F0F0",
)
student_number_entry.place(x=500, y=90)

password_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="password",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#0091ff",
    fg_color="#F0F0F0",
)
password_entry.place(x=500, y=130)
# Login
Login_button = customtkinter.CTkButton(
    master=window,
    text="Login",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#0091ff",
    fg_color="#F0F0F0",
    command=start
)
Login_button.place(x=600, y=180)

# Radiobutton
RadioButton_single = customtkinter.CTkRadioButton(
    master=window,
    variable=single_or_combo,
    value=1,
    text="Single",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
)
RadioButton_single.place(x=20, y=70)
RadioButton_combo = customtkinter.CTkRadioButton(
    master=window,
    variable=single_or_combo,
    value=2,
    text="Combo",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
)
RadioButton_combo.place(x=160, y=70)

# Meal 1
meal_1_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 1",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(1)
)
meal_1_choice.place(x=30, y=120)

# Meal 2
meal_2_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 2",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(2)
)
meal_2_choice.place(x=30, y=150)

# Meal 3
meal_3_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 3",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(3)
)
meal_3_choice.place(x=30, y=180)

# Meal 4
meal_4_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 4",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(4)
)
meal_4_choice.place(x=30, y=210)

# Meal 5
meal_5_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 5",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(5)
)
meal_5_choice.place(x=30, y=240)

# Meal 6
meal_6_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 6",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(6)
)
meal_6_choice.place(x=180, y=120)

# Meal 7
meal_7_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 7",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(7)
)
meal_7_choice.place(x=180, y=150)

# Meal 8
meal_8_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 8",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(8)
)
meal_8_choice.place(x=180, y=180)

# Meal 9
meal_9_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 9",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(9)
)
meal_9_choice.place(x=180, y=210)

# Meal 10
meal_10_choice = customtkinter.CTkCheckBox(
    master=window,
    text="Meal 10",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(10)
)
meal_10_choice.place(x=180, y=240)

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
    bg_color="#0091ff",
    fg_color="#F0F0F0",
    command=save
)
done_button.place(x=150, y=290)
# Cancel
cancel_button = customtkinter.CTkButton(
    master=window,
    text="Cancel",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#0091ff",
    fg_color="#F0F0F0",
    command=frost
)
cancel_button.place(x=250, y=290)

soup_checkbox = customtkinter.CTkCheckBox(
    master=window,
    text="Soup",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    command=lambda: update_price(11)
)
soup_checkbox.place(x=390, y=240)

Price_shower = customtkinter.CTkLabel(
    master=window,
    text="Price",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#0091ff",
    fg_color="#0091ff",
)
Price_shower.place(x=560, y=240)

frost()

# run the main loop
window.mainloop()
