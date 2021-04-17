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
    return s / len(values)


def median(values):
    values.sort()
    l = len(values)
    if l % 2 == 0:
        return (values[l // 2] + values[(l // 2) + 1]) / 2
    else:
        return values[l//2]


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
            flag = 0
            for index_row in row_above_target:
                if index_row == i:
                    flag = 1
            if flag == 1:
                filter_target.append(elem_target)
    else:
        row_under_target = []
        data_treatment = data[treatment]
        for i, val in enumerate(data_treatment):
            if val <= threshold:
                row_under_target.append(i)
        data_target = data[target]
        for i, elem_target in enumerate(data_target):
            flag = 0
            for index_row in row_under_target:
                if index_row == i:
                    flag = 1
            if flag == 1:
                filter_target.append(elem_target)
    for elem_statistic in statistic_functions:
        print(feature_description + elem_statistic(filter_target))