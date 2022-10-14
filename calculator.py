from graphics import *
from stack import Stack
import math

# Function that converts an infix expression to postfix
def infix_to_postfix(infix):
    postfix = ""
    s = Stack()
    for c in infix:
        if c in "0123456789x":
            postfix += c
        elif c in "*/":
            if not s.isEmpty() and s.top() in "*/":
                postfix += s.pop()
            s.push(c)
        elif c in "+-":
            while not s.isEmpty() and s.top() in "*/+-":
                postfix += s.pop()
            s.push(c)
        elif c == "^":
            s.push(c)
        elif c == "(":
            s.push(c)
        elif c == ")":
            while not s.isEmpty() and s.top() != "(":
                postfix += s.pop()
            s.pop()
        elif c == "s":
            s.push("sin")
        elif c == "c":
            s.push("cos")
        elif c == "t":
            s.push("tan")
        elif c == " ":
            continue
            
    while not s.isEmpty():
        postfix += s.pop()
    return postfix

# Function that evaluates a postfix expression
def evaluate_postfix(postfix, x):
    s = Stack()
    for c in postfix:
        if c in "0123456789":
            s.push(float(c))
        elif c == "x":
            s.push(x)
        elif c == "/":
            rhs = s.pop()
            lhs = s.pop()
            ans = lhs / rhs
            s.push(ans)
        elif c == "*":
            rhs = s.pop()
            lhs = s.pop()
            ans = lhs * rhs
            s.push(ans)
        elif c == "+":
            rhs = s.pop()
            lhs = s.pop()
            ans = lhs + rhs
            s.push(ans)
        elif c == "-":
            rhs = s.pop()
            lhs = s.pop()
            ans = lhs - rhs
            s.push(ans)
        elif c == "^":
            rhs = s.pop()
            lhs = s.pop()
            ans = lhs ** rhs
            s.push(ans)
        elif c == "s":
            rhs = s.pop()
            ans = math.sin(rhs)
            s.push(ans)
        elif c == "c":
            rhs = s.pop()
            ans = math.cos(rhs)
            s.push(ans)
        elif c == "t":
            rhs = s.pop()
            ans = math.tan(rhs)
            s.push(ans)
        elif c == " ":
            continue
    return s.pop()

def main():
    # Constants that control the size of the window and the X and Y ranges
    WIN_HEIGHT = 800
    WIN_WIDTH = 1200
    XLOW = -10
    XHIGH = 10
    YLOW = -10
    YHIGH = 10
    XINC = .1

    # Create the window
    win = GraphWin("Graphing Calculator", WIN_WIDTH, WIN_HEIGHT )
    win.setCoords(XLOW - 10, YLOW, XHIGH, YHIGH)

    # Draw X-Axis
    Line(Point(XLOW, 0), Point(XHIGH, 0)).draw(win)

    # Draw Y-Axis
    Line(Point(0, YLOW), Point(0, YHIGH)).draw(win)

    # Create grid lines
    for i in range(XLOW, XHIGH + 1):
        if i != 0:
            line = Line(Point(i, YLOW), Point(i, YHIGH))
            line.setOutline("lightgray")
            line.setWidth(1)
            line.draw(win)

    for i in range(YLOW, YHIGH + 1):
        if i != 0:
            line = Line(Point(XLOW, i), Point(XHIGH, i))
            line.setOutline("lightgray")
            line.setWidth(1)
            line.draw(win)

    # Label the x-axis from -10 to 10 exluding 0
    for i in range(XLOW, XHIGH + 1):
        if i != 0:
            Line(Point(i, -.1), Point(i, .1)).draw(win)
            Text(Point(i, -.3), str(i)).draw(win)
            
    # Label the y-axis from -10 to 10 exluding 0
    for i in range(YLOW, YHIGH + 1):
        if i != 0:
            Line(Point(-.1, i), Point(.1, i)).draw(win)
            Text(Point(-.3, i), str(i)).draw(win)

    # Create a gray rectangle on the left side of the window to hold inputs
    input_rect = Rectangle(Point(XLOW - 10, YLOW), Point(XLOW, YHIGH))
    input_rect.setFill("gray")
    input_rect.draw(win)

    # Title for the input section
    title_text = Text(Point(XLOW - 5, YHIGH - 1), "JEREMY'S GRAPHING CALCULATOR")
    title_text.setSize(15)
    title_text.setFace("arial")
    title_text.setTextColor("white")
    title_text.draw(win)

    # Create a quit button
    quit_button = Rectangle(Point(XLOW - 10, YLOW), Point(XLOW, YLOW + 1))
    quit_button.setFill("red")
    quit_button.draw(win)
    quit_text = Text(Point(XLOW - 5, YLOW + .5), "QUIT")
    quit_text.setTextColor("white")
    quit_text.draw(win)

    # Create a clear button to clear the graph
    clear_button = Rectangle(Point(XLOW - 10, YLOW + 1), Point(XLOW, YLOW + 2))
    clear_button.setFill("blue")
    clear_button.draw(win)
    clear_text = Text(Point(XLOW - 5, YLOW + 1.5), "CLEAR")
    clear_text.setTextColor("white")
    clear_text.draw(win)

    # Create text below the title to tell the user what to do
    directions_text = Text(Point(XLOW - 5, YHIGH - 4), 
    """Enter an equation in one of the boxes below
    and click the graph button to graph it.
    You can use the following functions:
    s (sin), c (cos), t (tan), ^ (exponent)
    + (addition), - (subtraction), * (multiplication),
     / (division), x (variable) and ( ) in your equation.
     Example 1: 2x^2 + 3x - 4
     Example 2: s(x) + c(x)
     Example 3: tx^4
     Example 4: x/2+sx""")
    directions_text.setSize(13)
    directions_text.setFace("arial")
    directions_text.setTextColor("white")
    directions_text.draw(win)

    # Create the first entry box
    entry_box1 = Entry(Point(XLOW - 5, YHIGH - 8), 30)
    entry_box1.setFill("white")
    entry_box1.draw(win)

    # Create the first graph button
    graph_button1 = Rectangle(Point(XLOW - 10, YHIGH - 9), Point(XLOW, YHIGH - 10))
    graph_button1.setFill("green")
    graph_button1.draw(win)
    graph_text1 = Text(Point(XLOW - 5, YHIGH - 9.5), "GRAPH FIRST EQUATION")
    graph_text1.setTextColor("white")
    graph_text1.draw(win)

    # Create the second entry box
    entry_box2 = Entry(Point(XLOW - 5, YHIGH - 12), 30)
    entry_box2.setFill("white")
    entry_box2.draw(win)

    # Create the second graph button
    graph_button2 = Rectangle(Point(XLOW - 10, YHIGH - 13), Point(XLOW, YHIGH - 14))
    graph_button2.setFill("green")
    graph_button2.draw(win)
    graph_text2 = Text(Point(XLOW - 5, YHIGH - 13.5), "GRAPH SECOND EQUATION")
    graph_text2.setTextColor("white")
    graph_text2.draw(win)

    # Button and graphing functionality
    while True:
        # Get the mouse click
        click = win.getMouse()

        # Graph the first equation if the first graph button is clicked and the entry box is not empty
        if click.getX() >= XLOW - 10 and click.getX() <= XLOW and click.getY() >= YHIGH - 10 and click.getY() <= YHIGH - 9 and entry_box1.getText() != "":
            equation = entry_box1.getText()
            postfix = infix_to_postfix(equation)
            x = XLOW
            while x <= XHIGH:
                y = evaluate_postfix(postfix, x)
                x2 = x + XINC
                y2 = evaluate_postfix(postfix, x2)
                line = Line(Point(x, y), Point(x2, y2))
                line.setWidth(2)
                line.setOutline("red")
                line.draw(win)
                x += XINC

        # Graph the second equation if the second graph button is clicked and the entry box is not empty
        if click.getX() >= XLOW - 10 and click.getX() <= XLOW and click.getY() >= YHIGH - 14 and click.getY() <= YHIGH - 13 and entry_box2.getText() != "":
            equation = entry_box2.getText()
            postfix = infix_to_postfix(equation)
            x = XLOW
            while x <= XHIGH:
                y = evaluate_postfix(postfix, x)
                x2 = x + XINC
                y2 = evaluate_postfix(postfix, x2)
                line = Line(Point(x, y), Point(x2, y2))
                line.setWidth(2)
                line.setOutline("blue")
                line.draw(win)
                x += XINC

        # Clear the graph if the clear button is clicked
        if click.getX() >= XLOW - 10 and click.getX() <= XLOW and click.getY() >= YLOW + 1 and click.getY() <= YLOW + 2:
            win.close()
            main()

        # Quit the program if the quit button is clicked
        if click.getX() >= XLOW - 10 and click.getX() <= XLOW and click.getY() >= YLOW and click.getY() <= YLOW + 1:
            win.close()
            break
        
if __name__ == "__main__":
    main()