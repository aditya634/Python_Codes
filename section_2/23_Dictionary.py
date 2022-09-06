# Dictionary
# An Dictionary Is An Un ordered Key Value Pair

dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': True
    }
]
print(my_list[0]['a'][2])
print(dictionary['a'][1])

user = {
'basket': [1,2,3],
'greet': 'hello'
}
# get is used to check wheather the key is available in the dictionar or not without getting any error If if is not available the we can assign any value to that key by writing the value after the (coma)
print(user.get('age', 55))

# More dictionary methods https://www.w3schools.com/python/python_ref_dictionary.asp
