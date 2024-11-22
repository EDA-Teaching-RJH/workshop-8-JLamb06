name = input("Enter the students name: ")
age = int(input("Enter the students age: "))
grade = input("Enter the students grade: ")
file = open("students.txt","w")
file.write(f"{name}, {age}, {grade} \n")
file.close()

with open("students.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print("hello,", line.rstrip())