#Write a program to print “Bright IT Career” ten times using for loop

for i in range(0,10):
    print('Bright IT Career')

# Write a python program to print 1 to 20 numbers using the while loop.

i=1
while(i<21):
    print(i)
    i+=1

#Program to equal operator and not equal operators

x=1
y=3
print(x==y) 
print(x!=y)

#Write a program to print the odd and even numbers.

Set=[5,8,6,1,7,2,3,12,21,33,78,52]
print(Set)
print('Even Numbers:')
for i in Set:
    if i%2==0:
        print(i)
print('Odd Numbers:')
for i in Set:
    if i%2!=0:
        print(i)

#Write a program to print largest number among three numbers.

x=5
y=4
z=2
if(x>y and x>z):
    print('Largest Number is:{0}'.format(x))
if(y>x and y>z):
    print('Largest Number is:{0}'.format(y))
if(z>x and z>y):
    print('Largest Number is:{0}'.format(z))

#Write a program to print even number between 10 and 20 using while loop

i=10
while(i<21):
    if i%2==0:
        print('Even Numbers =',i)
    i+=1


#Write a program to print 1 to 10 using the do-while loop statement.

a=1
while True:
    print(a)
    a+=1
    if(a>10):
        break
print()

#Write a program to find Armstrong number or not

num=int(input("Enter a number:"))
sum=0

temp=num
while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10

if num==sum:
   print(num,'is Armstrong')
else:
   print(num,'is not Armstrong')

#. Write a program to find the prime or not.



n=int(input('Enter a Number:'))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print('{0} is not prime number'.format(n))
            break
    else:
        print('{0} is a prime number'.format(n))

#. Write a program to palindrome or not

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print('The number is a palindrome')
else:
    print('The number is not palindrome')

#. Program to check whether a number is EVEN or ODD using switch

x=int(input('Enter a number to check for even or odd:'))
if x%2==0:
    print('{0} is Even Number'.format(x))
else:
    print('{0} is Odd Number'.format(x))



    
    



