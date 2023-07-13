# # # def person(name,email,password,address="nepal"):
# # #     print(f"""
# # #           hi! {name}!How are your,
# # #           email is {email}
# # #           and you live in {address}
# # #           """)
    
# # # person(name='bhupesh',password='bhupesh7shakya@gmail.com',email='password')


# # # def person(*args):
# # #         print(f"""
# # #           hi! {args[0]}!How are your,
# # #           email is {args[1]}
# # #           and you live in {args[2]}
# # #           """)
# # # person("name","email@","somewhere")

# # def person(**kargs):
# #         print(f"""
# #           hi! {kargs['name']}!How are your,
# #           email is {kargs['email']}
# #           and you live in {kargs['password']}
# #           """)
        
# # person(name="name",email="email@",password="somewhere")


# # def recursion():
# #     number=int(input("enter the number "))
# #     if number<=11:
# #         print('Ok')
# #         recursion()
# #     else:
# #         print('number was greater than 11')
    
# # recursion()

# # categories = {
# #     "Electronics": {
# #         "Mobile": ["Apple", "Samsung", "Google"],
# #         "TV": ["Sony", "LG", "Samsung"],
# #         "Laptop": ["Dell", "HP", "Lenovo"]
# #     }
# # }



# # def recursivePrint():
    
# # j=1
# # while j<=5:
# #     i=5
# #     while i>=j:
# #         print(i,end="")
# #         i-=1
# #     print()
# #     j+=1


# # file handling

# f = open("demo.txt")


# print(f.readlines()[1])

# from m import H

# print(H)


# import os 
# os.makedirs('day 15')
# os.chdir('day 15')
# f = open('task.py','w')

# os.remove('day 15')


from typing import Any


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __eq__(self, object):
        return self.x==object.x and self.y==object.y
    
    
    def __gt__(self, object):
        return self.x>object.x and self.y>object.y
    
    
    def draw(self):
       print(f" {self.x} {self.y}")
    
    # def __str__(self):
    #     return (f'point ko object hai')
point=Point(1,2)
other=Point(1,2)
# print(point.__eq__(other))
# print(point>other)
# print(point.draw())
# point.draw()

# print(type(point))
# print(isinstance(1,int))


# class TagCloud:
#     def __init__(self):
#         self.languages={}
        
#     def add(self,lang):
#         self.languages[lang]=self.languages.get(lang,0)+1

#     def __iter__(self):
#         return iter(self.languages)
    
# t=TagCloud()
# t.add('a')
# t.add('a')
# t.add('a')
# print(iter(t))


class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        
    def __str__(self):
        return f"{self.__x} and {self.__y}"
    
    def __eq__(self, other):
        # return self == other
        return self.__x == other.__x 
    
    
point = Point(10,10)
another = Point(10,10)

# print the point object
# print(type(point))

# print(point ==another )

# print(point.y)



# class Product:
#     __price=None
#     name=None
#     def __str__(self) -> str:
#         return f"{self.__price} {self.name}"
#     def __init__(self,price):
#         self.set_price(price)
    
#     def set_price(self,value):
#         self.__price=value
    
#     def get_price(self):
#         return self.__price
        

# product=Product()
# product.__price=12
# product.description=123123

# print(type(product.description))
# product.name="dsf"
# print(product.name)
# print(product.__price)
# print(product)

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def set_name(self,value):
        self.__name=value
        
    
class Animal:
    
    def __init__(self) -> None:
        self.age=1
        print("i was called")
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
    
    def eat(self):
        print('eat')


class Mammal(Animal):
    def __init__(self) -> None:
        self.age=1
        print("M was called")

    
    def walk(self):
        print('walk')


class Fish(Animal):
    def __init__(self) -> None:
        self.age=1
    #  print("i was called")

     
    def swim(self):
        print('swim')
    
# m = Mammal()
# m.eat()

# Output : 'eat'

from abc import ABC, abstractmethod

class Computer(ABC,object):
    @abstractmethod
    def process(self):
        pass
    
class Laptop(Computer):
    def process(self):
        print("I am running Google Chrome")


class Mobile(Computer):
    def process(self):
        print("I am running Mobile Legend")
# com = Computer()

lap=Laptop()
# lap.computer()

lap.process()

