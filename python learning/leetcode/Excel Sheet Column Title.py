def convert_to_title(column_number: int) -> str:
    result = []
    while column_number > 0:
        column_number -= 1
        result.append(chr(column_number % 26 + ord('A')))
        column_number //= 26
    return "".join(reversed(result))
