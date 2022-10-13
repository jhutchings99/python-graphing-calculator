from graphics import *
from stack import Stack
import math

def print_directions():
    print("Calculator Stuff...")

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
    while not s.isEmpty():
        postfix += s.pop()
    return postfix

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
    return s.pop()

def main():
    WIDTH = 800
    HEIGHT = 800
    print_directions()
    infix = input("Enter the function you want to graph. (ex: x*x): ")
    # infix is the operator between two numbers x + 3
    postfix = infix_to_postfix(infix)
    # postfix is the operator after two numbers x 3 +
    win = GraphWin("Graphing Calculator", WIDTH, HEIGHT )
    XLOW = -10
    XHIGH = 10
    YLOW = -10
    YHIGH = 10
    XINC = .1
    win.setCoords(XLOW, YLOW, XHIGH, YHIGH)
    x = XLOW

    Line(Point(XLOW, 0), Point(XHIGH, 0)).draw(win)
    Line(Point(0, YLOW), Point(0, YHIGH)).draw(win)

    for i in range(XLOW, XHIGH + 1):
        if i != 0:
            Line(Point(i, -.1), Point(i, .1)).draw(win)
            Text(Point(i, -.3), str(i)).draw(win)
    for i in range(YLOW, YHIGH + 1):
        if i != 0:
            Line(Point(-.1, i), Point(.1, i)).draw(win)
            Text(Point(-.3, i), str(i)).draw(win)

    while x <= XHIGH:
    # for x in range(XLOW, XHIGH, .1):
        # y = math.sin(x)
        y = evaluate_postfix(postfix, x)
        x2 = x + XINC
        y2 = evaluate_postfix(postfix, x2)
        line = Line(Point(x, y), Point(x2, y2))
        line.setWidth(2)
        line.setOutline("red")
        line.draw(win)
        #c = Circle(Point(x,y), .1)
        #c.draw(win)
        x += XINC
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()