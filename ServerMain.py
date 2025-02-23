import re
import csv
from Redo_today_menu import remake


class Brain:
    def __init__(self):
        self.data_in_menu = []

    def print_data(self):
        print(self.data_in_menu)

    def format_data_in_menu(self, input_list):
        """Method used by other functions, removes tabs from 2D list"""
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

    def set_up(self):
        """Returns the data in menu"""
        with open('today_menu.csv') as f:
            my_reader = csv.reader(f, delimiter=',')
            self.data_in_menu.append(list(my_reader))
        data_in_menu = self.data_in_menu[0]
        # print(data_in_menu)
        data_in_menu = self.format_data_in_menu(data_in_menu)
        return data_in_menu

    def save_data(self, x, y, new):
        """Easy Way to change data_in_menu"""
        self.data_in_menu[x][y] = new

    def reset(self):
        remake()

    def save(self, input_list):
        with open('today_menu.csv', 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(input_list)
        return True


if __name__ == "__main__":
    b = Brain()
    b.set_up()
