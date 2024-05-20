from PIL import Image

def pretty_print(matrix):
    print("[")
    for line in matrix:
        print(line)
    print("]")

def get_matrix(image_path):
    im = Image.open(image_path)
    width, _ = im.size
    pixels = list(im.getdata())

    resulting_matrix = []
    line = []
    linecount = 0

    for i in pixels:
        k = (i[0], i[1], i[2])
        if (i[3] == 0):
            line.append("void")
        else:
            line.append(k)
        linecount += 1
        if linecount == width:
            resulting_matrix.append(line)
            line=[]
            linecount = 0

    return resulting_matrix

if __name__ == "__main__":
    pretty_print(get_matrix("images/diamond.png"))
