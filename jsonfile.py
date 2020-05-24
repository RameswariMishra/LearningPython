import json
with open('/Users/rameswarimishra/Library/Preferences/PyCharmCE2019.3/scratches/Employee.json') as f:
    data = json .load(f)
print(data)

languages = '{"programming": ["python","C","Java"], "aws":["dev ops","cloud engineering"]}'
language_dict = json.loads(languages)
print(language_dict)

emp_dict = {'name': 'Bob', 'age': 30, 'children': None}

emp_json = json.dumps(emp_dict)

print(emp_json)

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('person.json', 'w') as json_file:
  json.dump(person_dict, json_file)

