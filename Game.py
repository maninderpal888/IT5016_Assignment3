import random
import turtle

def isInScreen(win, turt):
    leftBound = -win.window_width() / 2
    rightBound = win.window_width() / 2
    topBound = win.window_height() / 2
    bottomBound = -win.window_height() / 2

    turtleX = turt.xcor()
    turtleY = turt.ycor()

    stillIn = True

    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

def samePosition(turtle1, turtle2):
    return turtle1.pos() != turtle2.pos()

def main():
    wn = turtle.Screen()
    wn.setup(width=800, height=600)

    red = turtle.Turtle()
    red.pencolor("red")
    red.pensize(5)
    red.shape('turtle')
    
    blue = turtle.Turtle()
    blue.pencolor("blue")
    blue.pensize(5)
    blue.shape('turtle')
    blue.hideturtle()
    blue.penup()
    blue.goto(red.pos()[0] + 50, red.pos()[1])
    blue.showturtle()
    blue.pendown()

    while isInScreen(wn, red) and isInScreen(wn, blue) and samePosition(red, blue):
        coinRed = random.randrange(0, 2)
        angleRed = 90

        if coinRed == 0:
            red.left(angleRed)
        else:
            red.right(angleRed)

        coinBlue = random.randrange(0, 2)
        angleBlue = 90

        if coinBlue == 0:
            blue.left(angleBlue)
        else:
            blue.right(angleBlue)

        red.forward(50)
        blue.forward(50)

    red.pencolor("black")
    blue.pencolor("black")

    if isInScreen(wn, red) and not isInScreen(wn, blue):
        red.write("Red Won", True, align="center", font=("Arial", 15, "bold"))
    elif isInScreen(wn, blue) and not isInScreen(wn, red):
        blue.write("Blue Won", True, align="center", font=("Arial", 15, "bold"))
    else:
        red.write("Draw", True, align="center", font=("Arial", 15, "bold"))
        blue.write("Draw", True, align="center", font=("Arial", 15, "bold"))

    wn.exitonclick()

if __name__ == "__main__":
    main()
