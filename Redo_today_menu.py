import csv


def remake():
    with open('today_menu.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([['number', 'lunch', 'orders', 'price', 'combo'],
                          [1, '1', 0, 0, 0],
                          [2, '2', 0, 0, 0],
                          [3, '3', 0, 0, 0],
                          [4, '4', 0, 0, 0],
                          [5, '5', 0, 0, 0],
                          [6, '6', 0, 0, 0],
                          [7, '7', 0, 0, 0],
                          [8, '8', 0, 0, 0],
                          [9, '9', 0, 0, 0],
                          [10, '10', 0, 0, 0],
                          ['Soup', '', 0, 0, None]]
                         )
    return True

if __name__ == '__main__':
    remake()