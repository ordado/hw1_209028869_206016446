import pandas
import sys


def load_data(path, features):
    df = pandas.read_csv(path, usecols=features)
    data = df.to_dict(orient="list")
    feature_sholud_to_delete = []
    for data_key in data.keys():
        flag = 0
        for elem_features in features:
            if elem_features == data_key:
                flag = 1
        if flag == 0:
            feature_sholud_to_delete.append(data_key)
    for elem in feature_sholud_to_delete:
        del data[elem]
    return data


def filter_by_feature(data, feature, values):
    ok = {}.fromkeys(data, [])
    bad = {}.fromkeys(data, [])

    for key in data.keys():
        ok[key] = []
        bad[key] = []

    for i in range(len(data[feature])):
        if data[feature][i] in values:
            append_row(data, ok, i)
        else:
            append_row(data, bad, i)

    return ok, bad


def append_row(data, new, index):
    for key in data.keys():
        new[key].append(data[key][index])


def print_details(data, features, statistics_functions):
    for key in features:
        if key not in data.keys():
            continue
        print(f"{key}:", end=' ')
        for i, f in enumerate(statistics_functions):
            if i == len(statistics_functions) - 1:
                w = f(data[key])
                print(f"{w}")
            else:
                w = f(data[key])
                print(f"{w}, ", end='')
