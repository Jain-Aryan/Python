#Access through class
class Static:
    staticvar=3
    print('Access through class')
print(Static.staticvar)

#Access through instance

instance=Static()
print('Access through instance')
print(Static.staticvar)

#Change within instance
instance.staticvar=4
print('Change within instance')
print(instance.staticvar)
print(Static.staticvar)

#Change within the class

Static.staticvar=5
print('Change within class')
print(Static.staticvar)
