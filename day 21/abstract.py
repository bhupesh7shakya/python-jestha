from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
    def run(self,name):
        print(f"{self.process(name)}")
        
        
class Mobile(Computer):
    def process(self,name):
        return f"Mobile is running {name}"

class Laptop(Computer):
    def process(self,name):
        return f"Laptop is running {name}"




laptop=Laptop()
laptop.run("pubg")
# laptop.process()



