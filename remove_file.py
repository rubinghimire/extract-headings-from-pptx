import os


def delete_solution_js_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith("-solution.js"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except OSError as e:
                    print(f"Error deleting file: {file_path}, {e}")


# Specify the root directory where you want to search for and delete files
root_directory = 'C:/Users/lenovo/VSCodeProjects/js-challenges'

# Call the function to delete -solution.js files
delete_solution_js_files(root_directory)
