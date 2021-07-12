#write a Python program which accepts the radius of a circle from the user and computes area
#1.
import math
radius = float(input("Input the radius of the circle : "))
area = math.pi * radius * radius
print("The area of the circle with radius ",radius," is",area)


#write a Python program to accept a filename from the user and print the extension of that
#2.
fname = input("Input the Filename: ")
file_extns= fname.split(".")
print("The extension of the file is :"+repr(file_extns[-1]))




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.............HAPPY CODING...........<<<<<<<<<<<<<<<<<<<<<<<<<<<
