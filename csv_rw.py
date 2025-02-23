import csv


def read_csv(filepath):
    temp = []
    with open(filepath, encoding='utf-8-sig') as f:
        my_reader = csv.reader(f, delimiter=',')
        temp.append(list(my_reader))
    return temp


def write_csv(filepath, data):
    with open('today_menu.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def read_txt(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    return lines

def write_txt(filepath, data):
    with open(filepath, 'w') as f:
        f.write(data)

