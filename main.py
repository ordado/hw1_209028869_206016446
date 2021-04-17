# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data
import sys
import statistics


def main(argv):
#argv[1], argv[2].split(', ')
#####################################  Q1  ##############################################################
    print(argv)
    d = data.load_data("london_sample.csv", ['season', 't1', 'is_holiday', 'cnt', 'hum'])
    print("Question 1:")
    print("Summer:")
    d1, d2 = data.filter_by_feature(d, 'season', [1])
    data.print_details(d1, ['hum', 't1', 'cnt'], [statistics.sum, statistics.mean, statistics.median])
    print("Holiday:")
    d1, d2 = data.filter_by_feature(d, 'is_holiday', [1])
    data.print_details(d1, ['hum', 't1', 'cnt'], [statistics.sum, statistics.mean, statistics.median])
    print("All:")
    data.print_details(d, ['hum', 't1', 'cnt'], [statistics.sum, statistics.mean, statistics.median])






    ############################  Q2  ##################################################
    print("Question 2:")
    print("If t1<=13.0, then:")
    print("Winter holiday records:")
    data_main = data.load_data("london_sample.csv", ['season', 't1', 'is_holiday', 'cnt', 'hum'])
    d1, d2 = data.filter_by_feature(data_main, 'season', [3])
    winter_holiday, is_not_holiday = data.filter_by_feature(d1, 'is_holiday', [1])
    statistics.population_statistics('cnt', winter_holiday, 't1', 'cnt', 13.0, False,
                                     [statistics.mean, statistics.median])
    print("Winter weekday records:")
    statistics.population_statistics('cnt', is_not_holiday, 't1', 'cnt', 13.0, False,
                                     [statistics.mean, statistics.median])
    print("If t1>13.0, then:")
    print("Winter holiday records:")
    statistics.population_statistics('cnt', winter_holiday, 't1', 'cnt', 13.0, True,
                                     [statistics.mean, statistics.median])
    print("Winter weekday records:")
    statistics.population_statistics('cnt', is_not_holiday, 't1', 'cnt', 13.0, True,
                                     [statistics.mean, statistics.median])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
