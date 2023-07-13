class Product(object):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    
    def get_name(self):
        print(f"{self.name}")
        
product= Product("Laptop",10)

print(isinstance(product,str))
# product.