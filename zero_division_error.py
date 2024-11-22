try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: division by zero
