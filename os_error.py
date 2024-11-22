import os

try:
    os.remove('non_existent_file.txt')
except OSError as e:
    print(f"Error: {e}")  # Output: Error: [Errno 2] No such file or directory: 'non_existent_file.txt'
