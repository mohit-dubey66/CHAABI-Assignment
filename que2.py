def get_file_type(extension_type_string, filenames):
    """
    Returns a dictionary with filename: type pairs based on the file extensions.

    Args:
        extension_type_string (str): String of extension and type values in the format "extension1,type1;extension2,type2;extension3,type3".
        filenames (list): List of filenames.

    Returns:
        dict: Dictionary with filename: type pairs.
    """
    extension_type_pairs = extension_type_string.split(";")
    extension_type_dict = {}
    for pair in extension_type_pairs:
        extension, file_type = pair.split(",")
        extension_type_dict[extension] = file_type

    file_type_dict = {}
    for filename in filenames:
        extension = filename.split(".")[-1]
        file_type = extension_type_dict.get(extension, "unknown")
        file_type_dict[filename] = file_type

    return file_type_dict


# Example usage
extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result = get_file_type(extension_type_string, filenames)
print(result)
