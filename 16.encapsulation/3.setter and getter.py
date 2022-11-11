"""
setter and getter

"""

class student:
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id    
    
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    
    def setsubject(self,subject):
        self.subject=subject
    def getsubject(self):
        return self.subject

obj=student()

obj.setid("1")
obj.setname("nilesh")
obj.setsubject("pyhton")

print(obj.getid())
print(obj.getname())
print(obj.getsubject())