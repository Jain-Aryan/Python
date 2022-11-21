#Write a function for arithmetic operators(+,-,*,/)

n1=input('Enter first number:')
n2=input('Enter second number:')

add=float(n1)+float(n2)

sub=float(n1)-float(n2)

mul=float(n1)*float(n2)

div=float(n1)/float(n2)


print('Addition of {0} and {1}={2}'.format(n1,n2,add))
print('Addition of {0} and {1}={2}'.format(n1,n2,sub))
print('Addition of {0} and {1}={2}'.format(n1,n2,mul))
print('Addition of {0} and {1}={2}'.format(n1,n2,div))


#Write a method for increment and decrement operators(++, --)

a=1
a+=1
a+=1
print('Value of a=',a)

for i in range(1,5):
    print(i)
for i in range(5,-1,-1):
    print (i)

#Write a program to find the two numbers equal or not

n1=input('Enter first number:')
n2=input('Enter second number:')

if n1==n2:
    print('Two Numbers are Equal')

else:
    print('Two Numbers are not Equal')


#. Program for relational operators (<,<==, >, >==)


n1=input('Enter first number:')
n2=input('Enter second number:')

print(n1<n2)
print(n1<=n2)
print(n1>n2)
print(n1>=n2)


#Print the smaller and larger number

n1=input('Enter first number:')
n2=input('Enter second number:')

if n1<n2:
    print('Larger Number is:{0}'.format(n2))
    print('Smaller Number is:{0}'.format(n1))
if n1>n2:
     print('Larger Number is:{0}'.format(n1))
     print('Smaller Number is:{0}'.format(n2))
    


