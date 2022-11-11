
from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def display(self):
        print("hello")

class SBI(RBI):
    def display(self):
        print("SBI CLASS")
        # return super().display()

class HDFC(RBI):
    def display(self):
        print("HDFC CLASS")

sbi=SBI()
hdfc=HDFC() 

sbi.display()
hdfc.display()
sbi.display()











