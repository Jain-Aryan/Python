#Program to print your name
print("Aryan Jain")

#Write a program for a Single line comment and multi-line comments

#Single line comments
"""Multi
Line
Comments"""

#Define variables for different Data Types int, Boolean, char, float, double and print on the 
Console

a=5
print("Type=",type(a))
b=True
print("Type=",type(c))

var='a'
print("Type=",type(var))

c=2.3
print("Type=",type(c))

#Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a=2

def f1():
    print('Inside f1():',a)

def f2():
    a=6
    print('Inside f2():',a) 

def f3():
    global a
    a=9      
    print('Inside f3():',a)  

print('global:',a)
f1()
print('global:',a)
f2()
print('globa :',a)
f3()

