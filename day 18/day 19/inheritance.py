# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def speak(self):
#         print(" how how")
        
# class Cat(Animal):
#     def speak(self):
#         print(" meow meow")
 
 
# dog = Dog()
# dog.eat()
# dog.speak()
        
        
# cat= Cat()
# cat.eat()
# cat.speak()
        

# type  inheritance in python

# single inheritance
# multi level inheritance
# multi inhertance 


# mutilevel inhertance

# grandfather->father->son

class GrandFather(object):
    def eyes(self):
        print("green")
        
        
class Father(GrandFather):
    def hair(self):
        print("brown")
        
class Mother:
    def skin(self):
        print("skin white")

class Son(Father,Mother):
    pass

son=Son
print(son)
# son.hair()
# son.eyes()
# son.skin()

# todo:
# inhertance 
# euta new example 