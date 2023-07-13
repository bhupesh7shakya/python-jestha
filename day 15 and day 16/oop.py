# a =10

# print(type(a))

# a = 1.1
# print(type(a))

class Person: #classname define
   name=None
   age=None
   gender=None
   
   # def __init__(self):
   #    pass
   
   def setName(self,name):
      self.name=name
      
   def getName(self):
      print(self.name)
      
   def setAge(self,age):
      self.age=age
      
   def getAge(self):
      print(self.age)
      
   def setGender(self,gender):
      self.gender=gender
      
   def getGender(self):
      print(self.gender)
   
   def details(self):
      print(f"hello my name is {self.name} and age is {self.age} and i am {self.gender}")
      
   
   
p=Person()
# p1=Person()

# print(p)
# print(p1)
# print(type(p))

# print(isinstance(p,int()))


# p.setName("Ram")
# p.setAge(12)
# p.setGender("male")
# p.details()


# p.setName("shysam")
# p.details()



# p1=Person()
# p1.setName("SHyam")
# p1.getName()

# print(p.name)
# # p.setName('fkjlsdlfsd')
# p.getName()



