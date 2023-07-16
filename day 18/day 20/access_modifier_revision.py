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

# accessing the public varaible
# print(product.name)

# accessing the protected varaible
# print(product._price)

# accessing the private varaible
# private varibale can't be access directly
# print(product.get_category())


# print(product.get_category())

product.category="sound"
print(product.category)
# print(product.get_category())
