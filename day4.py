# -----------------GLOBAL VARIABLES----------

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()



# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)



# --------------global keyword----------------
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)




# ---------changing the value of global variable inside the function using global keyword--------
# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)



# ---------complex number---------
# x = 1j
# print(x)


# -----list-----
# x = ["apple", "banana", "cherry"]


# ---tuple-----
# x = ["apple", "banana", "cherry"]


# x = ("apple", "banana", "cherry")	-------->tuple	

# x = range(6)	range	


# x = {"name" : "John", "age" : 36}	-------->dict	


# x = {"apple", "banana", "cherry"}	-------->set	


# x = frozenset({"apple", "banana", "cherry"})	-------->frozenset	


# x = True	-------->bool	


# x = b"Hello"	-------->bytes	


# x = bytearray(5)	-------->bytearray

	
# x = memoryview(bytes(5))	-------->memoryview	


# x = None	-------->NoneType


# x=int(input("enter any number:"))
# rem=x%2
# print("the remainder is:",rem)

# a=5
# b=3.5
# if(a>b):
#     print("greater=",a)
# else:
#     print("greater=",b)


# ------------------------------------STRING AND STRING SLICING---------------------------------

# name="Supriya"
# nameshort=name[0:4]
# print(nameshort)
# character=name[2]
# print(character)




# name="supriya"
# print(name[:3])
# print(name[3:])
# print(name[0:6:2])


# name="edinburgh"
# print(len(name))



# name="edinburgh of england"
# print(len(name))
# print(name.endswith("rgha"))
# print(name.startswith("edin"))
# print(name.capitalize())               
# print(name.upper())
# print(name.lower())
# print(name.title())
# count=name.count("e")
# print(count)
# replacename= name.replace("edinburgh","london")
# print(replacename)












# ----------------ESCAPE SEQUENCE-----------------
# name="harry is a good boy \n but not a \"bad\" boy"
# print(name)


# x=input("enter:")

# print(x)
# print(x.capitalize())

# x=input("enter your name:")

# print(f"Good Afternoon, {x}")





# ----------TO FIND A DOUBLE SPACE--------------------
# name="Harry is  a good  boy  and is  helpful"
# print(name.find("  "))
# print(name.replace("  ","    "))   
#------------------------------------strings are immutable which means that we cant change them by running functions on them





# --------------LIST AND TUPLES--------------\
    
    
    
# a=["aryan", 6, 10, "Mango", 16]
# print(a[3])
# a[3]="Orange" 
# print(a[3])
# print(a[0:2])


num=[6, 2, 29, 38, 12, 9, 45, 121, 68]
print(num[4])
num.append(89)
print(num)
num.sort()
print(num)
num.reverse()
print(num)
num.insert(2,7)
print(num)
num.pop(2)
value=num.pop(2)
print(num)
print(value)
num.remove(89)
print(num)
