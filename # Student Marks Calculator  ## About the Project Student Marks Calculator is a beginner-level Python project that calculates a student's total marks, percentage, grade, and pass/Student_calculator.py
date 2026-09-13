print("Student Marks Calculator")

name = input("Enter your name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry

percentage = (total / 300) * 100
if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("Student:", name)
print("Maths:", maths)
print("Physics:", physics)
print("Chemistry:", chemistry)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 50:
    result = "Pass"
else:
    result = "Fail"

print("Result:", result)
