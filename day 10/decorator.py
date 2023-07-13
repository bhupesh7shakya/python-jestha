# def fuc(a):
#     print(a)
    
# fuc()
def star(func):
    def wrapper(*name,**kwargs):
        print('*'*10)
        print(type(name))
        func(*name)
        print('*'*10)
    return wrapper

def dash(func):
    def wrapper(*name):
        print('_'*10)
        print(type(name))
        func(*name)
        print('_'*10)
    return wrapper

@dash
def good_bye(name):
    print(type(name))
    print(f"good bye!!,{name}")

good_bye("bhpesh")


# @dash
# s

# @dash
# @star
# def hello_world():
#     print("hello world")
    
    



# hello_world()
# wrapper()
# star(hello_world)()


# hello_world()
# actually working 
# dash(star(good_bye))()

# star(hello_world)()
# star(good_bye)()

# __________
# %%%%%%%%%%
# **********
# hello world
# **********
# %%%%%%%%%
# __________

# after that decorate goodybye() with only star decorator``


# def i_take_function(func):
#     func()

# def i_take_another_function(func):
#     func()
    
    
# def hello_world():
#     print("hello world")
    
# # callback function
# i_take_function(hello_world)

def world():
    print('hello owlr')
    
# print(type(world))
# world()