student={
    "name" : "Supriya",
    "age" : 19,
    "course" : "CSIT"
}

print("Name:",student["name"])
print("Age:",student["age"])
print("Course:",student["course"])

# marks = {
#     "Math":75,
#     "Physics":85,
#     "Nepali":90
# }

# if marks["Physics"] >=40:
#     print("You have passed in Physics")
    
# else:
#     print("You have failed in Physics")

marks = {
    "Math":75,
    "Physics":85,
    "Nepali":30
}

if marks["Physics"] >=40 and marks["Math"] >=40 and marks["Nepali"] >=40  :
    print("You have passed")
    
else:
    print("You have failed")