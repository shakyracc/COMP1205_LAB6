# take 3 integers as inputs
# return whether integers are right triangle or not

# why is sort a friend? because sum of square of the two smaller sides must be equal the square of the largest side 

int1 = int(input("Enter a number: "))
int2 = int(input("Enter another number: "))
int3 = int(input("Enter one more number: "))

def isRightTriangle(int1, int2, int3):
    print("")

    sides = sorted([int1, int2, int3])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("These numbers are a right angle triangle")
        return True
    else:
        print("These numbers are NOT a right angle triangle")
        return False


isRightTriangle(int1, int2, int3)


