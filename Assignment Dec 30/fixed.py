from GradeCalculator import GradeCalculator

class FixedCreditSystem(GradeCalculator):
    def department_fix_credit(self, name, subjects, credits=None):
        self.department_name = name
        if credits is None:
            credits = [3] * len(subjects)
        elif len(credits) != len(subjects):
            raise ValueError("Credits list must match number of subjects")
        
        print(f"\n=== {name} - Fixed Credit System ===")
        calculator = GradeCalculator()
        total_credit_points = 0
        total_credits = 0
        for subject, credit in zip(subjects, credits):
            _, grade, point = calculator.get_course_marks(subject)
            
            credit_points = credit * point
            total_credit_points += credit_points 
            total_credits += credit

            calculator.add_course_result(credit, point)
            print(f"→ {subject}: {credit} credits, Grade: {grade}, Point: {point:.2f}")
        
        if total_credits > 0:
            gpa = total_credit_points / total_credits
            print(f"\nTotal Credits: {total_credits}")
            print(f"GPA: {gpa:.2f}")
            return gpa, total_credit_points, total_credits