try:
    import non_existent_module
except ImportError as e:
    print(f"Error: {e}")  # Output: Error: No module named 'non_existent_module'
