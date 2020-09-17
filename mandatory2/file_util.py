def get_file_content(path, mode = "r"):
    try:
        file = open(path, mode)
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        file.close()
        print("File could not be read")
        return False

def write_file_content(path, content, mode = "w"):
    try:
        file = open(path, mode)
        file.write(content)
        file.close()
        return True
    except FileNotFoundError:
        file.close()
        print("File could not be created")
        return False

