"""
Grade students based on marks 

marks >= 90, grade = "A"
90 > marks >= 80, grade = "B"
80 > marks >= 70, grade = "C"
70 > marks, grade = "D"

"""

marks = int(input("Enter the marks : "))

if(marks >= 90 ):
    print("Grade A")
elif(90 > marks  >= 80):
    print("Grade B")
elif(80 > marks  >= 70):
    print("Grade C")
else:
    print("Grade D")