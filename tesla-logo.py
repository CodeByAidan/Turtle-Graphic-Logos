import turtle

t = turtle.Turtle()
t.speed(0)


class Tesla:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.getscreen().bgcolor("#FEFBF6")

    def teslaTop(self):
        t.color("#E82127")
        self.e(-160, 160)
        t.left(18)
        self.d(-500, 40)
        t.right(89.5)
        self.d(500, 39)
        t.end_fill()

        self.e(-155, 133)

    def d(self, arg0, arg1):
        t.circle(arg0, arg1)
        t.right(90)
        t.forward(17)

    def e(self, arg0, arg1):
        self.a(arg0, arg1)
        t.begin_fill()

    def letterT(self):
        self.b(90.5, -500, 38, 70)
        t.circle(-30, 80)
        t.left(90)
        t.circle(-20, -70)
        self.b(10, -300, -15, 93)
        t.forward(280)
        t.right(160)
        t.forward(280)
        t.left(80)
        t.circle(300, 15)
        t.circle(20, 70)
        t.left(80)
        t.circle(30, -80)
        t.end_fill()

    def b(self, arg0, arg1, arg2, arg3):
        t.right(arg0)
        t.circle(arg1, arg2)
        t.right(arg3)

    def whiteV(self):
        self.a(-20, 155)
        t.pencolor("black")
        t.color("#FEFBF6")
        t.begin_fill()
        t.left(30)
        t.forward(60)
        t.left(130)
        t.forward(65)
        t.end_fill()

    def tLetter2(self):
        t.pencolor("#E82127")
        self.a(-200, -180)
        t.right(66)

        t.pensize(15)
        t.forward(60)
        t.back(30)
        t.right(90)
        t.forward(70)

    def eLetter(self):
        self.a(-115, -180)
        t.left(90)
        t.forward(60)
        self.a(-115, -215)
        t.forward(60)
        self.a(-115, -250)
        t.forward(60)

    def a(self, arg0, arg1):
        t.penup()
        t.goto(arg0, arg1)
        t.pendown()

    def sLetter(self):
        t.penup()
        t.goto(-20, -180)
        t.pendown()
        t.forward(60)
        t.backward(60)
        t.right(90)
        t.forward(34)
        t.left(90)
        t.forward(60)
        t.right(90)
        t.forward(34)
        t.right(90)
        t.forward(60)

    def lLetter(self):
        t.penup()
        t.goto(70, -180)
        t.pendown()
        t.left(90)
        t.forward(70)
        t.left(90)
        t.forward(60)

    def aLetter(self):
        self.c(-180)
        t.forward(60)

        self.c(-250)
        t.left(90)
        t.forward(32.5)
        t.right(90)
        t.forward(60)
        t.right(90)
        t.forward(32.5)

    def c(self, arg0):
        t.penup()
        t.goto(155, arg0)
        t.pendown()

    def teslaLogo(self):
        self.teslaTop()
        self.letterT()
        self.whiteV()
        self.tLetter2()
        self.eLetter()
        self.sLetter()
        self.lLetter()
        self.aLetter()
        t.hideturtle()
        turtle.done()


tesla = Tesla()
tesla.teslaLogo()
