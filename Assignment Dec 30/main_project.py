from GradeCalculator import GradeCalculator
from fixed import FixedCreditSystem
from opened import OpenCreditSystem
class MainProject:
    def main():
        print("Choose Credit System:")
        print("1. Fixed Credit (All courses = 3 credits)")
        print("2. Open Credit (Custom credits per course)")
        
        choice = input("Enter choice (1 or 2): ")
        
        calculator = GradeCalculator()
        fix = FixedCreditSystem()
        open = OpenCreditSystem()
        
        departments = {
            1: ("CSE", ["C", "DSA", "Database Systems", "Computer Networks", "OS"]),
            2: ("EEE", ["Circuit Theory", "Electronics", "Power Systems", "Control System", "Mathematics"]),
            3: ("BBA", ["Accounting", "Marketing", "Finance", "Management", "Economics"]),
            4: ("English", ["Cultural Studies", "Rhetoric", "Creative Writing", "Linguistics", "English Literature"]),
            5: ("Bangla", ["Bangla Grammar", "Linguistics", "Literature", "Composition & Rhetoric", "Comparative Bangla Studies"])
        }

        dept_choice = int(input("\nSelect Department (1-5): "))
        if dept_choice not in departments:
            print("Invalid department!")
            return

        name, subjects = departments[dept_choice]

        if choice == "1":
             _, p, c = fix.department_fix_credit(name, subjects)  # your existing fixed method
        elif choice == "2":
            _, p, c = open.department_open_credit(name, subjects)  # new open method
        else:
            print("Invalid choice!")
            return

        # Final CGPA (same for both)
        cgpa = calculator.calculate_cgpa(p,c)
        letter_grade = calculator.get_letter_grade(cgpa)

        print("\n" + "=" * 50)
        print("FINAL GRADE REPORT")
        print("=" * 50)
        print(f"Department: {name}")
        print(f"Total Credits: {c}")
        print(f"CGPA: {cgpa:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print("=" * 50)

    if __name__ == "__main__":
        main()