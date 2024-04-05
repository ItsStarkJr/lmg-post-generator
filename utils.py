import json
import string


def strip_casefold(data):
    """Returns data stripped and lower case."""
    return data.strip().casefold()


def check_string_is_empty(data):
    """Checks if data consists of only whitespace characters."""
    if data.translate({ord(c): None for c in string.whitespace}) == "":
        return True


def create_text_file(data, filename):
    try:
        with open(f"post_files/{filename}.txt", "x") as file:
            file.write(data)
            print(f"Saved {filename}.txt to save files.")
    except:
        print("File already exists.")


def write_to_json_file(data, filename):
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
            print(f"Saved to {filename}")
    except:
        print("Something went wrong.")


def create_file_name(title) -> str:
    file_name = "".join(letter for letter in title if letter.isalnum())
    return file_name


# def open_json_file(filename):
#     try:
#         with open(filename, "r") as file:
#             file_content = json.load(file)
#             print(f"\n{filename} loaded.\n")
#         return file_content
#     except:
#         print("Something went wrong.")
