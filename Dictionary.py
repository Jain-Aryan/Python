Dict=dict([(1,'Copenhagen'),(2,'Oslo'),(3,'Geneva'),(4,'Madrid'),(5,'Rome'),])
print('Dictionary:',Dict)

Dict[6]='Singapore'
print('Dictionary with new item:\n',Dict)

Dict[4]='Turin'
print('Dictionary Updated:',Dict)

del Dict[2]
print('Dictionary after Deleting:',Dict)
print('Accessing an element:',Dict[6])

Sports={1:'Football',2:'Tennis',3:{'Age':34,'Weight':80}}
print('Nested loop Dictionary',Sports)

print('Accessing element of nested loop Dictionary:',Sports[1])
