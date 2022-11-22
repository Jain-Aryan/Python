#Write a function to add integer values of an array

arr=[2,4,9,5,6]
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
print('Sum of Arrays=',sum)

#Write a function to calculate the average value of an array of integers

def average(num):
    sum=0
    for i in num:
        sum+=i
    avg=sum/len(num)
    return avg
print('Average of Array Elements=',average([2,4,9,5,6]))

#Write a program to find the index of an array element

arr=[1,4,8,9,6,3,11,2,7,8]
index=arr.index(4)
print('Index of 4=',index)

#Write a function to test if array contains a specific value


arr=[14,15,5,23,30]
for num in arr:
    if num==5:
        print("Array Element Exists")
 

#Write a function to remove a specific element from an array
print('Removing Element from Array')
arr=[1,4,8,9,6,3,11,2,7,8]
print(arr)
arr.remove(3)
print('\n Array after removal:')
print(arr)


#Write a function to copy an array to another array

print('Copy Array')
arr1=[1,2,3,4,5]
arr2=[]
arr2=arr1.copy()
print(arr2)

# Write a function to insert an element at a specific position in the array


print('Inserting Element:')
arr=[1,2,3,4,5,6]
arr.insert(0,7)

#Write a function to find the minimum and maximum value of an array

arr=[1,4,8,9,6,3,11,2,7,8]
minpos=arr.index(min(arr))
print('Minimun Array Element at Posistion:',minpos)
maxpos=arr.index(max(arr))
print('Maximum Array Element at Posistion:',maxpos)

#Write a function to reverse an array of integer values

arr=[5,8,7,4,9,6]
print(arr)
print('\nArray after reverse:')
arr.reverse()
print(arr)

#Write a function to find the duplicate values of an array

print('Duplicate Array Element')
arr=[5,8,7,4,9,6,4]
print(arr)
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print('Duplicate Array Element=',arr[j])

#Write a program to find the common values between two arrays

print('Common Elements')
arr1=[1,2,3,4,5,6]
arr2=[4,8,9,5,2,3]
print(arr1,arr2)
print('Common Elements=',set(arr1).intersection(arr2))

# Write a method to remove duplicate elements from an array

arr1=[1,2,5,4,8,4,2,5]
arr2=[] 
for i in arr1:
    if i not in arr2:
        arr2.append(i)
print(arr2)

#Write a method to find the second largest number in an array

arr=[1,5,6,4,2,3]
arr.sort()
print(arr)
print('Second Largest Number is:',arr[-2])

#Write a method to find number of even number and odd numbers in an array

arr=[1,2,3,4,5,6,7,8,9]
print(arr)
even=0
odd=0
for i in range(0,len(arr)):
    if arr[i]%2==0:
        even+=1

    else:
        odd+=1
print('No of Odd Array Elements=',odd)
print('No of Even Array Elements=',even)

#Write a function to get the difference of largest and smallest value


arr=[1,5,6,4,2,3]
arr.sort()
print(arr)
print('Difference=',arr[5]-arr[0])

#Write a method to verify if the array contains two specified elements(12,23)

arr=[12,47,64,23,88,98]
print(arr_
for i in arr:
    if i==12:
        print('Array Contains the given Element 12')
    elif i==23:
        print('Array Contains the given Element 23')


