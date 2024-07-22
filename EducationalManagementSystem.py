import re

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Doctor(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.courses = []

    def create_course(self, course_code, course_name):
        course = Course(course_code, course_name, self)
        self.courses.append(course)
        return course

    def create_assignment(self, course, assignment_name):
        assignment = Assignment(course, assignment_name)
        course.assignments.append(assignment)
        return assignment

    def list_courses(self):
        for course in self.courses:
            print(f"Course Code: {course.course_code}, Course Name: {course.course_name}")

    def view_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        print("Course not found.")

    def view_assignment(self, course, assignment_name):
        for assignment in course.assignments:
            if assignment.assignment_name == assignment_name:
                return assignment
        print("Assignment not found.")

class TeachingAssistant(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.courses = []

    def assist_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        for course in self.courses:
            print(f"Course Code: {course.course_code}, Course Name: {course.course_name}")

    def view_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        print("Course not found.")

class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        for course in self.courses:
            print(f"Course Code: {course.course_code}, Course Name: {course.course_name}")

    def view_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        print("Course not found.")

class Course:
    def __init__(self, course_code, course_name, doctor):
        self.course_code = course_code
        self.course_name = course_name
        self.doctor = doctor
        self.assignments = []

    def create_assignment(self, assignment_name, correct_answer, user):
        if isinstance(user, Doctor) or isinstance(user, TeachingAssistant):
            assignment = Assignment(self, assignment_name, correct_answer)
            self.assignments.append(assignment)
            return assignment
        else:
            raise PermissionError("Only doctors and teaching assistants can create assignments.")

    def list_assignments(self):
        for assignment in self.assignments:
            print(f"Assignment Name: {assignment.assignment_name}")

    def view_assignment(self, assignment_name):
        for assignment in self.assignments:
            if assignment.assignment_name == assignment_name:
                return assignment
        print("Assignment not found.")

class Assignment:
    def __init__(self, course, assignment_name, correct_answer):
        self.course = course
        self.assignment_name = assignment_name
        self.correct_answer = correct_answer
        self.grades = {}
        self.solutions = {}

    def add_grade(self, student, grade, user):
        if not isinstance(user, Doctor):
            raise PermissionError("Only doctors can add grades.")
        self.grades[student] = grade

    def submit_solution(self, student, solution):
        if not isinstance(student, Student):
            raise PermissionError("Only students can submit solutions.")
        self.solutions[student] = solution


    def check_solution_correctness(self, student):
        if isinstance(self.course.doctor, Doctor):
            if student in self.solutions:
                submitted_solution = self.solutions[student]
                if submitted_solution == self.correct_answer:
                    print(f"Solution for {student.name} is correct.")
                else:
                    print(f"Solution for {student.name} is not correct.")
            else:
                print(f"No solution found for {student.name}.")
        else:
            raise PermissionError("Only doctors can check solution correctness.")
        
    def show_info(self):
        print(f"Assignment Name: {self.assignment_name}")
        print(f"Course Name: {self.course.course_name}")
        print(f"Doctor Name: {self.course.doctor.name}")

    def grade_solution(self, student, solution):
        if solution == self.correct_answer:
            self.grades[student] = "Correct"
        else:
            self.grades[student] = "Incorrect"

    def grade_solution(self, student, grade):
        if student in self.solutions:
            self.grades[student] = grade
        else:
            print(f"No solution found for student {student.name}.")

    def show_info(self):
        print(f"Assignment Name: {self.assignment_name}")
        print(f"Course Name: {self.course.course_name}")
        print(f"Doctor Name: {self.course.doctor.name}")

    def view_grades(self, current_user):
        if isinstance(current_user, Doctor):
            for student, grade in self.grades.items():
                print(f"{student.name}: {grade}")
        else:
            print("Only doctors can view grades.")
    
    def view_solution(self, student, user):
        if not isinstance(user, Doctor):
            raise PermissionError("Only doctors can view solutions.")
        if student in self.solutions:
            print(f"Solution for {student.name}: {self.solutions[student]}")
        else:
            print(f"No solution found for {student.name}.")

class System:
    def __init__(self):
        self.doctors = {}
        self.teaching_assistants = {}
        self.students = {}
        self.courses = {}  # Store courses separately for easy enrollment
        self.current_user = None

    def validate_email(self, email):
        regex = r'^[A-Za-z0-9._%+-]+@(?:yahoo\.com|gmail\.com|menofia\.edu\.eg)$'
        return re.match(regex, email.lower()) is not None

    def sign_up(self, user_type, user_id, name, email):
        try:
            if not self.validate_email(email):
                print("Invalid email format.")
                return

            if user_type == "doctor":
                if user_id not in self.doctors:
                    self.doctors[user_id] = Doctor(user_id, name, email)
                else:
                    print("User ID already exists.")
            elif user_type == "ta":
                if user_id not in self.teaching_assistants:
                    self.teaching_assistants[user_id] = TeachingAssistant(user_id, name, email)
                else:
                    print("User ID already exists.")
            elif user_type == "student":
                if user_id not in self.students:
                    self.students[user_id] = Student(user_id, name, email)
                else:
                    print("User ID already exists.")
            else:
                print("Invalid user type.")
        except Exception as e:
            print(f"Error during sign up: {e}")

    def sign_in(self, user_type, user_id):
        try:
            if user_type == "doctor":
                if user_id in self.doctors:
                    self.current_user = self.doctors[user_id]
                    print(f"Signed in as Doctor {self.current_user.name}.")
                else:
                    print("Invalid user ID.")
            elif user_type == "ta":
                if user_id in self.teaching_assistants:
                    self.current_user = self.teaching_assistants[user_id]
                    print(f"Signed in as TA {self.current_user.name}.")
                else:
                    print("Invalid user ID.")
            elif user_type == "student":
                if user_id in self.students:
                    self.current_user = self.students[user_id]
                    print(f"Signed in as Student {self.current_user.name}.")
                else:
                    print("Invalid user ID.")
            else:
                print("Invalid user type.")
        except Exception as e:
            print(f"Error during sign in: {e}")

    def log_out(self):
        self.current_user = None
        print("Logged out successfully.")

    def list_available_courses(self):
        if self.courses:
            print("Available Courses:")
            for course_code, course_name in self.courses.items():
                print(f"Course Code: {course_code}, Course Name: {course_name}")
        else:
            print("No courses available.")

    def enroll_course(self):
        try:
            self.list_available_courses()
            course_code = input("Enter Course Code to enroll: ")
            if course_code in self.courses:
                course = self.courses[course_code]
                if isinstance(self.current_user, Student):
                    self.current_user.enroll_course(course)
                    print(f"Enrolled in {course.course_name} successfully.")
                else:
                    print("Only students can enroll in courses.")
            else:
                print("Course not found.")
        except Exception as e:
            print(f"Error during course enrollment: {e}")

    def main_menu(self):
        while True:
            if self.current_user is None:
                print("\nWelcome to The Educational Management System\n")
                print("1. Sign Up")
                print("2. Sign In")
                print("3. Exit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    user_type = input("Enter user type (doctor/ta/student): ")
                    user_id = input("Enter your User ID: ")
                    name = input("Enter your User Name: ")
                    email = input("Enter your Email: ")
                    self.sign_up(user_type, user_id, name, email)

                elif choice == "2":
                    user_type = input("Enter user type (doctor/ta/student): ")
                    user_id = input("Enter your User ID: ")
                    self.sign_in(user_type, user_id)

                elif choice == "3":
                    break

                else:
                    print("Invalid choice.")
            else:
                if isinstance(self.current_user, Doctor):
                    self.doctor_menu()
                elif isinstance(self.current_user, TeachingAssistant):
                    self.ta_menu()
                elif isinstance(self.current_user, Student):
                    self.student_menu()

    def doctor_menu(self):
        while True:
            print("\nDoctor Menu")
            print("1. List Courses")
            print("2. Create Course")
            print("3. View Course")
            print("4. Log Out")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.current_user.list_courses()

            elif choice == "2":
                course_code = input("Enter Course Code: ")
                course_name = input("Enter Course Name: ")
                course = self.current_user.create_course(course_code, course_name)
                self.courses[course_code] = course
                print("Course created successfully.")

            elif choice == "3":
                course_code = input("Enter Course Code: ")
                course = self.current_user.view_course(course_code)
                if course:
                    self.course_menu(course)

            elif choice == "4":
                self.log_out()
                break

            else:
                print("Invalid option.")

    def ta_menu(self):
        while True:
            print("\nTeaching Assistant Menu")
            print("1. List Assisted Courses")
            print("2. View Course")
            print("3. Log Out")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.current_user.list_courses()

            elif choice == "2":
                course_code = input("Enter Course Code: ")
                course = self.current_user.view_course(course_code)
                if course:
                    self.course_menu(course)

            elif choice == "3":
                self.log_out()
                break

            else:
                print("Invalid option.")

    def student_menu(self):
        while True:
            print("\nStudent Menu")
            print("1. List Enrolled Courses")
            print("2. View Course")
            print("3. Enroll in a Course")
            print("4. Log Out")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.current_user.list_courses()

            elif choice == "2":
                course_code = input("Enter Course Code: ")
                course = self.current_user.view_course(course_code)
                if course:
                    self.course_menu(course)

            elif choice == "3":
                self.enroll_course()

            elif choice == "4":
                self.log_out()
                break

            else:
                print("Invalid option.")

    def course_menu(self, course):
        while True:
            print("\nCourse Menu")
            print("1. List Assignments")
            print("2. Create Assignment")
            print("3. View Assignment")
            print("4. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                course.list_assignments()

            elif choice == "2":
                try:
                    assignment_name = input("Enter Assignment Name: ")
                    correct_answer = input("Enter correct solution: ")
                    assignment = course.create_assignment(assignment_name, correct_answer, self.current_user)
                    print(f"Assignment {assignment.assignment_name} created.")
                except PermissionError as e:
                    print(e)

            elif choice == "3":
                assignment_name = input("Enter Assignment Name: ")
                assignment = course.view_assignment(assignment_name)
                if assignment:
                    self.assignment_menu(assignment)

            elif choice == "4":
                break

            else:
                print("Invalid option.")

   
    def assignment_menu(self, assignment):
        while True:
            print("\nAssignment Menu")
            print("1. View Assignment Info")
            print("2. Add Grade")
            print("3. Submit Solution")
            print("4. View Grades")
            print("5. View Solution")
            print("6. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                assignment.show_info()

            elif choice == "2":
                try:
                    if isinstance(self.current_user, Doctor):
                        student_name = input("Enter Student Name: ")
                        student = self.find_student_by_name(student_name)
                        if student:
                            grade = input("Enter Grade: ")
                            assignment.add_grade(student, grade, self.current_user)
                            print(f"Grade added for {student.name}.")
                        else:
                            print("Student not found.")
                    else:
                        print("Only doctors can add grades.")

                except PermissionError as e:
                    print(e)

            elif choice == "3":
                try:
                    if isinstance(self.current_user, Student):
                        solution = input("Enter Solution: ")
                        assignment.submit_solution(self.current_user, solution)
                        print(f"Solution submitted for {self.current_user.name}.")
                    else:
                        print("Only students can submit solutions.")

                except PermissionError as e:
                    print(e)

            elif choice == "4":
                assignment.view_grades(self.current_user)

            elif choice == "5":
                try:
                    if isinstance(self.current_user, Doctor):
                        student_name = input("Enter Student Name: ")
                        student = self.find_student_by_name(student_name)
                        if student:
                            assignment.view_solution(student, self.current_user)
                        else:
                            print("Student not found.")
                    else:
                        print("Only doctors can view solutions.")

                except PermissionError as e:
                    print(e)

            elif choice == "6":
                break

            else:
                print("Invalid option.")

    

    def find_student_by_name(self, student_name):
        for student in self.students.values():
            if student.name == student_name:
                return student
        return None

  

if __name__ == "__main__":
    system = System()
    system.main_menu()
