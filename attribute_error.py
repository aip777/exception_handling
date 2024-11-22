class Example:
    pass

obj = Example()
try:
    obj.non_existent_attribute
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'Example' object has no attribute 'non_existent_attribute'
