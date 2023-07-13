# types of access modifier
# public
# protected
# private


class Product:
    name="Headphone" #public
    _price=299 #protecteed
    __category="Sound"  #private
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self,value):
        self.__category=value
    
   
    
    # category=property(get_category,set_category)
    
product= Product()

product.category="sounds"

print(product.category)
# print(product.get_category())

# 

# print(product.__category)

# print(product.name)
# print(product._price)

# print(product.__category)

# accesing private varibale using getter and setter
# print(product.get_category())

# print(product.category)


# product.__category=10
# print(product.__category)




# product.category="sounds"
# print(product.category)
# product.category=10
# print(product.category)
# print(product.get_category())


# product.hello="sounds"
# print(product.hello)