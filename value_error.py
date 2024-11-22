try:
    number = int('not_a_number')
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: invalid literal for int() with base 10: 'not_a_number'
