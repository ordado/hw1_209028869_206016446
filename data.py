import pandas


def load_data(path, features):
    """The method reads the data set from a csv file and uploads the information to the main memory.

    Parameters:
    path (string): Is the full path to the file (at the end of the file name)
    features (list): Is a list of relevant features that we are interested in

    Returns:
    dictionary: Data dictionary, where the keys of the dictionary will be only the relevant attributes

    """

    df = pandas.read_csv(path, usecols=features)
    data = df.to_dict(orient="list")
    feature_to_delete = []
    for data_key in data.keys():
        flag = 0
        for elem_features in features:
            if elem_features == data_key:
                flag = 1
        if flag == 0:
            feature_to_delete.append(data_key)
    for elem in feature_to_delete:
        del data[elem]
    return data


def filter_by_feature(data, feature, values):
    """The method divides a dictionary into two dictionaries based on a particular values of the feature.

        Parameters:
        data (dictionary): Is a dictionary whose keys are properties of the dataset
        feature (string): Is the name of a categorical attribute, that is, its attributes are categories
        values (list): Is a set of values, where the attribute in the feature can have all the values in values

        Returns:
        dictionary: Data1, Data2 Two dictionaries, when their union is the dictionary data.
                    The first dictionary contains all entries in which the feature feature has been given some
                    value appearing in values, and the second dictionary will be a containing dictionary
                    all records in which the feature feature received values that do not appear in values,
                    and only them.
    """

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
    """The method will print statistical indices on data solely

       Parameters:
       data (dictionary): Is a dictionary whose keys are properties from the dataset,
                              and the values are lists that contain the feature values.
       new (dictionary): A dictionary into which the values in the What data in the index line will enter
       index (int): Number of row

    """

    for key in data.keys():
        new[key].append(data[key][index])


def print_details(data, features, statistics_functions):
    """The method will print statistical indices on data solely

       Parameters:
       data (dictionary): Is a dictionary whose keys are properties from the dataset,
                          and the values are lists that contain the feature values.
       features (list): Is a list of features from the dataset.
       statistics_functions (list): A list containing statistical methods found in the statistic.py module

        """

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
