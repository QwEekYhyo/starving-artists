import time

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

def time_function(function):
    start = time.time()
    function()
    return time.time() - start

def time_format(seconds):
    minutes = seconds // 60
    seconds = seconds % 60

    hours = minutes // 60
    minutes = minutes % 60

    result = ""
    if hours > 0:
        result += f"{hours}h "
    if minutes > 0:
        result += f"{minutes}min "
    result += f"{seconds}s"
    return result

if __name__ == "__main__":
    print(rgb_to_hex((255, 6, 27)))
    print(time_format(7969))
