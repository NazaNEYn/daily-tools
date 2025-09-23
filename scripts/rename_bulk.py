import os
import datetime

def bulk_rename_files():
    """Rename all files in the specified directory with a custom or timestamped prefix."""
    # Prompt for folder path
    folder = input("Enter folder path (leave blank for current directory): ").strip()
    if not folder:
        folder = os.getcwd()  # Use current directory if blank

    # Validate folder
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid directory")
        return

    # Change to the specified directory
    os.chdir(folder)

    # Prompt for prefix
    prefix = input("Enter prefix (leave blank for timestamp): ").strip()
    if not prefix:
        prefix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Get list of files
    files = [f for f in os.listdir() if os.path.isfile(f)]
    if not files:
        print("No files found in the specified directory")
        return

    # Rename files
    count = 0
    for file in files:
        new_name = f"{prefix}_{file}"
        os.rename(file, new_name)
        count += 1

    print(f"Renamed {count} files with prefix '{prefix}' in '{folder}'")

if __name__ == "__main__":
    bulk_rename_files()
