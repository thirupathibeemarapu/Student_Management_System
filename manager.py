import json
import os
from student import Student

FILE_NAME = "students.json"


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.students = json.load(file)
        else:
            self.students = []

    def save_students(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")

        # Validation: unique ID
        for s in self.students:
            if s["id"] == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")

        student = Student(student_id, name, grade)
        self.students.append(student.to_dict())
        self.save_students()
        print("Student added successfully!")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        for s in self.students:
            if s["id"] == student_id:
                s["name"] = input("Enter new name: ")
                s["grade"] = input("Enter new grade: ")
                self.save_students()
                print("Student updated successfully!")
                return

        print("Student not found!")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        for s in self.students:
            if s["id"] == student_id:
                self.students.remove(s)
                self.save_students()
                print("Student deleted successfully!")
                return

        print("Student not found!")

    def list_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n{:<10} {:<20} {:<10}".format("ID", "Name", "Grade"))
        print("-" * 40)

        for s in self.students:
            print("{:<10} {:<20} {:<10}".format(s["id"], s["name"], s["grade"]))
