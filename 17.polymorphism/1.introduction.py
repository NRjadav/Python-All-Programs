
"""
polymorphism:
============

==> poly means many and morphism menas forms

==> one named method has different different forms its called polymorphism

==> there are 2 types of polymorphism

1 : method overloading :
    ====== ===========

    ==> one class can contain same name method with different signature(parameters)

    ==> note : in python this is not supported
        ====

2 : method overriding : 
    ====== ==========

    ==> two class have same name method with same parameters


"""

class nilesh():
    def jaydip(self):
        print("my name is jadav jaydip ramjibhai")

class mital(nilesh):
    def jaydip(self) :
        nilesh.jaydip(self)
        print("my name is jadav urvashi ramjibhai")

obj1=mital()               
obj1.jaydip()
