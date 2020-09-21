import json
import string


def number_of_placeholder(placeholder_info):
    characters = string.ascii_lowercase + string.ascii_uppercase + " "
    start = 0
    end = 1
    num_of_placeholder = ""
    while True:
        if placeholder_info[start:end] not in characters:
            num_of_placeholder += placeholder_info[start:end]
            start += 1
            end += 1
        else:
            break
    return int(num_of_placeholder)


def frequency_table(dict):
    freq_dict = {}
    for key in dict.keys():
        key_freq_dict = number_of_placeholder(key)
        if key_freq_dict not in freq_dict.keys():
            freq_dict[key_freq_dict] = 1
        else:
            freq_dict[key_freq_dict] += 1
    return freq_dict


def add_spaces(placeholder):
    if "Text" in placeholder:
        spaces =  4 * " "
    elif "Table" in placeholder:
        spaces =  3 * " "
    else:
        spaces =  1 * " "
    return spaces       


def read_data_json(filename):

    # Opening JSON file
    with open(filename) as read_file:

        # returns JSON object as a dictionary
        data = json.load(read_file)
    return data


def store_data_json(content):

    # The json file where the output must be stored
    with open("wire_up_new.json", "w") as out_file:

        # Returns JSON object as a dictionary
        json.dump(content, out_file, indent=6)
    return "wire_up_new.json"