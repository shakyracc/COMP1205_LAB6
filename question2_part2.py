# define two input and check functions

import math

def is_nneg_float(s):

    # checks if string s denotes a non-negative floating point value (not in scientific notation)
    if s.count('.') > 1:
        return False
    
    if s.startswith('-'):
        return False
    
    if 'e' in s or 'E' in s:
        return False 
    
    # This function should return True if s contains (at most) one decimal point  one or more digits (and nothing else)
    if s.replace('.', '', 1).isdigit():
        return True
    
    return False

def get_nneg_float(p):
    #repeatedly prompt user using p until the user input a non-negative floating point value
    # return the non-negative float that was input (as float, not a string)
    # invoke the previous function to check the input string before converting to a float.

    while is_nneg_float(p) == False:
        p = input("Must be a float value. please try again.: ")
        is_nneg_float(p)
    
    print(float(p))
    return(float(p))


print("This program accepts radius and height inputs from the user and returns the surface area of the cone and the volume of the cone.")

def getDimensions():

    radius = get_nneg_float(input("Enter a non-negative float for Radius of the cone (##.##): "))

    height = get_nneg_float(input("Enter a non-negative float for Height of the cone (##.##): "))
    
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



