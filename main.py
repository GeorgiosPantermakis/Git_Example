import os
import sys
import getopt
from support_functions import number_of_placeholder, frequency_table, read_data_json, store_data_json

step_forward = None
starting_point = None
path = None

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, "s:f:d:", ["starting_point=", "step_forward=", "path="])

for opt, arg in opts:
    if opt in ("-s", "--starting_point"):
        starting_point = int(arg)
    elif opt in ("-f", "--step_forward"):
        step_forward = int(arg)
    elif opt in ("-p", "--path"):
        path = arg

step_forward = 1 if step_forward is None else step_forward
starting_point = 1 if starting_point is None else starting_point
path = "wire_up.json" if path is None else path

data = read_data_json(filename=path)

new_data = {}
freq = frequency_table(data)
counter = 0
for key, value in data.items():
    counter += 1
    current_number_of_placeholder = number_of_placeholder(placeholder_info=key)
    if current_number_of_placeholder >= starting_point:
        new_number_of_placeholder = current_number_of_placeholder + step_forward
        placeholder = (str(new_number_of_placeholder) + " " + key[len(str(current_number_of_placeholder)) + 1 :])
        new_data[placeholder] = value
        fake_placeholder = new_number_of_placeholder
    else:
        placeholder = (str(current_number_of_placeholder) + " " + key[len(str(current_number_of_placeholder)) + 1 :])
        new_data[placeholder] = value
        fake_placeholder = current_number_of_placeholder

    if freq[current_number_of_placeholder] == counter:
        fake_placeholder = str(fake_placeholder) + " Drop this textline"
        new_data[fake_placeholder] = ""
        counter = 0

new_wire_up = store_data_json(content=new_data)
filepath = os.getcwd() + "\\" + new_wire_up
print("The new wire-up.json stored in {path}".format(path=filepath))