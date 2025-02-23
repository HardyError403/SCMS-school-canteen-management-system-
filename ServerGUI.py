# libraries Import
from tkinter import *
import customtkinter
import ServerMain
from tkinter import messagebox

b = ServerMain.Brain
print(b().set_up())


def save():
    # food names
    temp = b().set_up()
    temp[1][1] = food1_name_entry.get()
    temp[2][1] = food2_name_entry.get()
    temp[3][1] = food3_name_entry.get()
    temp[4][1] = food4_name_entry.get()
    temp[5][1] = food5_name_entry.get()
    temp[6][1] = food6_name_entry.get()
    temp[7][1] = food7_name_entry.get()
    temp[8][1] = food8_name_entry.get()
    temp[9][1] = food9_name_entry.get()
    # b().save_data(1, 1, food1_name_entry.get())
    # b().save_data(2, 1, food2_name_entry.get())
    # b().save_data(3, 1, food3_name_entry.get())
    # b().save_data(4, 1, food4_name_entry.get())
    # b().save_data(5, 1, food5_name_entry.get())
    # b().save_data(6, 1, food6_name_entry.get())
    # b().save_data(7, 1, food7_name_entry.get())
    # b().save_data(8, 1, food8_name_entry.get())
    # b().save_data(9, 1, food9_name_entry.get())
    # the special food
    if food10_checkbox.get() == 1:
        temp[10][1] = food10_name_entry.get()
        # b().save_data(10, 1, food9_name_entry.get())
    else:
        temp[10][1] = 'No tenth food for today!'
        # b().save_data(10, 1, 'No tenth food for today!')

    temp[11][1] = soup_name_entry.get()
    temp[11][3] = soup_price_entry.get()

    # write price
    for i in range(1, 11):
        temp[i][3] = price_entry.get()
        # b().save_data(i, 3, price_entry.get()

    # combo price
    for i in range(1, 11):
        temp[i][4] = combo_add_price_entry.get()
        # b().save_data(i, 4, combo_add_price_entry.get())

    print(temp)

    if b().save(temp):
        messagebox.showinfo('Saved', 'Today\'s meal has been saved')


# Main Window Properties
window = Tk()
window.title("SCMS-Canteen Side")
window.geometry("1000x350")
window.configure(bg="#00ff88")

# Place the Title
title_label = customtkinter.CTkLabel(
    master=window,
    text="School Canteen Management System",
    font=("Arial", 20),
    text_color="#000000",
    height=30,
    width=400,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
title_label.place(x=210, y=0)

# Food

# Food Entry 1
food1_label = customtkinter.CTkLabel(
    master=window,
    text="1.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food1_label.place(x=0, y=90)

food1_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food1_name_entry.place(x=100, y=90)

# Food Entry 2

food2_label = customtkinter.CTkLabel(
    master=window,
    text="2.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food2_label.place(x=0, y=120)

food2_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food2_name_entry.place(x=100, y=120)

# Food Entry 3

food3_label = customtkinter.CTkLabel(
    master=window,
    text="3.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food3_label.place(x=0, y=150)

food3_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food3_name_entry.place(x=100, y=150)

# Food Entry 4

food4_label = customtkinter.CTkLabel(
    master=window,
    text="4.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food4_label.place(x=0, y=180)

food4_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food4_name_entry.place(x=100, y=180)

# Food Entry 5

food5_label = customtkinter.CTkLabel(
    master=window,
    text="5.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food5_label.place(x=0, y=210)

food5_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food5_name_entry.place(x=100, y=210)

# Food Entry 6

food6_label = customtkinter.CTkLabel(
    master=window,
    text="6.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food6_label.place(x=300, y=90)

food6_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food6_name_entry.place(x=400, y=90)

# Food Entry 7

food7_label = customtkinter.CTkLabel(
    master=window,
    text="7.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food7_label.place(x=300, y=120)

food7_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food7_name_entry.place(x=400, y=120)

# Food Entry 8

food8_label = customtkinter.CTkLabel(
    master=window,
    text="8.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food8_label.place(x=300, y=150)

food8_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food8_name_entry.place(x=400, y=150)

# Food Entry 9

food9_label = customtkinter.CTkLabel(
    master=window,
    text="9.",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
food9_label.place(x=300, y=180)

food9_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food9_name_entry.place(x=400, y=180)

# Food Entry 10

food10_checkbox = customtkinter.CTkCheckBox(
    master=window,
    text="Enable 10.",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
)
food10_checkbox.place(x=300, y=210)

food10_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type food name here...",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
food10_name_entry.place(x=410, y=210)

# Soup
soup_label = customtkinter.CTkLabel(
    master=window,
    text="Soup",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
soup_label.place(x=600, y=90)
soup_label = customtkinter.CTkLabel(
    master=window,
    text="Soup ($)",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
soup_label.place(x=600, y=120)

soup_name_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Soup name",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
soup_name_entry.place(x=700, y=90)

soup_price_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Soup Price",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
soup_price_entry.place(x=700, y=120)
# Price setter

# Normal price

price_label = customtkinter.CTkLabel(
    master=window,
    text="Price ($)",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
price_label.place(x=0, y=250)

price_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Price of each meal",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
price_entry.place(x=100, y=250)

# Combo_price
combo_label = customtkinter.CTkLabel(
    master=window,
    text="Combo",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#00ff88",
    fg_color="#00ff88",
)
combo_label.place(x=310, y=250)
combo_add_price_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="$+?",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
)
combo_add_price_entry.place(x=410, y=250)

# Done button

done_button = customtkinter.CTkButton(
    master=window,
    text="Done",
    font=("Arial", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#00ff88",
    fg_color="#F0F0F0",
    command=save
)
done_button.place(x=290, y=300)

# run the main loop
window.mainloop()
