#Different ways creating a string

str='Portugal'
print(str)
str="will"
print(str)
str='''win the'''
print(str)
str="""World Cup"""
print(str)

#. Concatenating two strings using + operator

str1='Aryan'
str2=' Jain'
str=str1+str2
print('Concatenation of String:',str)

#Finding the length of the string

str='Manchester United'
print(str)
print('Length of string=',len(str))

#Extract a string using Substring

str1='Cristian'
str2='st'
print('Position of st=',str1.index(str2))

#Searching in strings using index()

str='Cristiano Ronaldo'
print('Searching Ronaldo....Found at:',str.index('Ronaldo'))

#Matching a String Against a Regular Expression With matches()
import re
str='India'
pattern='Ind'
match=re.match(pattern,str)
if match:
   print('Regular Expression matches:',match.group())
else:
   print('Pattern Not Found')

#Comparing strings

str1='Madeira'
str2='Manchester'
str3='Madrid'
str4='Turin'
print(str1==str2)
print(str3==str4)
print(str1!=str4)
print(str2!=str3)

#startsWith(), endsWith() and compareTo()

str='Wayne Rooney'
print(str.startswith('W'))
print(str.endswith('y'))
print()

#Trimming strings with strip()

str='Real Madrid'
print(str.strip('id'))

#Replacing characters in strings with replace()

str='El Classico'
print(str)
print('After Replacing:')
print(str.replace('El','The'))

#Splitting strings with split()

str='Manchester Derby'
print(str)
print('After Splitting:')
print(str.split('-'))

#Converting integer objects to Strings

n=3
print('Type before Conversion:',type(n))
c_n="%s"%n
print('Type after Conversion:',type(c_n))

#Converting to uppercase and lowercase

str='lower'
print(str.upper())







