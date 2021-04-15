# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import data


def main(argv):
    feature = ['cnt', 'hum', 't1', 'season', 'is_holiday']
    main_data = data.load_data("london_sample.csv", feature)
    print(main_data)
    values = {337}
    data1, data2 = data.filter_by_feature(main_data, 'cnt', values)
    print(data1)
    print(data2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
