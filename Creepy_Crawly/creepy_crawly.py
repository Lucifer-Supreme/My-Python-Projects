import os
import shutil

def search_and_copy(keywords, search_directory, destination_folder):
    try:
        print(f"Searching for files containing any of these keywords: {keywords} in '{search_directory}'...")

        # Convert keywords to lowercase for case-insensitive comparison
        keywords_lower = [keyword.lower() for keyword in keywords]

        # Create destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Destination folder '{destination_folder}' created.")

        found_files = []

        # Traverse the directory tree
        for root, dirs, files in os.walk(search_directory):
            for file in files:
                # Check if any keyword matches the file name (case-insensitive)
                if any(keyword in file.lower() for keyword in keywords_lower):
                    source_file = os.path.join(root, file)
                    destination_path = os.path.join(destination_folder, file)

                    # Copy the file
                    shutil.copy(source_file, destination_path)
                    found_files.append(file)
                    print(f"Copied: {file}")

        if found_files:
            print("\nSearch Complete. The following files were copied:")
            for f in found_files:
                print(f"- {f}")
        else:
            print("No files matching the keywords were found.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Get user input for the list of keywords, search directory, and destination folder
#keywords_input = input("Enter keywords to search for, separated by commas (e.g., important, hidden): ")
keywords = ["important","hidden"]

destination = "Copied"

# Assuming the search directory is the C drive
search_directory = "C:\\"

search_and_copy(keywords, search_directory, destination)
