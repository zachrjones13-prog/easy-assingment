import csv

passed_students = []
failed_students = []
all_scores = []

with open("students.csv", "r", newline="") as data:
    csv_file = csv.reader(data)
    headings = next(csv_file)

    for student in csv_file:
        score = int(student[1])
        all_scores.append(score)

        if score >= 70:
            passed_students.append(student)
        else:
            failed_students.append(student)

# save passing students
with open("passed.csv", "w", newline="") as data:
    csv_file = csv.writer(data)
    csv_file.writerow(headings)
    csv_file.writerows(passed_students)

# save failing students
with open("failed.csv", "w", newline="") as data:
    csv_file = csv.writer(data)
    csv_file.writerow(headings)
    csv_file.writerows(failed_students)

# find highest and lowest scores
students = passed_students + failed_students

highest_score = max(students, key=lambda student: int(student[1]))
lowest_score = min(students, key=lambda student: int(student[1]))

# calculate average
average_score = sum(all_scores) / len(all_scores)

print("highest:", highest_score)
print("lowest:", lowest_score)
print("average:", average_score)
