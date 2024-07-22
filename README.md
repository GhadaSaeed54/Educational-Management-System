Educational Management System

Overview
The Educational Management System is a Python-based application designed to facilitate course management, assignment creation, grading, and solution submissions within an educational environment. It supports three main user roles: Doctor, Teaching Assistant (TA), and Student, each with specific permissions and functionalities.

Components:

Users:
Doctor: Responsible for creating and managing courses, assignments, grading student submissions, and viewing solutions.
Teaching Assistant (TA): Assists in courses by viewing course details, assignments, and providing support.
Student: Enrolls in courses, submits solutions to assignments, and views their grades.
Courses and Assignments:

Course: Identified by a unique course code and managed by a Doctor. Contains multiple assignments.
Assignment: Belongs to a specific course and includes attributes such as assignment name, correct answer, grades, and student solutions.

System:
Manages user authentication, course enrollment, assignment creation, and provides interfaces for different user roles.
Functionalities

Doctor:
Creates and manages courses.
Creates assignments within courses.
Adds grades to student submissions.
Views courses, assignments, and student solutions.

Teaching Assistant:
Assists in courses assigned to them.
Views courses they assist in.
Views assignments within assisted courses.

Student:
Enrolls in courses.
Views enrolled courses.
Submits solutions to assignments.
Views grades received for assignments.

Usage
Signing Up:
Choose user type (doctor, ta, student).
Enter user ID, name, and email (valid email from Yahoo, Gmail, or Menofia.edu.eg).

Signing In:
Enter user type and user ID to log in.
Navigate through menus based on user role to access functionalities.

Main Menu:
Offers options for signing up, signing in, or exiting the system.

Role-specific Menus:
Doctor Menu: Manage courses, create assignments, and view course details.
Teaching Assistant Menu: Assist in courses, view assisted courses, and their details.
Student Menu: Enroll in courses, view enrolled courses, and manage assignments.


Notes
Permissions are strictly enforced (e.g., only doctors can add grades or view student solutions).
Error handling is implemented for invalid inputs and unauthorized actions.
Users interact with menus to perform actions based on their roles, ensuring secure and role-specific functionalities.
