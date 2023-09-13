def filter_string(value):
    result = ""
    for char in value:
        if char.isdigit():
            result += char
    return int(result)