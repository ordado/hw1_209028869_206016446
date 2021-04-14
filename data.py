import pandas


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    save_featrure_should_delete = []
    for list_features in features:
        for key_data in data.keys():                       //1,2,3,4
                                                           //2,3,4,5,6
            if key_data != list_features:
                save_featrure_should_delete.append(key_data)

    for elem in save_featrure_should_delete:
        del data[elem]

    return data


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}
    for elem_data in data[feature]:
        for elem_values in values.items():
            if elem_data == elem_values:
                for keys in data.keys():
                    data1[keys] = data[keys]
            else:
                for keys in data.keys():
                    data2[keys] = data[keys]
    return data1, data2
