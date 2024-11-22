try:
    with open('/restricted_file.txt', 'w') as file:
        file.write('Test')
except PermissionError as e:
    print(f"Error: {e}")  # Output: Error: [Errno 13] Permission denied: '/restricted_file.txt'
