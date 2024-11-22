it = iter([1, 2, 3])

try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))  # This will raise StopIteration
except StopIteration as e:
    print(f"Error: {e}")  # Output: Error:
