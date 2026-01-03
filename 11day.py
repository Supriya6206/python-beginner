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

# marks = {
#     "Math":75,
#     "Physics":85,
#     "Nepali":30
# }

# if marks["Physics"] >=40 and marks["Math"] >=40 and marks["Nepali"] >=40  :
#     print("You have passed")
    
# else:
#     print("You have failed")
    
    
    
    
    
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
    print(f"Your grade is {grade} - Excellent!")
elif marks >= 80:
    grade = "B"
    print(f"Your grade is {grade} - Good!")
elif marks >= 70:
    grade = "C"
    print(f"Your grade is {grade} - Average!")
elif marks >= 60:
    grade = "D"
    print(f"Your grade is {grade} - Pass!")
else:
    grade = "F"
    print(f"Your grade is {grade} - Fail!")
