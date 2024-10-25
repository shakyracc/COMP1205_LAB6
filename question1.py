number = 50 
def func(number):
    print(number)
    number = 2
    print(number)
func(number)
print(number)

#   This code prints the variable "number". number is set to 50 on line 1. At line 6, number whose value is still 50 is pass to the function "func". func prints the number (50). It then sets number to 2 and prints number again (2). Once the function is complete the code moves on to line 7 which prints number again whose value at this point is 50. 
#   The final output is: 50, 2, 50
#   This code demonstrates the difference between local and global variables. 
#   A local variable is defined inside a function and is accessible only within the function where it's defined. The local variable only exists during the function's execution. 
#   A global variable is defined outside of all functions and is accessible throughout the enter program including within functions. It is stored in memory for the program. 
#   In this code the local variable "number" in the function "func" being the same name as the global variable "number" may confuse things. However, when a local variable has the same name as a global variable the local variable takes precedence inside the function. 