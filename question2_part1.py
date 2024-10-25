# Promp user for radius and height of a 3d code in a function 
# calculate and print the surface area in a function
# calculate and print the volume in a function 


# a. print a message indicating what the program does
# b. prompt the user for the radius in feet. a non-negative float
# c. prompt the user for the height in feet. a non negative float
# print the radius and height. round to 2 decimal places
# print the surface area and volume. round to 2 decimal places 

import math

print("This program accepts radius and height inputs from the user and returns the surface area of the cone and the volume of the cone.")

def getDimensions():

        radius = float(input("Insert the radius of the 3 dimensional cone in feet: "))
        height = float(input("Enter the height of the 3d cone in feet: "))
        return radius, height

radius, height = getDimensions()

print(f"Radius = {radius} ft, Height = {height} ft")

def cone_surface_area(r,h):
    # r is radius of base
    # l is slant height if cone
    # h is perpendicular height of cone
    # pythagoras theorem says l^2 = h^2 + r^2
    # l = math.sqrt(h**2 + r**2)
    print(r, h)
    l = math.sqrt(r**2 + h**2)

    # surface area of cone = ( pi * r * l ) + (*pi * r**2)
    SA = (math.pi * r * l) + (math.pi * r**2)
    print(f"Surface area of the cone = {round(SA, 2)} ft")
    
def cone_volume(r,h):
    # volume of a cone = (1/3) * math.pi * r**2 * h
    V = (1/3) * math.pi * r**2 * h
    print(f"Volume of the cone = {round(V, 2)} ft")

cone_surface_area(radius,height)
cone_volume(radius, height)

