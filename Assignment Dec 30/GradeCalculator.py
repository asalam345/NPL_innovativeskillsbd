class GradeCalculator:
    def __init__(self):
        self.total_credits = 0
        self.total_points = 0
        self.department_name = ""
    
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
    
    def calculate_cgpa(self,totalPoints, totalCredits):
        """Calculate final CGPA"""
        if totalCredits > 0:
            return totalPoints / totalCredits
        return 0.0
    
    def get_letter_grade(self, cgpa):
        """Get letter grade based on CGPA"""
        # match cgpa:
        #     case '1':

        if cgpa >= 3.75:
            return "A+"
        elif cgpa >= 3.50:
            return "A"
        elif cgpa >= 3.25:
            return "B+"
        elif cgpa >= 3.00:
            return "B"
        elif cgpa >= 2.75:
            return "C+"
        elif cgpa >= 2.50:
            return "C"
        else:
            return "F (Fail)"