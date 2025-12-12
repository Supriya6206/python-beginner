# ----------------------------------LIST PRACTICE SET-------------------------------


# s=[4,6,7]
# print(type(s))
# print(s)
# sum=s[0]+s[1]+s[2]
# print(sum)


# list=[2,5,8,4]


# food=("momo", "fried rice", "icecream", "cake", "pasta")
# print(food)
# print(food[0], food[4])



# list=[7,3,12,10]
# print(list[1:3])


# li=[10,20,30,40,50]
# print(li[1:3])


# fru=["mango", "grapes", "banana"]
# print(fru)
# fru[1]="orange"
# print(fru)



# list=[3,7,2,9]
# print(list)
# list.append(13)
# print(list)
# print(list.pop(4))
# print(list)


# s=[2,9,12,23,45]
# a=["harry", "steve", "larry"]
# print(s); print(a)
# b=s+a
# print(b)
# print(b.pop(-1))
# print(b)


# l=[1, 2, 3, 4, 5]
# print(l)
# print(type(l))
# lt=tuple(l)
# print(lt)
# print(type(lt))
# ll=list(lt)
# print(ll)
# print(type(ll))
# print(len(ll))


# n=["sky", 5, 7.667, True]
# print(n)


# ----------------------------------TUPLES PRACTICE SET-------------------------------

# t=(1,3,6,38,99)
# print(t[2])
# l=list(t)
# l[3]=73
# print(l)
# tt=tuple(l)
# print(tt)


# a=(29,28,830,36)
# b=("missy", "cat")
# print(a+b)


# n=(23,87,73,47,83)
# print(n[2:4])

# x=[5,5,5,2,2]
# y=x.count(5)
# print(y)



# -----------------------------SETS PRACTICE--------------------------

# s=[4,2,7,1]
# print(s)
# print(s.append(44))
# print(s)
# s.remove(2)
# print(s)


# a=[4,7,13,5]
# print(a)
# b=["apollo","lily"]
# print(a+b)


# list=[1,2,2,3,4,4,4,5]
# set=set(list)
# print(set)


#--------------------------DICTIONARY PRACTICE SETS-----------------------

# dict={
#     "name":"sione",
#     "age":19,
#     "city":"eden"
    
# }
# print(dict["city"])
# dict.update({"country":"Germany"})
# print(dict)
# dict.update({"age":29})
# print(dict)
# dict.pop("city")
# print(dict)

# dict={
#     "sione":"blue",
#     "hermonie":"black",
#     "mikasa":"red"
# }
# print(dict.keys())
# print(dict.values())


keys=["a","b","c"]
values=[1, 2, 3]
di= {
    
    keys[0]:values[0],
    keys[1]:values[1],
    keys[2]:values[2]
}
print(di)
print(di.get("a","1"))