import os
import sys 
import getopt
from support_functions import read_data_json
from support_functions import store_data_json
from support_functions import number_of_placeholder

step_forward = None
starting_point = None
path = None

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, "s:f:d:",["starting_point=", "step_forward=","path="])

for opt, arg in opts:
    if opt in ('-s', '--starting_point'):
        starting_point = int(arg)
    elif opt in ('-f', '--step_forward'):
        step_forward = int(arg)
    elif opt in ('-p', '--path'):
        path = arg

step_forward = 1 if step_forward is None else step_forward
starting_point = 1 if starting_point is None else starting_point
path = 'wire_up.json' if path is None else path

data = read_data_json(filename = path)

new_data = {}
bounder = starting_point
for key, value in data.items():
    
    current_number_of_placeholder = number_of_placeholder(placeholder_info = key)
    if current_number_of_placeholder >= starting_point:
        new_number_of_placeholder = current_number_of_placeholder + step_forward
        placeholder = str(new_number_of_placeholder) + " " + key[len(str(current_number_of_placeholder))+1:]
        new_data[placeholder] = value
    else:
        placeholder = str(current_number_of_placeholder) + " " + key[len(str(current_number_of_placeholder))+1:]
        new_data[placeholder] = value

new_wire_up = store_data_json(content = new_data)
filepath = os.getcwd() + "\\" + new_wire_up
print("The new wire-up.json stored in {path}".format(path = filepath))




# bounder = starting_point
# copy_dict = new_data.copy()
# for key, value in copy_dict.items():
#     current_number_of_placeholder = number_of_placeholder(placeholder_info = key)
#     print(bounder, current_number_of_placeholder, bounder < current_number_of_placeholder)
#     if bounder < current_number_of_placeholder:
#         bounder = current_number_of_placeholder
#         placeholder = str(current_number_of_placeholder) + " " + key[len(str(current_number_of_placeholder))+1:]
#         new_data[placeholder + "X"] = ""