# cball1.py
from math import pi, sin, cos, radians
def main():
    angle = eval(input("Enter the launch angle (in degrees):"))
    vel = eval(input("Enter the initial velocity (in meters/sec):"))
    time = eval(input("Enter time interval between calculations:"))
    theta = radians(angle)     # convert angle to radians
    xpos = 0                   # the initial position
    ypos = 0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    while ypos >= 0:           # loop until the ball hits the ground
        # update position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1
        print("(xpos,ypos): ({},{})".format(xpos, ypos))
main()
