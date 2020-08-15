import math
# use this for getting input from user
#radius = int((input("Input diameter of sphere : ")))/2
# default value of radius below
diameter = 12
radius = diameter/2
volume = (4/3)*math.pi*radius**3
print("Answer rounded off to closest two decimal places: \n")
print("\tVolume of sphere is {:.2f} \n".format(volume))
