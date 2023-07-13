# while True:
#     try:
#         a=int(input("Enter number:"))
#         b=int(input("Enter number:"))

#         print(a/b)
        
#     except ZeroDivisionError:
#         print("Cannot divide by Zero number. Please Try again")
        
#     except ValueError:
#         print("Please enter valid numbers.")
#     except Exception as e:
#         print(e)


# number='123adfewa'
# int(number)

# file 
# r
# error 

# ask your which file you want to open 
# file name enter 
# mode=input("Enter the mode")
# file_name=input("Enter the file name:")
# try:
#     f= open(file_name,'r')
#     print(f.read())
# except FileNotFoundError:
#     print("File Doesn't exists You must create it first")
# except Exception as e:
#     print(f"Something went wrong!! {e}")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# n = int(input('Enter Positve number'))

# if n<0:
#     raise Exception("Number should be positive")