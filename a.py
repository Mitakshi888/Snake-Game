import turtle
import time
import random

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#221a28")  # Soft, dim lofi night bedroom tone
screen.title("your safe space // chill & breathe")

# --- Turtle Setup ---
t = turtle.Turtle()
t.hideturtle()
t.speed(5)  # Calm, rhythmic drawing speed
t.pensize(2)  # Delicate pen stroke


# --- Cute & Lo-fi Helper Functions ---
def shaky_line(x1, y1, x2, y2, color, thick=2):
    """Draws a line with tiny imperfections to give it a cozy hand-drawn vibe."""
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.pensize(thick)

    steps = 6
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps

    for i in range(1, steps + 1):
        target_x = x1 + (dx * i) + random.uniform(-1.0, 1.0)
        target_y = y1 + (dy * i) + random.uniform(-1.0, 1.0)
        t.goto(target_x, target_y)
    t.pensize(2)


def draw_kawaii_eye(x, y):
    """Draws a sleepy, content kawaii closed blinking eye (n_n)."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#2a2033")  # Soft dark ink outline
    t.pensize(3)
    t.setheading(45)
    t.circle(8, 90)  # Curved happy blink eye
    t.setheading(0)
    t.pensize(2)


def draw_blush(x, y):
    """Draws a soft, warm pastel pink cheek blush."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#ffb3c1")
    t.begin_fill()
    t.circle(6)
    t.end_fill()


def draw_cute_bear_mug():
    """Draws a chubby kawaii mug with little round bear ears and a face."""
    outline = "#2a2033"

    # 1. Left Bear Ear Fill
    t.penup()
    t.goto(-40, 35)
    t.color("#a3c4bc")
    t.begin_fill()
    t.setheading(60)
    t.circle(12, 200)
    t.end_fill()

    # 2. Right Bear Ear Fill
    t.penup()
    t.goto(20, 42)
    t.begin_fill()
    t.setheading(20)
    t.circle(12, 200)
    t.end_fill()
    t.setheading(0)

    # 3. Fill the chubby mug body (Soft pastel sage green)
    t.penup()
    t.goto(-50, 40)
    t.color("#a3c4bc")
    t.begin_fill()
    t.goto(50, 40)
    t.goto(40, -40)
    t.setheading(-90)
    t.circle(-40, 180)
    t.goto(-50, 40)
    t.end_fill()
    t.setheading(0)

    # 4. Outlines for the ears
    t.penup()
    t.goto(-42, 36)
    t.pendown()
    t.color(outline)
    t.pensize(3)
    t.setheading(65)
    t.circle(12, 190)

    t.penup()
    t.goto(22, 41)
    t.pendown()
    t.setheading(25)
    t.circle(12, 190)
    t.pensize(2)
    t.setheading(0)

    # 5. Sketch the mug outlines
    shaky_line(-50, 40, 50, 40, outline, thick=3)
    shaky_line(50, 40, 40, -40, outline, thick=3)
    shaky_line(-40, -40, -50, 40, outline, thick=3)

    # Bottom curved outline
    t.penup()
    t.goto(40, -40)
    t.pendown()
    t.color(outline)
    t.pensize(3)
    t.setheading(-90)
    t.circle(-40, 180)
    t.pensize(2)
    t.setheading(0)

    # 6. Cute Mug Handle
    t.penup()
    t.goto(45, 20)
    t.pendown()
    t.color(outline)
    t.pensize(3)
    t.setheading(-30)
    t.circle(-20, 140)
    t.pensize(2)
    t.setheading(0)

    # 7. Add Kawaii Face features (u_u)
    draw_kawaii_eye(-22, 10)
    draw_kawaii_eye(10, 10)
    draw_blush(-28, -2)
    draw_blush(20, -2)

    # Small happy kitty/bear mouth (w)
    t.penup()
    t.goto(-3, 2)
    t.pendown()
    t.color(outline)
    t.pensize(2)
    t.setheading(-90)
    t.circle(3, 180)
    t.setheading(-90)
    t.circle(3, 180)
    t.setheading(0)


def draw_tiny_sparkle(x, y, color):
    """Draws a cute, soft 4-point doodle star."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    shaky_line(x - 6, y, x + 6, y, color, thick=2)
    shaky_line(x, y - 6, x, y + 6, color, thick=2)


def draw_heart_steam(x, y):
    """Draws warm, soft pastel pink heart bubbles floating upward."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#ffccd5")
    t.begin_fill()
    t.left(50)
    t.forward(12)
    t.circle(6, 200)
    t.right(140)
    t.circle(6, 200)
    t.forward(12)
    t.end_fill()
    t.setheading(0)


# --- Random Comforting Text Generator ---
# A pool of calming combinations so it is unique every time you run it
breathing_prompts = [
    "breathe in . . .",
    "take a soft breath . . .",
    "slow down your mind . . ."
]
grounding_prompts = [
    "you are safe here.",
    "unclench your jaw.",
    "drop your shoulders.",
    "it is okay to rest."
]
comfort_quotes = [
    "everything is going to be okay (u_u) //",
    "you did enough for today ( ᵕ_ᵕ ) //",
    "tomorrow is a brand new page (◌ˊᵕˋ◌) //",
    "you are doing just fine, one step at a time //"
]

selected_line1 = random.choice(breathing_prompts)
selected_line2 = random.choice(grounding_prompts)
selected_line3 = random.choice(comfort_quotes)

# --- Step-by-Step Aesthetic Sketch ---

# 1. Background Soft Pastel Glow
t.penup()
t.goto(-10, -50)
t.pendown()
t.color("#f9dbbd")  # Faded cozy peach moon glow
t.begin_fill()
t.circle(100)
t.end_fill()

# 2. Sketch the Kawaii Bear Mug
draw_cute_bear_mug()

# 3. Sketch Floating Heart Steam
draw_heart_steam(-22, 65)
draw_heart_steam(12, 85)

# 4. Add Cute Scattered Sparkles
draw_tiny_sparkle(-90, 120, "#fff3b0")
draw_tiny_sparkle(85, 140, "#fff3b0")
draw_tiny_sparkle(95, 30, "#ffccd5")

# 5. Dynamic Typewriter Typography
t.penup()
t.goto(0, -180)
t.color("#eee9f5")
t.write(selected_line1, font=("Courier", 18, "normal"), align="center")

time.sleep(2.5)

t.penup()
t.goto(0, -220)
t.color("#bdaec6")
t.write(selected_line2, font=("Courier", 16, "normal"), align="center")

time.sleep(2.0)

t.penup()
t.goto(0, -260)
t.color("#ffccd5")
t.write(selected_line3, font=("Courier", 14, "italic"), align="center")

# Keep window open
screen.mainloop()
