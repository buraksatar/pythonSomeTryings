import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # create the turtle brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    draw_square(brad)
    # create the turtle Angie - draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    draw_circle(angie)
    # create the Turtle Burak - draws a triangle
    burak = turtle.Turtle()
    burak.shape("arrow")
    burak.color("yellow")
    draw_triangle(burak)
    window.exitonclick()
    
def draw_square(brad):
    for i in range(1,5) :
        brad.forward(100)
        brad.right(90)       
    
def draw_circle(angie):      
    angie.circle(100)

def draw_triangle(burak):
    for i in range(1,4) : 
        burak.forward(100)
        burak.right(120)
        
    
draw_art()



