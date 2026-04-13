student_marks={ }
number_of_students=int(input("enter number of students"))

for i in range(number_of_students):
 student_name=input("enter your name")
 student_score=int(input("enter your score"))

 student_marks[student_name]=student_score

total=sum(student_marks.values)
average=total/student_marks

print(average)

while True:
    score = int(input("Enter score {0-100}: "))

    if 0 <= score <= 100:
        break
    else:
        print("Invalid score! Please enter a number between 0")