import turtle
import time
import random
Name= turtle.textinput("Name", "What is you name?")   
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person(Name)
print("Great job, "+p1.name)
 
#declaring variables
wn = turtle.Screen()
head = turtle.Turtle()
food = turtle.Turtle()
pen = turtle.Turtle()

# Create window screen using Turtle
def create_window():
    wn.title("Snake Game")  #window name
    wn.bgcolor("white")   #background screen
    wn.setup(width=550, height=550)   #window size
    wn.tracer(0)

# Create head of snake
def create_head():
    head.shape("circle")
    head.color("green")   #color of head
    head.penup()            #penup- does not leave tracks  
    head.goto(0, 0)         #starting point of head      
    head.direction = "Stop" #initial state
 
# Create food 
def create_food():
    colors = random.choice(['yellow','red', 'blue','purple', 'black'])  #options for colors
    shapes = random.choice(['triangle', 'square'])                    #options for shape of food
    food.speed(0)     #how fast food pops up
    food.shape(shapes) 
    food.color(colors)
    food.penup()    #does not leave tracks
    food.goto(0, 50)  #starting point of food
     
#Create title on screen
def create_title():  
    pen.speed(5) 
    pen.shape("circle")
    pen.color("blue")      #title color
    pen.penup()            #does not leave marks
    pen.hideturtle()       #make pen invisible
    pen.goto(0, 150)       #coordinates of title
    pen.write("Current Score : 0 ", align="center", font=("Arial", 25, "normal"))
 
#directions
def goup():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = "down"
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
def goright():
    if head.direction != "left":
        head.direction = "right"

#how many pixels the head moves after each key
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if (head.direction != "up" and head.direction !="down" and head.direction != "left" 
       and head.direction != "right" and head.direction != "Stop" and head.direction != "stop"):
        raise Exception("No other direction allowed") 
    #exception for any unexpected direction
         
wn.listen()
wn.onkeypress(goup, "w")    #binds goup to key "w"
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
 
segments = []

def body():
    score=0       #default settings
    delay=0.15
    while True:
        wn.update()
        colors = random.choice(['yellow','red', 'blue','purple', 'black'])
       #if you reach the boundaries, then end game
        if head.xcor() > 270 or head.xcor() < -270 or head.ycor() > 270 or head.ycor() < -270:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'yellow','purple','black'])
            shapes = random.choice(['square', 'triangle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()      #body of snake resets
            score = 0             #resets default values
            delay = 0.15
            pen.clear()
            pen.write("Current Score : {}  ".format(score), 
                      align="center", font=("Arial", 25, "normal"))
       # How close the head needs to be in order for new food to pop up
        if head.distance(food) < 25:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            food.goto(x, y)
 
           # Increase length of snake's body
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color(colors)  # random choice of colors from above
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 1
            pen.clear()
            pen.write("Current Score : {} ".format(score), 
                      align="center", font=("Arial", 25, "normal"))
    # Checks if snake bumps into itself
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()
             #resets to default settings 
                score = 0
                delay = 0.15
                pen.clear()
                pen.write("Current Score : {}  ".format(score), 
                          align="center", font=("Arial", 25, "normal"))
        time.sleep(delay)


def main():
    create_window()
    create_head()
    create_food()
    create_title()
    body()
    
if __name__ == "__main__":
    main()
    
wn.mainloop()



