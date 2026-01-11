all_grades = [
[88, 92, 70], # Student 0 
 [45, 80, 33], # Student 1 (Has a 45!) 
 [99, 100, 35] # Student 2
]
for idx, student_grades in enumerate(all_grades):
        for grade in student_grades:
                if grade < 50:
                        print(f"Student {idx} failed a subject!")
    #if any(grade < 50 for grade in student_grades):
        