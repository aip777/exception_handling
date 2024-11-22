import sys
print(sys.getrecursionlimit())

def recurse():
    return recurse()  # Infinite recursion

try:
    recurse()
except RecursionError as e:
    print(f"Error: {e}")  # Output: Error: maximum recursion depth exceeded
