from GradeCalculator import GradeCalculator

class OpenCreditSystem(GradeCalculator):
    def department_open_credit(self, name, subjects):
        """Handle department courses with OPEN credit system"""
        print(f"\n=== {name} - Open Credit System ===")
        print("Course credits can vary (e.g., 1, 2, 3, 4)")

        total_credit_points = 0
        total_credits = 0

        print("\nEnter marks and credits for each course:")
        calculator = GradeCalculator()
        for subject in subjects:
            # Get marks
            _, grade, point = calculator.get_course_marks(f"{subject} Course")
            
            # Get credit for this course
            while True:
                try:
                    credit = int(input(f"Enter credit hours for {subject} Course (e.g., 1-4): "))
                    if 1 <= credit <= 4:
                        break
                    else:
                        print("Credit must be between 1 and 4.")
                except ValueError:
                    print("Please enter a valid integer.")

            credit_points = credit * point
            total_credit_points += credit_points
            total_credits += credit

            # Also update the main CGPA tracker
            calculator.add_course_result(credit, point)

        if total_credits > 0:
            gpa = total_credit_points / total_credits
            print(f"\nTotal Credits: {total_credits}")
            print(f"GPA: {gpa:.2f}")
            return gpa, total_credit_points, total_credits
        
    