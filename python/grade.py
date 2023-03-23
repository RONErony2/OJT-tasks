# 8. Take the input marks from user using input() function and find out the grade of the students. Note
# the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
# 51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the

# 1st approach
def find_grade(marks):
    if marks >= 0 and marks <= 100:
        grade = {4 : "C2", 5 : 'C2', 6 : "C1", 7 : "B2", 8 : "B1", 9 : "A2", 10 : "A1"}
        if marks < 40:
            return 'Fail'
        key = marks//10
        if marks%10 > 0:
            key += 1
        return grade[int(key)]
    else:
        print("Invalid Marks !....")

marks = float(input("Enter the marks : "))
res = find_grade(marks)
if res != None:
    print(f"Your grade : {res}")

# 2nd approach
def find_grade(marks):
    if marks >= 0 and marks <= 100:
        if marks >= 91 and marks <= 100:
            grade = "A1"
        elif marks >= 81 and marks <= 90:
            grade = "A2"
        elif marks >= 71 and marks <= 80:
            grade = "B1"
        elif marks >= 61 and marks <= 70:
            grade = "B2"
        elif marks >= 51 and marks <= 60:
            grade = "C1"
        elif marks >= 40 and marks <= 50:
            grade = "C2"
        else:
            grade = "Fail"
        return grade
    else:
        print("Invalid Marks !....")

marks = float(input("Enter the marks : "))
res = find_grade(marks)
if res != None:
    print(f"Your grade : {res}")
