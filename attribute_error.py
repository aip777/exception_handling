class Example:
    pass

obj = Example()
try:
    obj.non_existent_attribute
except AttributeError as e:
    print(f"Error: {e}") 
