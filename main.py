# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import data
import sta
import sys

def main(argv):
    print(argv)
    d = data.load_data(argv[1], argv[2].split(', '))
    d, x = data.filter_by_feature(d, 'season', [1])
    d, x = data.filter_by_feature(d, 'is_holiday', [1])
    data.print_details(d, ['hum'], [statistics.sum, statistics.mean, statistics.median])

############################  Q2  ##################################################
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
