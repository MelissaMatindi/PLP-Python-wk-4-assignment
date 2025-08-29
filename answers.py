# The program first prompts the user for an input file name.
# It then attempts to read the content of that file, modify it,
# and write the modified content to a new output file specified by the user.
# Comprehensive error handling is included to manage common issues.

import os

def process_file_with_error_handling():
    """
    Reads content from a user-specified file, modifies it, and writes
    the new content to another user-specified file.

    Handles FileNotFoundError and other potential I/O errors gracefully.
    """
    input_filename = input("Enter the name of the file to read from: ")

    try:
        # Step 1: Read the content from the input file
        # The 'with' statement ensures the file is automatically closed.
        print(f"\nAttempting to read '{input_filename}'...")
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            original_content = input_file.read()
        print("File read successfully!")

        # Step 2: Modify the content
        # For this example, we'll convert the text to uppercase.
        modified_content = original_content.upper()
        print("Content modified (converted to uppercase).")

        # Step 3: Ask for the output filename and write the modified content
        output_filename = input(
            "\nEnter the name for the new output file "
            "(e.g., 'output.txt'): "
        )
        print(f"Attempting to write to '{output_filename}'...")
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)
        
        print("\nSuccess! The modified content has been written to "
              f"'{output_filename}'.")

    # Step 4: Handle potential errors
    except FileNotFoundError:
        # This block runs if the input file does not exist.
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please check the file path and try again.")
    except Exception as e:
        # This is a generic exception handler for other potential issues, such as permission errors when writing the output file.
        print(f"\nAn unexpected error occurred: {e}")
        print("Please ensure you have permission to read/write files.")

# To run the program, call the main function.
if __name__ == "__main__":
    process_file_with_error_handling()
