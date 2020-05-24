list_A =[1,1,2,3,4]
set_A = {1,2,3, 'A', 'B', 'C'}


set_B = set(list_A)
print(set_B)

list_B =list(set_A)

print(list_B)

print(set_A.union(set_B))

print(set_A.intersection(set_B))

print(set_A & set_B)

print(set_A | set_B)

print(set_A - set_B)

print(set_B - set_A)

integer_dict ={ 'one':1, 'two':2, 'three':3, 'four':[4,5,6,'abc']}
print(integer_dict)
print(type(integer_dict))
print(integer_dict['four'])
integer_dict['four'].append('hello gaurav')
print(integer_dict['four'])
integer_dict['five'] ='how are you'
print(integer_dict)
print('I am working since {} years, {} months, {} days'.format(integer_dict['one'], integer_dict['two'], integer_dict['three']))
print(integer_dict.keys())
print(integer_dict.values())