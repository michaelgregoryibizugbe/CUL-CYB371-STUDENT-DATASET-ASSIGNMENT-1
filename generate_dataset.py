"""
CUL-CYB 371 - Data Mining and Data Warehousing
Assignment Two: Fictional Student Dataset Generator
Author: Michael Gregory Ibizugbe
Language: Python 3 (standard library only)

Generates a fictional student dataset with:
Student ID, Department, Level, Attendance Percentage, Average Examination Score
and saves it as students.csv
"""
import csv
import random

random.seed(42)  # reproducible results

DEPARTMENTS = [
    "Cyber Security", "Computer Science", "Information Technology",
    "Software Engineering", "Data Science", "Information Systems",
]
LEVELS = ["100 Level", "200 Level", "300 Level", "400 Level"]


def generate_students(n=50):
    students = []
    for i in range(1, n + 1):
        student_id = f"CYB-2026-{i:04d}"
        department = random.choice(DEPARTMENTS)
        level = random.choice(LEVELS)
        attendance = round(random.uniform(45.0, 100.0), 1)
        # students who attend more tend to score higher
        avg_score = round(min(100.0, max(20.0, attendance * 0.6 + random.uniform(10, 40))), 1)
        students.append([student_id, department, level, attendance, avg_score])
    return students


def main():
    students = generate_students(50)
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Student ID", "Department", "Level",
                         "Attendance Percentage", "Average Examination Score"])
        writer.writerows(students)
    print(f"Saved {len(students)} fictional student records to students.csv")


if __name__ == "__main__":
    main()
