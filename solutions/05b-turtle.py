# Bonus solution — turtle starburst

import turtle

t = turtle.Turtle()
t.speed(0)
t.pencolor("purple")

for i in range(36):
    t.forward(100)
    t.left(170)

turtle.done()

# Tweak: change 170 to 172, 120, 144... each angle makes a different
# star pattern. Change the color too.
