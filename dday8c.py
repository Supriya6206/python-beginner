# age= int(input("enter your age"))
# if(age>=18):
#     print("Yes")
# else:
#     print("No")

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))
# d=int(input("enter fourth number:"))

# if(a>b and a>c and a>d):
#     print(a," a is greatest")
    
# elif(b>c and b>a and b>d):
#     print(b,"b is greatest")
    
# elif(c>b and c>a and c>d):
#     print(c,"c is greatest")

# else:
#     print(d, "d is greatest")


# print("Enter the marks obtained by a student:")
# sub1=int(input("Enter marks of subject 1:"))
# sub2=int(input("Enter marks of subject 2:"))
# sub3=int(input("Enter marks of subject 3:"))

# total_percentage= ((sub1+sub2+sub3)/300)*100

# if(total_percentage>=40 and sub1>33 and sub2>33 and sub3>33):
#     print("you passed")
    
# else:
#     print("You have failed")


# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# message = input("Enter your comment:")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is a spam")
    
# else:
#     print("This comment is not a spam")


# character= input("Enter any word:")

# if(len(character)>=10):
#     print("this char is more than ten")
    
# else:
#     print("less than ten")


l =["harry", "mike", "el", "dustin", "robin"]
name= input("enter your name:")
 
if(name in l):
    print("YOur name is in list")

else:
    print("not in list")