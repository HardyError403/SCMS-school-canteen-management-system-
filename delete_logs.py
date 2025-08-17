import os

def delete_log_files():
    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Loop through all files in the directory
    for filename in os.listdir(current_dir):
        if filename.endswith(".log"):
            file_path = os.path.join(current_dir, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    delete_log_files()
