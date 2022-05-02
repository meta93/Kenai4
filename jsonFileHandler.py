import json
def readJsonFile(fileName): #Define the function that will read the file
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data


