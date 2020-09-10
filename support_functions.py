import json

def read_data_json(filename):
    
    # Opening JSON file 
    with open(filename) as read_file:

        # returns JSON object as a dictionary
        data = json.load(read_file)
    return data    

def store_data_json(content):

    # The json file where the output must be stored
    with open('wire_up_new.json', 'w') as out_file:
    
        # Returns JSON object as a dictionary
        json.dump(content, out_file, indent = 6)
    return 'wire_up_new.json'