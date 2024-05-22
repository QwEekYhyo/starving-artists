import utils, colormatrix
import turtle


def square(length, x, y, color, t):
    t.up()
    t.goto(x, y)
    t.down()
    t.color(color)
    t.seth(0)
    t.begin_fill()
    for _ in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()

def draw_texture(matrix, x, y, size, t):
    squaresize = size // len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "void":
                square(squaresize, x + j*squaresize, y - i*squaresize, matrix[i][j], t)

def main(image_path):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    screen.tracer(0)
    screen.colormode(255)
    texture = colormatrix.get_matrix(image_path)
    draw_texture(texture, -400, 400, 400, t)
    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    time_taken = utils.time_function(lambda
                                     : main("images/diamond.png"))
    print(f"Execution took {time_taken} seconds")
