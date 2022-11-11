
"""
multi-level inheritance:

      A
      |
      V
      B
      |
      V
      C

"""

# class A:
#     def displayA(self):
#         print("A Class")

# class B(A):
#     def displayB(self):
#         print("B Class")

# class C(B):
#     def displayC(self):
#         print("C Class")        
   
# obj=C()

# obj.displayA()
# obj.displayB()
# obj.displayC()


class A:
    def displayA(self):
        self.num=10

class B(A):
    def displayB(self):
        self.num1=20

class C(B):
    def displayC(self):
        # self.a=self.num+self.num1
        print("DONE")

obj=C()

b=obj.num+obj.num1
print(obj.b)
obj.displayC()








