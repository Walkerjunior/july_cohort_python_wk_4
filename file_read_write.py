# File Read & Write Challenge 🖋️ + Error Handling Lab 🧪

def read_and_modify_file():
    try:
        # Ask user for a filename
        filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Successfully created {new_filename} with modified content.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
