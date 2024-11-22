my_dict = {'name': 'Alice'}
try:
    print(my_dict['age'])
except KeyError as e:
    print(f"Error: {e}")
