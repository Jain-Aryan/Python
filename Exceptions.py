x=[1,2,3,4,5,6,7,8,9]
try:
    print('Largest Element in Array=',max(x))
except:
    print('No Elements in Array')

    
class A():
    a=1
    b=2
    c=5
    d=8
   
    print('Maximum of 1,2,5,8 is:',max(a,b,c,d))
   
    
def fun(y,z):
    try:
        m=((y+z)/(y-z))
    except ZeroDivisionError:
        print('y*z gives zero...EXCEPTION!')
    else:
        print(m)

fun(1,1)

try:
    file=open('PYQ.txt','r')
    print(data)
    print()
except:
    print('File does not exist....EXCEPTION')
finally:
    print('Move to the next task')

op=int(input('Enter a valid number:'))

        
try:
    if op==1:
        print('Valid Operator')
    else:
        print('Invalid Operator')
except:
    print('Exception Occurred')
finally:
    print('Bravo!')
            
        
        
           

       

        
        
    
  

    
    

