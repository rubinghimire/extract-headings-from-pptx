import os


def delete_hints_line(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()

        # Find the line with "### Hints" and its index
        hints_index = None
        for i, line in enumerate(lines):
            if line.strip() == "### Hints":
                hints_index = i
                break

        # If "### Hints" line is found, delete it
        if hints_index is not None:
            del lines[hints_index]

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                delete_hints_line(file_path)


# Specify the root directory where README.md files are located
root_directory = 'C:/Users/lenovo/VSCodeProjects/js-challenges'

# Call the function to process the files
process_directory(root_directory)
