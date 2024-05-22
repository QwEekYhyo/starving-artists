def rgb_to_hex(rgb):
    # Store hex values of red, green and blue
    temp = ["", "", ""]
    for i in range(3):
        temp[i] = hex(rgb[i])[2:]

    # Concatenate the values and ensure they are of length two to match the
    # format : ff00ff
    result = ""
    for v in temp:
        if len(v) < 2:
            result += "0" + v
        elif len(v) == 2:
            result += v

    return result


if __name__ == "__main__":
    print(rgb_to_hex((255, 6, 27)))
