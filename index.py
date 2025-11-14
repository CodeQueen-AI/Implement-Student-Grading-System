student_name = input("Enter student name: ")

num_subjects = int(input("How many subjects do you have? "))

if num_subjects == 1:
    sub1 = input("Enter subject 1 name: ")
    mark1 = float(input(f"Enter marks for {sub1}: "))
    total_marks = mark1
elif num_subjects == 2:
    sub1 = input("Enter subject 1 name: ")
    mark1 = float(input(f"Enter marks for {sub1}: "))
    sub2 = input("Enter subject 2 name: ")
    mark2 = float(input(f"Enter marks for {sub2}: "))
    total_marks = mark1 + mark2
elif num_subjects == 3:
    sub1 = input("Enter subject 1 name: ")
    mark1 = float(input(f"Enter marks for {sub1}: "))
    sub2 = input("Enter subject 2 name: ")
    mark2 = float(input(f"Enter marks for {sub2}: "))
    sub3 = input("Enter subject 3 name: ")
    mark3 = float(input(f"Enter marks for {sub3}: "))
    total_marks = mark1 + mark2 + mark3
elif num_subjects == 4:
    sub1 = input("Enter subject 1 name: ")
    mark1 = float(input(f"Enter marks for {sub1}: "))
    sub2 = input("Enter subject 2 name: ")
    mark2 = float(input(f"Enter marks for {sub2}: "))
    sub3 = input("Enter subject 3 name: ")
    mark3 = float(input(f"Enter marks for {sub3}: "))
    sub4 = input("Enter subject 4 name: ")
    mark4 = float(input(f"Enter marks for {sub4}: "))
    total_marks = mark1 + mark2 + mark3 + mark4
elif num_subjects == 5:
    sub1 = input("Enter subject 1 name: ")
    mark1 = float(input(f"Enter marks for {sub1}: "))
    sub2 = input("Enter subject 2 name: ")
    mark2 = float(input(f"Enter marks for {sub2}: "))
    sub3 = input("Enter subject 3 name: ")
    mark3 = float(input(f"Enter marks for {sub3}: "))
    sub4 = input("Enter subject 4 name: ")
    mark4 = float(input(f"Enter marks for {sub4}: "))
    sub5 = input("Enter subject 5 name: ")
    mark5 = float(input(f"Enter marks for {sub5}: "))
    total_marks = mark1 + mark2 + mark3 + mark4 + mark5
elif num_subjects == 6:
    sub1 = input("Enter subject 1 name: ")
    mark1 = float(input(f"Enter marks for {sub1}: "))
    sub2 = input("Enter subject 2 name: ")
    mark2 = float(input(f"Enter marks for {sub2}: "))
    sub3 = input("Enter subject 3 name: ")
    mark3 = float(input(f"Enter marks for {sub3}: "))
    sub4 = input("Enter subject 4 name: ")
    mark4 = float(input(f"Enter marks for {sub4}: "))
    sub5 = input("Enter subject 5 name: ")
    mark5 = float(input(f"Enter marks for {sub5}: "))
    sub6 = input("Enter subject 6 name: ")
    mark6 = float(input(f"Enter marks for {sub6}: "))
    total_marks = mark1 + mark2 + mark3 + mark4 + mark5 + mark6
elif num_subjects == 7:
    sub1 = input("Enter subject 1 name: ")
    mark1 = float(input(f"Enter marks for {sub1}: "))
    sub2 = input("Enter subject 2 name: ")
    mark2 = float(input(f"Enter marks for {sub2}: "))
    sub3 = input("Enter subject 3 name: ")
    mark3 = float(input(f"Enter marks for {sub3}: "))
    sub4 = input("Enter subject 4 name: ")
    mark4 = float(input(f"Enter marks for {sub4}: "))
    sub5 = input("Enter subject 5 name: ")
    mark5 = float(input(f"Enter marks for {sub5}: "))
    sub6 = input("Enter subject 6 name: ")
    mark6 = float(input(f"Enter marks for {sub6}: "))
    sub7 = input("Enter subject 7 name: ")
    mark7 = float(input(f"Enter marks for {sub7}: "))
    total_marks = mark1 + mark2 + mark3 + mark4 + mark5 + mark6 + mark7
else:
    print("Sorry! This program supports up to 7 subjects only.")
    exit()

average_marks = total_marks / num_subjects
percentage = (total_marks / (num_subjects * 100)) * 100

if percentage >= 50:
    result = "Pass"
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"
else:
    result = "Fail"
    grade = "No Grade"

# Print the result
print("\n==================== STUDENT REPORT ====================")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Result: {result}")
print(f"Grade: {grade}")
