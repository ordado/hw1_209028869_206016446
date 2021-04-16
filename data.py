import pandas
import sys


def load_data(path, features):
    df = pandas.read_csv(path, usecols=features)
    data = df.to_dict(orient="list")
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
    for key in data.keys():
        if key not in features:
            continue
        print(f"Printing details for {key}...")
        for f in statistics_functions:
            w=f(data[key])
            print(f"Executing {f.__name__}: {w}")
