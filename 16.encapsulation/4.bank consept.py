
class robot():
    def __init__(self):
        self.a=123
        self._b=123
        self.__c=123
    def display(self):
        print(self.__c)    

# class robot1(robot):
#     def __int__(self):
#         self.a

obj=robot()
# print(obj.a)
# print(obj._b)
# print(obj.__c)

obj.display()
