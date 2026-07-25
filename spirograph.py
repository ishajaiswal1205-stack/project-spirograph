import turtle # opens up python's basic drawing kit (called turtle)so we can draw lines on the screen 
import math #brings a calculator tool so python can understand circles and curves

# Screen setup
screen = turtle.Screen()#creates a fresh, blank pop up window for us to draw on
screen.bgcolor("black")#turns the background color of the window completely black
screen.setup(900, 900)#sets the window size to a square that is 900 pixels wide and 900 pixels tall
screen.title("HEAVY Spirograph 🌵")#puts the custom title at the very top of the window
screen.tracer(20)#boosts the drawing speed by hiding the lines until 20 of them are finished

t = turtle.Turtle()#spawns our drawing pen and name it t
t.speed(0)#tells our pen t to move at the absolute maximum speed 
t.width(1)#makes the drawing line thin exactly 1 pixel thick
t.hideturtle()#hides the pen pointer icon so that you can see the beautiful drawing, not the tool drawing it

colors = ["#FFD700", "#FFA500", "#FFFF00", "#FFCC00"]#makes a list of 4 different shades of gold and yellow to use for drawing

R = 220# these three lines set the math number that controls the shape, size and loops of our pattern
r = 65
d = 140

for layer in range(8):# tells python to repeat everything below it 8 times, creating 8 overlapping layers 
    t.color(colors[layer % len(colors)])#Switches the pen color to next golden shade in our list for each new layer
    
    t.penup()#lifts the pen off the screen so it can move without drawing a messy line
    t.goto(R - r + d, 0)#move the pen to the perfect starting spot on the right side of the screen 
    t.pendown()#puts the pen back down on the screen, ready to start drawing lines
    
    for i in range(3000): #tells the python to draw 3,000 tiny micro-lines per layer to make a smooth, curved shape
        angle = i * 0.03  #slightly changes the rotation angle every single micro line 
        x = (R - r) * math.cos(angle) + (d + layer * 5) * math.cos((R - r) / r * angle)#used a math formula to calculate the exact left and right position(X) for the nxt dot line
        y = (R - r) * math.sin(angle) - (d + layer * 5) * math.sin((R - r) / r * angle)#used a math formula to calculate the exact up and down position(y) for the nxt dot line
        t.goto(x, y) # moves the pen to that newly calculated (x,y)spot, leaving a tiny line behind it
        
    t.right(10) #tilts the pens starting angle by 10 degrees before starting the next layer so the shapes interlace beautifully

screen.update()#instantly displays any leftover lines on the screen
turtle.done() #keeps the window open when it finishes drawing so you can look at your final artwork
