# 

# pass is keyword that is when nothing is needed
# while True:
#     pass
# if True:
#     pass 
# def hello_world():
#     return "hello world"
# hello_world()
# # print(hello_world())

# #value = "hello world"
# value= hello_world()

# create calculate function
# 1 argument integer
#output= 1*10
#output /2 return garera print

print()

# def calculate(num):
#     return (num*10)/2
   
# print(calculate(1))

# def person(name,age):
#     return f"{name} {age}"

# print(person(age="22",name="bhupesh"))

# print("a","b","c",end=".")

#credential_Check 
# function return True False yedi username ra password correct True and wrong False

def credential_check(username,password):
    USERNAME="bhupesh"
    PASSWORD="password"
    
    if username==USERNAME and password == PASSWORD:
        return True
    return False

# print(credential_check("bhupesh","password"))


# refactor code
def credential_check(username,password):
    USERNAME="bhupesh"
    PASSWORD="password"
    
    return  username==USERNAME and password == PASSWORD


def login(username,password):
    # print(username)
    # print(password)
    if credential_check(username,password):
        print('Welcome to Somthing')
        return 0
        
    # else:
        print("invalid")

login('bhupesh','password')