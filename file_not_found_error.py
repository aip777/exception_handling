try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")  # Output: Error: [Errno 2] No such file or directory: 'non_existent_file.txt'
