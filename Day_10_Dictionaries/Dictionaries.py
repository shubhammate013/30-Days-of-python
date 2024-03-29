# Dictionaries

# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary

# To create a dictionary we use curly brackets, {} or the *dict()* built-in function.
# Creating an empty dictionariy

empty_dict = {}

# syntax
'''
empty_dict = {}

'''
# Dictionary with data values
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

'''


person = {
    'first_name':'shubham',
    'last_name':'Mate',
    'age':22,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }


# The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

# Dictionary Length
# It checks the number of 'key: value' pairs in the dictionary.


# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

'''


person = {
    'first_name':'shubham',
    'last_name':'mate',
    'age':22,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7



### Accessing Dictionary Items

# We can access Dictionary items by referring to its key name.

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4

'''

person = {
    'first_name':'shubham',
    'last_name':'Mate',
    'age':22,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # shubham
print(person['country'])    # India
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error


# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the _get_ method. The get method returns None, which is a NoneType object data type, if the key does not exist.

person = {
    'first_name':'shubham',
    'last_name':'mate',
    'age':22,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # shubham
print(person.get('country'))    # mate
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None


# Adding Items to a Dictionary

# We can add new key and value pairs to a dictionary

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

'''


person = {
    'first_name':'shubham',
    'last_name':'mate',
    'age':22,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


# Modifying Items in a Dictionary

# We can modify items in a dictionary

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

'''

person = {
    'first_name':'shubham',
    'last_name':'Mate',
    'age':22,
    'country':'India',
    'is_marred':False,   
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Mr.'
person['age'] = 23


### Checking Keys in a Dictionary

# We use the _in_ operator to check if a key exist in a dictionary

# syntax

'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

'''

### Removing Key and Value Pairs from a Dictionary

# - _pop(key)_: removes the item with the specified key name:
# - _popitem()_: removes the last item
# - _del_: removes an item with specified key name

# syntax

'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

'''

person = {
    'first_name':'shubham',
    'last_name':'Mate',
    'age':22,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item


### Changing Dictionary to a List of Items

# The _items()_ method changes dictionary to a list of tuples.

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

'''
### Clearing a Dictionary

# If we don't want the items in a dictionary we can clear them using _clear()_ method

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

'''
### Deleting a Dictionary

# If we do not use the dictionary we can delete it completely


# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

'''
### Copy a Dictionary

# We can copy a dictionary using a _copy()_ method. Using copy we can avoid mutation of the original dictionary.

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

'''
### Getting Dictionary Keys as a List

# The _keys()_ method gives us all the keys of a a dictionary as a list.

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

'''
### Getting Dictionary Values as a List

# The _values_ method gives us all the values of a a dictionary as a list.

# syntax
'''
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

'''

