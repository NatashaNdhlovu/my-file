students = {}

while True:
    name = input("Enter name (or 'done'): ")

    if name == "done":
        break

    # score validation
    score = int(input("Enter score (0-100): "))

    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score (0-100): "))

    students[name] = score

print("report")

total = 0

# alphabetical order
for name in sorted(students):
    print(name, ":", students[name])
    total += students[name]

# average
average = total / len(students)
print("Average:", average)

# top student
top = max(students, key=students.get)
print("Top Student:", top, "with", students[top])