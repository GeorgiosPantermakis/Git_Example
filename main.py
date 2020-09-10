import string
import os
from support_functions import read_data_json, store_data_json

data = read_data_json(filename = 'wire_up.json')

seats = 2
starting_point = 10
characters = string.ascii_lowercase + string.ascii_uppercase + ' '
new_data = {}
for key, value in data.items():
    start = 0
    end = 1
    old_number_of_placeholder = ""
    while True:
        if key[start:end] not in characters:
            old_number_of_placeholder += key[start:end]
            start += 1
            end += 1 
        else:
            break
    old_number_of_placeholder = int(old_number_of_placeholder)
    if old_number_of_placeholder >= starting_point:
        new_number_of_placeholder = old_number_of_placeholder + seats
        placeholder = str(new_number_of_placeholder) + " " + key[len(str(new_number_of_placeholder))+1:]
        new_data[placeholder] = value
    else:
        placeholder = str(old_number_of_placeholder) + " " + key[len(str(old_number_of_placeholder))+1:]
        new_data[placeholder] = value
 
new_wire_up = store_data_json(content = new_data)
path = os.getcwd()
print("The new wire-up.json stored in {path}\\{file}".format(path = path, file = new_wire_up))