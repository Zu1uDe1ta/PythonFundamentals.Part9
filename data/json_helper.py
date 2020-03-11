import json

json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

def read_json(str):
    parsed_json = (json.loads(json_data))
    print(json.dumps(parsed_json, indent=4, sort_keys=True))

read_json(json_data)

def read_all_json_files(str):
    loaded_json = json.loads(json_data)
    for x in loaded_json:
        print("%s: %d" % (x, loaded_json[x]))

read_all_json_files(json_data)

import pickle

def write_pickle(data, f):
    with open('data.pkl', 'wb') as f:
        super_smash_characters.pickle = pickle.dump(data, f)

def load_pickle(data, f):
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
        print(data)
