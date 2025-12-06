import turtle
import random
import time
# we have IMPORTED THEM!!

rog = turtle.Turtle()
bog = turtle.Screen()

# now we do stuff hehe
rog.shape("square")
rog.color("green")
bog.bgcolor("black")
bog.title("idk bro i gyatt bored")
bog.tracer(0)
uhm = []
dog = 0.1

rog.penup()
rog.hmm = "stop"

# ok we make rog move now
def NONO():
    if rog.hmm == "up":
        y = rog.ycor()
        rog.sety(y + 20)
    elif rog.hmm == "down":
        y = rog.ycor()
        rog.sety(y - 20)
    elif rog.hmm == "left":
        x = rog.xcor()
        rog.setx(x - 20)
    elif rog.hmm == "right":
        x = rog.xcor()
        rog.setx(x + 20)

def go_up():
    if rog.hmm != "down":
        rog.hmm = "up"

def go_down():
    if rog.hmm != "up":
        rog.hmm = "down"

def go_left():
    if rog.hmm != "right":
        rog.hmm = "left"

def go_right():
    if rog.hmm != "left":
        rog.hmm = "right"

bog.listen()

bog.onkey(go_up, "w")
bog.onkey(go_up, "Up")
bog.onkey(go_down, "s")
bog.onkey(go_down, "Down")
bog.onkey(go_left, "a")
bog.onkey(go_left, "Left")
bog.onkey(go_right, "d")
bog.onkey(go_right, "Right")

# im hungry 
nom = turtle.Turtle()
nom.shape("circle")
nom.color("red")
nom.penup()
nom.speed(0)
nom.goto(random.randint(-290, 290), random.randint(-290, 290))

# yay scores
me = 0
you = 0

fog = turtle.Turtle()
fog.speed(0)
fog.shape("square")
fog.color("white")
fog.penup()
fog.hideturtle()
fog.goto(0, 260) 
fog.write(f"Score: {me}  High Score: {you}", align="center", font=("Courier", 24, "normal"))

# uh
try:
    with open("DONTTOUCHME.txt", "r") as f:
        you = int(f.read())
except FileNotFoundError:
    you = 0
    with open("DONTTOUCHME.txt", "w") as f:
        f.write("0")

while True:
    bog.update()
    # --- 1. WALL COLLISION CHECK ---
    if rog.xcor() > 290 or rog.xcor() < -290 or rog.ycor() > 290 or rog.ycor() < -290:
        time.sleep(1)
        rog.goto(0, 0)
        rog.hmm = "stop"
        for segment in uhm:
            segment.goto(1000, 1000)
        uhm.clear()
        dog = 0.1
        me = 0 
        fog.clear()
        fog.write(f"Score: {me}  High Score: {you}", align="center", font=("Courier", 24, "normal"))
    
    # --- 2. BODY TRAILING LOGIC ---
    for index in range(len(uhm) - 1, 0, -1):
        x = uhm[index - 1].xcor()
        y = uhm[index - 1].ycor()
        uhm[index].goto(x, y)
    if len(uhm) > 0:
        x = rog.xcor()
        y = rog.ycor()
        uhm[0].goto(x, y)
        
    NONO()
    
    # --- 3. BODY COLLISION CHECK ---
    for segment in uhm:
        if segment.distance(rog) < 20:
            time.sleep(1)
            rog.goto(0, 0)
            rog.hmm = "stop"
            for segment in uhm:
                segment.goto(1000, 1000)
            uhm.clear()
            dog = 0.1
            me = 0 
            fog.clear()
            fog.write(f"Score: {me}  High Score: {you}", align="center", font=("Courier", 24, "normal"))
            break

    # --- 4. FOOD COLLISION / GROWTH ---
    if rog.distance(nom) < 20:
        new_uhm = turtle.Turtle()
        new_uhm.speed(0)
        new_uhm.shape("square")
        new_uhm.color("#235E0A")
        new_uhm.penup()
        uhm.append(new_uhm)
        nom.goto(random.randint(-250, 250), random.randint(-250, 250))
        me += 10
        if me > you:
            you = me
            with open("DONTTOUCHME.txt", "w") as f:
                f.write(str(you))
        fog.clear()
        fog.write(f"Score: {me}  High Score: {you}", align="center", font=("Courier", 24, "normal"))
        dog *= 0.95
        if dog < 0.03:
            dog = 0.03

    time.sleep(dog)

# heyy original by irialovington on github lol, dont remove me pls i license
# you can mod thiss!! << fun fact, this was inspired by some random idea i had at 3 am
