# example of recursion
# def number(start,end):
#     print(start)
#     # 1 != 10
#     if start is not end:
#         number(start+1,end)
    
# number(1,10)


# def eachChar(text):
#     for char in text:
#          print(char)
         
# eachChar("hello world")
# do it using recursion

# task 
# create a variable and assign value hello world
# print each character using recursion

def eachChar(text,number=0):
    print(text[number])
    if text[number] is not text[-1]:
        eachChar(text,number+1)

eachChar("hello")
# print
# h
# e



