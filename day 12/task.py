# todo:-task 
# take input from user whethere user want to login or register
# if user says regiter then take input from the user 
# 1.email
# 2.password
# 3.confirmpassword
# if password and confirm password are matched then store in list form from hint 1
# after the registration is complete print message as registraion successfully if not print error
# task end


# take input from user 
# email
# password
# confirm password
# list method append
# dictionary
# 3-4 register

# hint 1
# [
#     {
#         'email':"something@gmai..com",
#         'password':"password"
#     },
#       {
#         'email':"something@gmai..com",
#         'password':"password"
#     },
#         {
#         'email':"something@gmai..com",
#         'password':"password"
#     },
#           {
#         'email':"something@gmai..com",
#         'password':"password"
#     },
# ]

# login
# list check register cha ki xaina check garnu parcha
# 

def email_exists(email):
    for user in users:
        if user.get('email') == email:
            return True
    return False




def register(email,password):
        if email_exists(email=email):
            print("User Already Exists")
            return
        
        confirm_password=input('Enter your confirm_password:-')
        # print(users)
        if password == confirm_password:
            user={
                'email':email,
                'password':password
            }
            # print('#'*10)
            users.append(user)
            
            
def login(email,password):
       for user in users:
            if user.get('email') == email and user.get('password')==password:
                print('You have been Login successfully')
                global isLogin
                isLogin=True
                return
            print("Email or Password invalid")



users=[]
isLogin=False
while True:
    choice=int(input(f"""
                 1.Press 1 to register
                 2.Press 2 to login
                 3.Press 3 to exit
                 3.Press 4 to show all register user
                 """))
    
    if choice ==1 or choice==2:
        email=input('Enter your email:-')
        password=input('Enter your password:-')
        
    if choice == 1:
        register(email=email,password=password)
           
    if choice ==2:
        # print('login')
        login(email=email,password=password)
     
    
    if choice == 3:
        break
    
    if choice == 4:
        
        # email:_______|password:________ 
    
        # print(users)
        if isLogin:
            for user in users:
                print(f"|email:{user.get('email')} | password:{user.get('password')}|")
        else:
            print('You must Login first')



# my_list=[1,2,3,4]

# for element in my_list:
#     print(element)



# my_list=[
#     {
#         'name':'bhupesh'
#     }
# ]
# my_list.append({
#     'name':'test'
# })
# print(my_list)