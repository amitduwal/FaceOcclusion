import pickle

# Specify the path to your pickle file
pickle_file_path = 'path/to/your/pickle/file.pkl'

try:
    # Open the pickle file in read mode
    with open(pickle_file_path, 'rb') as pickle_file:
        # Load the data from the pickle file
        loaded_data = pickle.load(pickle_file)
        print(f"Data loaded from the pickle file: {loaded_data}")
except FileNotFoundError:
    print(f"Error: The specified pickle file '{pickle_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred while reading the pickle file: {e}")
