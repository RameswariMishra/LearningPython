import json
alphabets_json = '{"a":"A","b":"B"}'
alpha_dict = json.loads(alphabets_json)
print(alpha_dict)

new_json = json.dumps(alpha_dict)
print(new_json)

# reading a json file
with open("/Users/rameswarimishra/Library/Preferences/PyCharmCE2019.3/scratches/Employee.json") as f:
    dict_a = json.load(f)

print(dict_a)

# Writing into a json file ie. creating a json file and copying the dictionary into it.

dict_emp = {'name': 'Ram', 'Designation': 'Manager'}

with open('emp.json', 'w') as s:
    json.dump(dict_emp, s)

with open('emp.json') as j:
    dict_emp2 = json.load(j)

print(dict_emp2)
#imnbnmb
