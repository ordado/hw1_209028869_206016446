# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import data
import statistics


def main(argv):
    print(argv)
    d = data.load_data(argv[1], argv[2].split(', '))
    print("Question 1:")
    print("Summer:")
    d1, d2 = data.filter_by_feature(d, 'season', [1])
    data.print_details(d1, ['hum', 't1', 'cnt'], [statistics.sum, statistics.mean, statistics.median])
    print("Holiday:")
    d1, d2 = data.filter_by_feature(d, 'is_holiday', [1])
    data.print_details(d1, ['hum', 't1', 'cnt'], [statistics.sum, statistics.mean, statistics.median])
    print("All:")
    data.print_details(d, ['hum', 't1', 'cnt'], [statistics.sum, statistics.mean, statistics.median])







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
