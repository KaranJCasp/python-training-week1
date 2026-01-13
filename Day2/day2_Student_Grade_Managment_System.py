'''
4. Student Grade Management System
Write a program that uses ONLY functions and dictionaries:
- Store student data: {name: {"marks": [list], "grade": ""}}
- Functions to implement:
  1. add_student(name, marks_list) - add new student
  2. calculate_grade(marks_list) - return grade (A/B/C/D/F based on average)
  3. get_student_report(name) - print detailed report
  4. get_class_topper() - return name of student with highest average
  5. save_to_file() - save all data to "students.txt"
  6. load_from_file() - load data from "students.txt"

Create a menu-driven program to test all functions.

Grading Scale: A(>=90), B(>=80), C(>=70), D(>=60), F(<60)
'''
students_db={}

def calculate_grade(marks_list):
    if not marks_list:
        return "F"
    avg = sum(marks_list) / len(marks_list)
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"


def add_student(name, marks_list):
    grade = calculate_grade(marks_list)
    students_db[name] = {"marks": marks_list, "grade": grade}
    print(f"Student {name} added successfully.")

def get_student_report(name):
    StudentData=students_db.get(name)
    print(f"Student Name: {name}")
    print(f"Student Marks: {StudentData['marks']}")
    print(f"Student Grade: {StudentData['grade']}")

#return name of student with highest average
def get_class_topper():
    if len(students_db)==0:
        return "Database is empty"
    else:
        highest_avg=1
        for name ,item in students_db.items():
            avg = int(sum(item['marks']) / len(item['marks']))
            if avg > highest_avg:
                highest_avg = avg
                Topper_name=name
        print({"name :":{Topper_name},"avg :":{highest_avg}})

def save_to_file():
    import json

    json_str = json.dumps(students_db, indent=4)
    with open("students.txt", "w") as f:
        f.write(json_str)
        f.close()

# load data from "students.txt"
def load_from_file():
    import json

    with open("students.txt", "r") as f:
        data = json.load(f)
        print(data)


add_student("jenil",[70,80,90])
add_student("kenil",[56,23,87])
get_student_report("jenil")
print("return name of student with highest average :", end=" ")
get_class_topper()
#save all data to "students.txt
save_to_file()
#load data from "students.txt
print("Load Data from txt file :", end=" ")
load_from_file()

# print(students_db)