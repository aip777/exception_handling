try:
    result = 'hello' + 5
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: can only concatenate str (not "int") to str
