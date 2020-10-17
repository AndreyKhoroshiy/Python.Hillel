import os


def get_way(path=r"C:\Users\Тарас\Python.Hillel"):
    list_dir = os.listdir(path)
    dict_ff = {"files": [], "folders": []}
    for object in list_dir:
        way_object = os.path.join(path, object)
        if os.path.isfile(way_object):
            dict_ff["files"].append(object)
        else:
            dict_ff["folders"].append(object)
    print(dict_ff)


get_way()