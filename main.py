import os
import sys
import getopt
from support_functions import number_of_placeholder, frequency_table, read_data_json, store_data_json

step = 0
beginning = 1
path = "wire_up.json"
textline = False

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, "s:f:b:t:", ["beginning=", "step=", "path=", "textline="])

for opt, arg in opts:
    if opt in ("-b", "--beginning"):
        beginning = int(arg)
    elif opt in ("-s", "--step"):
        step = int(arg)
    elif opt in ("-p", "--path"):
        path = arg
    elif opt in ("-t", "--textline"):
        textline = arg

data = read_data_json(filename=path)

new_data = {}
freq = frequency_table(data)
counter = 0
for key, value in data.items():
    counter += 1
    current_number_of_placeholder = number_of_placeholder(placeholder_info=key)
    if current_number_of_placeholder >= beginning:
        new_number_of_placeholder = current_number_of_placeholder + step
        placeholder = (str(new_number_of_placeholder) + " " + key[len(str(current_number_of_placeholder)) + 1 :])
        new_data[placeholder] = value
        fake_placeholder = new_number_of_placeholder
    else:
        placeholder = (str(current_number_of_placeholder) + " " + key[len(str(current_number_of_placeholder)) + 1 :])
        new_data[placeholder] = value
        fake_placeholder = current_number_of_placeholder

    if freq[current_number_of_placeholder] == counter and textline:
        fake_placeholder = str(fake_placeholder) + " Drop this textline"
        new_data[fake_placeholder] = ""
        counter = 0

new_wire_up = store_data_json(content=new_data)
filepath = os.getcwd() + "\\" + new_wire_up
print("The new wire-up.json stored in {path}".format(path=filepath))