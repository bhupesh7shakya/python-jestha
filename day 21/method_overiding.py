class GrandFather:
    def __init__(self):
        print("Parent constructor")
    def house(self):
        print("House")
        
        
class Father(GrandFather):
    def __init__(self):
        super().__init__()
        print("Child constructor")
    def car(self):
        print("Car")
    
    def house(self):
        super().house()
        print("another House")
        
        
father=Father()
father.house()