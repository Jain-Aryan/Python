class A():
    def display(dp):
        print('This is class A')
    def show(self):
        print('Class A Method')


class B(A):
    def display1(d):
        print('This is class B')
    def show(self):
        print('Class B Method')


class C(B):
    def display2(dpp):
        print('This is class C')
    def show(self):
        print('Class C Method')


a=A()
a.display()
b=B()
b.display1()
c=C()
c.display2()
        
