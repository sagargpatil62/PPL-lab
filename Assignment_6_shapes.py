import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.width(5)


class shape:
    def __init__(self, sides = 0, length = 0) :
        self.sides = sides
        self.length = length


class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")
        
class square(polygon):
    def show(self):
        for i in range(4):
            t.fd(self.length)
            t.rt(90)
        
    

class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 

class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)

class octagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(45)

class triangle(polygon):
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)

class circle(shape):
    def show(self):
        t.circle(self.radius)

class circle:
    def __init__(self, radius = 0) :
        self.radius = radius

class circle(circle):
    def show(self):
        t.circle(self.radius)




t.begin_fill()
t.fillcolor("yellow")
c1 = circle(100)
c1.show()
t.end_fill()

t.right(90)
t.forward(5)

t.color("white")
t.forward(100)
t.color("green")

hex1 = hexagon(6, 100)
hex1.info()
hex1.show()

t.left(90)
t.forward(5)

t.color("white")
t.forward(105)
t.color("red")

sq1 = square(4, 200)
sq1.info()
sq1.show()
t.hide()
