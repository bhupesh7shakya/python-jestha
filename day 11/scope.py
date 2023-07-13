# global scope
a=10

def number():
    print(a)
    a=11
    print(a)
    
number()
print(a)
# local scope
# def number():
#     global a
#     a=10

# # a=11
# # number()
# print(a)


# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   return myinnerfunc

# # myinnerfunc()
# print(myfunc()())


# a=10


# def change():
#     # print(a+5)
#     a=10
#     b=a+5
#     # a=11
#     a=b
#     print(a)
#     # print(a=11)
#     # print(a)
# change()