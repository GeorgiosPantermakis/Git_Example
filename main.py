import string
import os
import sys 
import getopt
from support_functions import read_data_json, store_data_json

data = read_data_json(filename = 'wire_up.json')

step_forword = None
starting_point = None

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, "s:f:",["starting_point=", "step_forword="])

for opt, arg in opts:
    if opt in ('-s', '--starting_point'):
        starting_point = int(arg)
    elif opt in ('-f', '--step_forword'):
        step_forword = int(arg)
print(starting_point)
step_forword = 1 if step_forword is None else step_forword
starting_point = 1 if starting_point is None else starting_point

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
        new_number_of_placeholder = old_number_of_placeholder + step_forword
        placeholder = str(new_number_of_placeholder) + " " + key[len(str(new_number_of_placeholder))+1:]
        new_data[placeholder] = value
    else:
        placeholder = str(old_number_of_placeholder) + " " + key[len(str(old_number_of_placeholder))+1:]
        new_data[placeholder] = value
 
new_wire_up = store_data_json(content = new_data)
path = os.getcwd() + "\\" + new_wire_up
print("The new wire-up.json stored in {path}".format(path = path))