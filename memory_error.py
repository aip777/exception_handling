try:
    large_list = [1] * (10**10)  # May raise MemoryError depending on system
except MemoryError as e:
    print(f"Error: {e}")
