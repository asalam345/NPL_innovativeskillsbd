class GradeCalculator:
    def __init__(self):
        self.total_credits = 0
        self.total_points = 0
    
    def get_course_marks(self, course_name):
        """Get marks for a single course"""
        print(f"\n--- {course_name} ---")
        ct = self.get_valid_score("Class Test", 0, 20)
        mid = self.get_valid_score("Mid Term", 0, 30)
        final = self.get_valid_score("Final Term", 0, 50)
        
        total = ct + mid + final
        grade = self.calculate_grade(total)
        point = self.grade_to_point(grade)
        
        print(f"Total Marks: {total}/100 | Grade: {grade} | Grade Point: {point:.2f}")
        
        return total, grade, point
    
    def get_valid_score(self, exam_name, min_score, max_score):
        """Get valid score within range"""
        while True:
            try:
                score = float(input(f"Enter {exam_name} score ({min_score}-{max_score}): "))
                if min_score <= score <= max_score:
                    return score
                else:
                    print(f"Error: Score must be between {min_score} and {max_score}")
            except ValueError:
                print("Error: Please enter a valid number")
    
    def calculate_grade(self, total_marks):
        if total_marks >= 80:
            return "A+"
        elif total_marks >= 75:
            return "A"
        elif total_marks >= 70:
            return "A-"
        elif total_marks >= 65:
            return "B+"
        elif total_marks >= 60:
            return "B"
        elif total_marks >= 55:
            return "B-"
        elif total_marks >= 50:
            return "C+"
        elif total_marks >= 45:
            return "C"
        elif total_marks >= 40:
            return "D"
        else:
            return "F"
    
    def grade_to_point(self, grade):
        grade_points = {
            "A+": 4.00, "A": 3.75, "A-": 3.50,
            "B+": 3.25, "B": 3.00, "B-": 2.75,
            "C+": 2.50, "C": 2.25, "D": 2.00,
            "F": 0.00
        }
        return grade_points.get(grade, 0.00)
    
    def add_course_result(self, credit, grade_point):
        """Add course result to CGPA calculation"""
        self.total_points += (grade_point * credit)
        self.total_credits += credit
    
    def calculate_cgpa(self):
        """Calculate final CGPA"""
        if self.total_credits > 0:
            return self.total_points / self.total_credits
        return 0.0
    
    def get_letter_grade(self, cgpa):
        """Get letter grade based on CGPA"""
        if cgpa >= 3.75:
            return "A+ (First Class with Distinction)"
        elif cgpa >= 3.50:
            return "A (First Class)"
        elif cgpa >= 3.25:
            return "B+ (Second Class)"
        elif cgpa >= 3.00:
            return "B (Second Class)"
        elif cgpa >= 2.75:
            return "C+ (Third Class)"
        elif cgpa >= 2.50:
            return "C (Third Class)"
        else:
            return "F (Fail)"
def cse(self):
    print("\n=== CSE Department - Fixed Credit System ===")
    print("All courses have 3 credits each")
        
        # Get marks for all courses using class method
    print("\nEnter marks for each course:")
    calculator = GradeCalculator()

    _, prog_grade, prog_point = calculator.get_course_marks("Programming Course")
    calculator.add_course_result(3, prog_point)
        
    _, ds_grade, ds_point = calculator.get_course_marks("Data Structures Course")
    calculator.add_course_result(3, ds_point)
        
    _, db_grade, db_point = calculator.get_course_marks("Database Course")
    calculator.add_course_result(3, db_point)
        
    _, algo_grade, algo_point = calculator.get_course_marks("Algorithms Course")
    calculator.add_course_result(3, algo_point)
        
    _, web_grade, web_point = calculator.get_course_marks("Web Technology Course")
    calculator.add_course_result(3, web_point)  

def fixed_credit_system():
    print("=" * 50)
    print("FIXED CREDIT SYSTEM - GRADE CALCULATOR")
    print("=" * 50)
    
    # Create calculator object
    calculator = GradeCalculator()
    
    # Department selection
    print("\nAvailable Departments:")
    print("1. CSE")
    print("2. EEE")
    print("3. BBA")
    print("4. CE")
    print("5. Pharmacy")
    
    department = input("\nEnter department number: ")


    if department == 1:
       calculator.cse()

    elif department == "EEE":
        print("\n=== EEE Department - Fixed Credit System ===")
        print("All courses have 3 credits each")
        
        print("\nEnter marks for each course:")
        
        _, ct_grade, ct_point = calculator.get_course_marks("Circuit Theory Course")
        calculator.add_course_result(3, ct_point)
        
        _, elec_grade, elec_point = calculator.get_course_marks("Electronics Course")
        calculator.add_course_result(3, elec_point)
        
        _, ps_grade, ps_point = calculator.get_course_marks("Power Systems Course")
        calculator.add_course_result(3, ps_point)
        
        _, mach_grade, mach_point = calculator.get_course_marks("Machines Course")
        calculator.add_course_result(3, mach_point)
        
        _, cs_grade, cs_point = calculator.get_course_marks("Control Systems Course")
        calculator.add_course_result(3, cs_point)
        
    elif department == "BBA":
        print("\n=== BBA Department - Fixed Credit System ===")
        print("All courses have 3 credits each")
        
        print("\nEnter marks for each course:")
        
        _, acc_grade, acc_point = calculator.get_course_marks("Accounting Course")
        calculator.add_course_result(3, acc_point)
        
        _, mk_grade, mk_point = calculator.get_course_marks("Marketing Course")
        calculator.add_course_result(3, mk_point)
        
        _, fin_grade, fin_point = calculator.get_course_marks("Finance Course")
        calculator.add_course_result(3, fin_point)
        
        _, mgt_grade, mgt_point = calculator.get_course_marks("Management Course")
        calculator.add_course_result(3, mgt_point)
        
        _, eco_grade, eco_point = calculator.get_course_marks("Economics Course")
        calculator.add_course_result(3, eco_point)
        
    elif department == "CE":
        print("\n=== CE Department - Fixed Credit System ===")
        print("All courses have 3 credits each")
        
        print("\nEnter marks for each course:")
        
        _, sa_grade, sa_point = calculator.get_course_marks("Structural Analysis Course")
        calculator.add_course_result(3, sa_point)
        
        _, geo_grade, geo_point = calculator.get_course_marks("Geotechnical Engineering Course")
        calculator.add_course_result(3, geo_point)
        
        _, sur_grade, sur_point = calculator.get_course_marks("Surveying Course")
        calculator.add_course_result(3, sur_point)
        
        _, trans_grade, trans_point = calculator.get_course_marks("Transportation Engineering Course")
        calculator.add_course_result(3, trans_point)
        
        _, env_grade, env_point = calculator.get_course_marks("Environmental Engineering Course")
        calculator.add_course_result(3, env_point)
        
    elif department == "PHARM":
        print("\n=== Pharmacy Department - Fixed Credit System ===")
        print("All courses have 3 credits each")
        
        print("\nEnter marks for each course:")
        
        _, pharma_grade, pharma_point = calculator.get_course_marks("Pharmacology Course")
        calculator.add_course_result(3, pharma_point)
        
        _, medchem_grade, medchem_point = calculator.get_course_marks("Medicinal Chemistry Course")
        calculator.add_course_result(3, medchem_point)
        
        _, pharmaceutics_grade, pharmaceutics_point = calculator.get_course_marks("Pharmaceutics Course")
        calculator.add_course_result(3, pharmaceutics_point)
        
        _, practice_grade, practice_point = calculator.get_course_marks("Pharmacy Practice Course")
        calculator.add_course_result(3, practice_point)
        
        _, biochem_grade, biochem_point = calculator.get_course_marks("Biochemistry Course")
        calculator.add_course_result(3, biochem_point)
        
    else:
        print("Invalid department selected!")
        return
    
    # Calculate and display results
    cgpa = calculator.calculate_cgpa()
    letter_grade = calculator.get_letter_grade(cgpa)
    
    print("\n" + "=" * 50)
    print("GRADE REPORT - FIXED CREDIT SYSTEM")
    print("=" * 50)
    print(f"Department: {department}")
    print(f"Total Credits: {calculator.total_credits}")
    print(f"CGPA: {cgpa:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print("=" * 50)

# Run the fixed credit system
if __name__ == "__main__":
    fixed_credit_system()