import json

#encoding = dictonary to json 

# json.dump() convert dictonary to json format
# json.dumps() convert string to json format


python_data = {

    "name": "bob",

    "items": [10,20,30],

    "is_vip": False
}

# with open("test.json", "w") as obj1:
#     json.dump(python_data, obj1 , indent=4)


# print(json.dumps(python_data))


#########decoding ====>>> json to python


# load()
# loads()


# with open("test.json") as f:
#     print(json.load(f))


json_input_string = '{"city": "london", "temp": 15.5, "unit": true}'

print(json.loads(json_input_string))