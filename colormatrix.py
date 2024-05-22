from PIL import Image


def pretty_print(matrix):
    print("[")
    for line in matrix:
        print(line)
    print("]")


# Get color matrix of image
def get_matrix(image_path, quality_loss_factor=1):
    # Open image and get sequence of pixels
    im = Image.open(image_path)
    width, _ = im.size
    pixels = list(im.getdata())

    resulting_matrix = []
    line = []
    linecount = 0

    is_alpha = None
    for pixel in pixels:
        current_color = (pixel[0], pixel[1], pixel[2])
        if quality_loss_factor != 1:
            current_color = round_color(current_color, quality_loss_factor)

        # If we did not already check that the pixels have an alpha value, do it
        if is_alpha is None:
            is_alpha = len(pixel) == 4
        # If the image has transparency, check fully transparent pixels
        if is_alpha and pixel[3] == 0:
            line.append("void")
        else:
            line.append(current_color)

        linecount += 1
        if linecount == width:
            resulting_matrix.append(line)
            line = []
            linecount = 0

    return resulting_matrix


# Return unique colors in color matrix
#   Used to reduce the number of times we open the color picked menu
def get_unique_colors(matrix):
    unique_colors = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current_color = matrix[i][j]
            if current_color != "void" and current_color not in unique_colors:
                unique_colors.add(current_color)

    return unique_colors


def round_color(color, factor):
    return (
        (color[0] // factor) * factor,
        (color[1] // factor) * factor,
        (color[2] // factor) * factor,
    )


if __name__ == "__main__":
    matrix = get_matrix("images/diamond.png")
    pretty_print(matrix)
    print(get_unique_colors(matrix))
    color_to_round = (234, 7, 46)
    print(color_to_round)
    print(round_color(color_to_round, 20))
