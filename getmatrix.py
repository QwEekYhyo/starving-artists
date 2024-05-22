from PIL import Image

def pretty_print(matrix):
    print("[")
    for line in matrix:
        print(line)
    print("]")

# Get color matrix of image
def get_matrix(image_path):
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
            line=[]
            linecount = 0

    return resulting_matrix

if __name__ == "__main__":
    pretty_print(get_matrix("images/diamond.png"))
