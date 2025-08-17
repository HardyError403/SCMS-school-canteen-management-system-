> # School Canteen Managing System

## Introduction

* [ ]

## Targeted Users

1. Anyone who wanted to learn GUI designing on python
2. Anyone who get a canteen with a **long** queue and wanted to solve the problem
3. Anyone who wanted to see how a _newbie_ design python app and upload them to github

## How to use

### account_maker.exe

This is a file for creating accounts, accounts should be something like this:

> Username: 8-digit number
> Password: Any combination of letters and numbers

**Warning:** This is a file which can make a huge mess on `students.csv`, file storing students data if used improperly, so this file should not be faced to the public. Instead, this
should be kept by admins

### ClientsideGUI.exe

This is the file which the **students** or **customers** should use, it is for ordering

#### User Manual (for clients)

1. Login with your student number and password
2. Select either you want single (1 meal) or combo (2 meals) and see if you would like to have soup.
3. Check the price and press done to confirm. You will be logged out automaticly

**Important Notice**: Server(canteen) should make neccery changes on ServerGUI.exe to update the meals before the clients order!!!

### Graph_shower.exe

Run this file to see the statistics of today's order

### ServerGUI.exe

Type the food names and soup name here, and enter the prices of them. Note that combo price is calculated like this
Meal Price + Combo(placeholder: _$+?_) = Price of combo
**Notice**: This file should be kept/executed by the server(canteen)

### students.csv

This is a file that stores all student's information, and should be kept by admin

> I reccommand admins to use account_maker.exe to add accounts/change passwords unless you are good at editing csvs

### today_menu.csv

This is a file that stores all menu's information, and should be kept by canteen

> I reccommand admins to use ServerGUI.exe to add accounts/change passwords unless you are good at editing csvs

## Contact me

Found Bugs? Post on `Issues` section or mail me (*hardyshang19@gmail.com*)
Note I am a busy man and a newbie programmer, so please accept my aplogise if I can't solve some of the bugs...

## Next Update checklist

* [ ] Convert .py to .exe
* [ ] Make this readme better
