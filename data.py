import pandas


def load_data(path, features):
    df = pandas.read_csv(path)
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
    data1 = {}
    data2 = {}
    save_the_number_of_row_to_data1 = []
    feature_list = data[feature]
    for i, val in enumerate(feature_list):
        for k in values:
            if k == val:
                save_the_number_of_row_to_data1.append(i)

    for key in data.keys():
        temp_list = data[key]
        data1.setdefault(key, [])
        data2.setdefault(key, [])
        for index, val in enumerate(temp_list):
            flag = 0
            for k in save_the_number_of_row_to_data1:
                if index == k:
                    flag = 1
                    break
            if flag == 0:
                data2[key].append(val)
            else:
                data1[key].append(val)
    return data1, data2
