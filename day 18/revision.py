class Person:
    def __init__(self, name,age):
        self.name = name
        self.age=age
    
    def __eq__(self,  object):
        return self.name == object.name
    
    def __gt__(self, object):
        return self.age>object.age
    
    def __le__(self, object):
        return self.age<=object.age
    

    
    # def __str__(self):
    #     return f"My name is {self.name}"
        

# person=Person("Ram",10)
# person_two=Person("Rams",11)

# person.__eq__(person_two)
# print(person == person_two)
# # 
# # person.__gt__(person_two)
# # print(person > person_two)
# # 
# # person.__gt__(person_two)
# # print(person < person_two)
# print(person<=person_two)


# todo:task
# two object attribute add with magic function


class Product:
    def __init__(self,price):
        self.price=price

    def __add__(self,object):
        return self.price+object.price
    
product=Product(10)
product_two=Product(30)


# product.price

# product_two.price
# product.__add__(product_two)
print(product+product_two)