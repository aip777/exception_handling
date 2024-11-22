try:
    print(undeclared_variable)
except NameError as e:
    print(f"Error: {e}")  # Output: Error: name 'undeclared_variable' is not defined
