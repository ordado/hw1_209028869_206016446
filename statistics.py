import math


def sum(values):
    """

    :param values: a list of numbers
    :return sum of the numbers in the list
    """
    s = 0
    for value in values:
        s += value
    return s


def mean(values):
    """

    :param values: values: a list of numbers
    :return average of the numbers in the list
    """
    s = sum(values)
    return s / len(values)


def median(values):
    """

    :param values: values: a list of numbers
    :return median number of the sorted list
    """
    values.sort()
    len_of_values = len(values)
    if len_of_values % 2 == 0:
        len_of_values = int(len_of_values / 2) - 1
        return (values[len_of_values] + values[len_of_values + 1]) / 2
    else:
        return float(values[math.ceil((len_of_values - 1) / 2)])


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """

    :param feature_description: a string that describes the name
    :param data: a dict-keys are the features, values are lists indicating the key's value
    :param treatment: a key from the data
    :param target: a key from the data
    :param threshold: indicates threshold value for the key 'treatment'
    :param is_above: false or true
    :param statistic_functions: statistics functions from this module

    **     prints statistical information according to the arguments
    """
    filter_target = []
    if is_above:
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
