import csv


def remake():
    with open('today_menu.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([['number', 'lunch', 'orders', 'price', 'combo'],
                          [1, 'q', 0, 0, 0],
                          [2, 'w', 0, 0, 0],
                          [3, 'e', 0, 0, 0],
                          [4, 'r', 0, 0, 0],
                          [5, 't', 0, 0, 0],
                          [6, 'y', 0, 0, 0],
                          [7, 'u', 0, 0, 0],
                          [8, 'i', 0, 0, 0],
                          [9, 'o', 0, 0, 0],
                          [10, 'p', 0, 0, 0],
                          ['Soup', 'asdf', 0, 0, None]]
                         )
    return True

if __name__ == '__main__':
    remake()