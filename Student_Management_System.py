class StudentDatabase:

    student_list = []

    @classmethod
    def add_student(cls, student):

        if not isinstance(student, Student):
            raise TypeError("Apni Student na bhai.")

        if cls.find_student(student.student_id) is not None:
            raise ValueError(f"A student with ID: {student.student_id} already exists.")
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.student_id == student_id:
                return student
        return None

class Student:

    def __init__(self, student_id, name, department, is_enrolled):
        student_id = str(student_id).strip()
        if not student_id.isdigit():
            raise ValueError("Enter valid student id.")

        self.__student_id = student_id        
        self.__name = name                    
        self.__department = department        
        self.__is_enrolled = is_enrolled      

        StudentDatabase.add_student(self)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__department

    @property
    def is_enrolled(self):
        return self.__is_enrolled

    def enroll_student(self):
        if self.__is_enrolled:
            raise ValueError(f"Student {self.__student_id} is already enrolled.")

        self.__is_enrolled = True
        return self.__is_enrolled

    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError(f"Student {self.__student_id} is not enrolled.")

        self.__is_enrolled = False
        return self.__is_enrolled

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        return f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, is enrolled: {status}"



def get_student_by_id(student_id):
    student_id = student_id.strip()

    if not student_id.isdigit():
        raise ValueError("Invalid student ID.")

    student = StudentDatabase.find_student(student_id)

    if student is None:
        raise ValueError(f"Invalid student ID. No student found with ID {student_id}.")

    return student


def view_all_students():
    if not StudentDatabase.student_list:
        print("No students found.")
        return

    for student in StudentDatabase.student_list:
        print(student.view_student_info())


def enroll_student():
    student = get_student_by_id(input("Enter student ID to enroll: "))
    student.enroll_student()
    print(f"Student {student.name} has been enrolled successfully.")


def drop_student():
    student = get_student_by_id(input("Enter student ID to drop: "))
    student.drop_student()
    print(f"Student {student.name} has been dropped successfully.")


def main():
    Student("240042132", "Mahdi Nur Samin", "CSE", True)
    Student("240042116", "Safwan Bhuiyan", "SWE", True)
    Student("250042132", "Aksa Mim", "CEE", True)
    Student("240042102", "Musaddik Ibna Solimullah", "SWE", True)

    while True:
        print("\n===== Student Management Menu =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        try:
            if choice == "1":
                view_all_students()
            elif choice == "2":
                enroll_student()
            elif choice == "3":
                drop_student()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
        except ValueError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()