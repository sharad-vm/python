import turtle

t = turtle.Turtle()
t.speed(14)

def square(t):
    
    for i in range(1,5):
      t.forward(90)
      t.left(90)
    
def flower(t):
    
    for c in range(1,37):
        square(t)
        t.right(10)
    
    t.right(90)
    t.forward (240)

flower(t)
