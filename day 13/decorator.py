# def star(func):
#     def wrapper(*args,**kwargs):
#         print('*'*10)
#         func(*args,**kwargs)
#         print('*'*10)
#     return wrapper

# def dash(func):
#     def wrapper():
#         print('_'*10)
#         print()
#         func()
#         print('_'*10)
#     return wrapper

# @star
# def hello(name):
#     print(f'hello {name}')
    
# hello('ram')