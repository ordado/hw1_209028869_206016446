import sys
import pandas
import math


def sum(values):
    s = 0
    for value in values:
        s += value
    return s


def mean(values):
    s = sum(values)
    return (s / len(values))


def median(values):
    values.sort()
    l = len(values)
    if l % 2 == 0:
        l = (int)(l / 2) - 1
        return (values[l] + values[l + 1]) / 2
    else:
        return values[math.ceil(l / 2) - 1]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    filter_target = []
    if is_above == True:
        row_above_target = []
        data_treatment = data[treatment]
        for i, val in enumerate(data_treatment):
            if val > threshold:
                row_above_target.append(i)

        data_target = data[target]

        for i, elem_target in enumerate(data_target):
            for index_row in row_above_target:
                if index_row == i:
                    filter_target.append(elem_target)
    else:
        row_under_target = []
        data_treatment = data[treatment]
        for i, val in enumerate(data_treatment):
            if val <= threshold:
                row_under_target.append(i)

        data_target = data[target]

        for i, elem_target in enumerate(data_target):
            for index_row in row_under_target:
                if index_row == i:
                    filter_target.append(elem_target)
    print(feature_description, end=': ')
    for i, elem_statistic in enumerate(statistic_functions):
        if i == len(statistic_functions) - 1:
            print(elem_statistic(filter_target))
        else:
            print(elem_statistic(filter_target), end=', ')
