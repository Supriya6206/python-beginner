# a= int(input("enter your age"))
# if(a<18):
#     print("You are minor")
    
# elif(a>=18 and a<60):
#     print("You are adult")
    
# else:
#     print("You are senior citizen")


# a=int(input("enter any number:"))
# if(a<0):
#     print("This is negative number")
    
# elif(a==0):
#     print("This is zero")
    
# else:
#     print("This is positive number")



# color=["red","green","blue"]
# a=input("enter the color:")
# if("red" in color or "yellow" in color or "blue" in color):
#     print("yes, it is present in the list")
    
# else:
#     print("no,it is not present in the list")



n=[1,6,4,23,12]
i = int(input("Enter a index(0:4):"))

if(i>=0 and i<5):
    print("The value at index",i,"is",n[i])
    
else:
    print("index out of range")
