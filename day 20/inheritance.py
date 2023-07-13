# types of inheritance

# single
# multi-level
# multiple

class Animal:
    def eat(self):
        print("Eating")
        

class Mammal(Animal):
    def walk(self):
        print("walk")
        
# mamamal=Mammal()
# mamamal.walk()    
# mamamal.eat() 


class Fish(Animal):
    def swim(self):
        print("swim")


fish=Fish()

# print(isinstance(fish,Animal))

# # mammal=Mammal()
# # mammal.eat()
# # mammal.walk()

# # fish=Fish()
# # fish.eat()
# # fish.swim()

# # todo: task
# # animal 
# # cat and cot class animal duitaimai inherit 
# # and create the object of each and callit with its extra feature


# class Dog(Mammal):
#     def speak(self):
#         print("howhowhow")
        
# class Cat(Mammal):
#     def speak(self):
#         print("meoew meow")
        
# dog=Dog()
# dog.eat()
# dog.walk()
# dog.speak()


# animal->eat
# mammal->walk
# dog->speak


# class GrandFather:
#     def house(self):
#         print("House")
        
        
# class Father(GrandFather):
#     def car(self):
#         print("Car")
        
# class Mother:
#     def jewellary(self):
#         print("jewellary")

# class Son(Father,Mother):
#     def ps5(self):
#         print("ps5")
        

# class Daughter(Mother):
#     def make_up(self):
#         print("make_up")
        
        
        
# son=Son()
# son.car()
# son.house()
# son.ps5()
# son.jewellary()
        
        
        