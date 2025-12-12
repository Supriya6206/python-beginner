# -----------------------------DICTIONARY AND SETS---------------------------------------

# marks ={
#     "nima" : 100,
#     "harry" : 46,
#     "jack" : 89,  
#     "esa"  : "london",
# }

# print(marks, type(marks))
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"nima":90,"eunho":86})
# print(marks)
# print(marks.get("esa"))
# print(marks["harry"])


# print(marks["harry2"])        ----->this will tell none
# print(marks["harry2"])        ----->this will occur error





# --------------------------SETS--------------------------
# d={}             #empty dictionary
# e= set()

# s = {1, 2, 33, 8, 5 ,5,"harry"}        #dont use d={} as it will create an empty dictionary
# print(s)
# print(type(s))
# s.add(67)
# print(s)
# print(len(s))
# s.remove(33)
# print(s.union({8,11}))
# print(s.intersection({8,11}))
# print({1,2}.issubset(s))
# print(s.issuperset({1,2}))








# --------------------------PRACTICE SET-------------------------

# words= {
#     "madad": "help",
#     "aaha": "wow",
#     "dhilo": "late"
# }

# word= input("enter the word you want to know the meaning of: ")

# print(words[word])




# s=set()

# n1=int(input("Enter the number:"))
# s.add(n1)

# n2=int(input("Enter the number:"))
# s.add(n2)
# n3=int(input("Enter the number:"))
# s.add(n3)
# n4=int(input("Enter the number:"))
# s.add(n4)
# n5=int(input("Enter the number:"))
# s.add(n5)
# n6=int(input("Enter the number:"))
# s.add(n6)
# n7=int(input("Enter the number:"))
# s.add(n7)
# n8=int(input("Enter the number:"))
# s.add(n8)

# print(s)



# s=set()
# s.add(18)
# s.add("18")
# print(s)


# s=set()
# s.add(20)
# s.add(20.0)   #same as 20
# s.add("20")
# print(s)
# print(len(s))

# s={}
# print(type(s))


# d={}


# name= input("enter the names;")
# lang= input("enter fav language:")

# d.update({name:lang})


# name= input("enter the names;")
# lang= input("enter fav language:")

# d.update({name:lang})


# name= input("enter the names;")
# lang= input("enter fav language:")

# d.update({name:lang})


# name= input("enter the names;")
# lang= input("enter fav language:")

# d.update({name:lang})

# print(d)
# print(d.keys())



#cant change the value of the list
# s={8, 7, 12, "harry", [1,2]}