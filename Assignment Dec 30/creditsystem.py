# =============================================
# FIXED CREDIT SYSTEM - GRADE CALCULATOR
# =============================================

def fixed_credit_system():
    print("=" * 50)
    print("FIXED CREDIT SYSTEM - GRADE CALCULATOR")
    print("=" * 50)
    
    # Department selection
    print("\nAvailable Departments:")
    print("1. Computer Science & Engineering (CSE)")
    print("2. Electrical & Electronics Engineering (EEE)")
    print("3. Business Administration (BBA)")
    print("4. Civil Engineering (CE)")
    print("5. Pharmacy (Pharm)")
    
    department = input("\nEnter department name (CSE/EEE/BBA/CE/Pharm): ").strip().upper()
    
    if department == "CSE":
        print("\n=== CSE Department - Fixed Credit System ===")
        print("Courses: Programming (3 credits), Data Structures (3 credits),")
        print("Database (3 credits), Algorithms (3 credits), Web Tech (3 credits)")
        
        # Programming course
        print("\n--- Programming Course (3 credits) ---")
        prog_ct = float(input("Enter Class Test score (0-20): "))
        prog_mid = float(input("Enter Mid Term score (0-30): "))
        prog_final = float(input("Enter Final Term score (0-50): "))
        prog_total = prog_ct + prog_mid + prog_final
        
        # Data Structures course
        print("\n--- Data Structures Course (3 credits) ---")
        ds_ct = float(input("Enter Class Test score (0-20): "))
        ds_mid = float(input("Enter Mid Term score (0-30): "))
        ds_final = float(input("Enter Final Term score (0-50): "))
        ds_total = ds_ct + ds_mid + ds_final
        
        # Database course
        print("\n--- Database Course (3 credits) ---")
        db_ct = float(input("Enter Class Test score (0-20): "))
        db_mid = float(input("Enter Mid Term score (0-30): "))
        db_final = float(input("Enter Final Term score (0-50): "))
        db_total = db_ct + db_mid + db_final
        
        # Algorithms course
        print("\n--- Algorithms Course (3 credits) ---")
        algo_ct = float(input("Enter Class Test score (0-20): "))
        algo_mid = float(input("Enter Mid Term score (0-30): "))
        algo_final = float(input("Enter Final Term score (0-50): "))
        algo_total = algo_ct + algo_mid + algo_final
        
        # Web Technology course
        print("\n--- Web Technology Course (3 credits) ---")
        web_ct = float(input("Enter Class Test score (0-20): "))
        web_mid = float(input("Enter Mid Term score (0-30): "))
        web_final = float(input("Enter Final Term score (0-50): "))
        web_total = web_ct + web_mid + web_final
        
        # Calculate grades and grade points
        prog_grade = calculate_grade(prog_total)
        ds_grade = calculate_grade(ds_total)
        db_grade = calculate_grade(db_total)
        algo_grade = calculate_grade(algo_total)
        web_grade = calculate_grade(web_total)
        
        prog_point = grade_to_point(prog_grade)
        ds_point = grade_to_point(ds_grade)
        db_point = grade_to_point(db_grade)
        algo_point = grade_to_point(algo_grade)
        web_point = grade_to_point(web_grade)
        
        # All courses have 3 credits in fixed system
        total_credits = 15  # 5 courses × 3 credits
        total_points = (prog_point * 3) + (ds_point * 3) + (db_point * 3) + (algo_point * 3) + (web_point * 3)
        
        cgpa = total_points / total_credits
        
    elif department == "EEE":
        print("\n=== EEE Department - Fixed Credit System ===")
        print("Courses: Circuit Theory (3 credits), Electronics (3 credits),")
        print("Power Systems (3 credits), Machines (3 credits), Control Systems (3 credits)")
        
        # Circuit Theory course
        print("\n--- Circuit Theory Course (3 credits) ---")
        ct_ct = float(input("Enter Class Test score (0-20): "))
        ct_mid = float(input("Enter Mid Term score (0-30): "))
        ct_final = float(input("Enter Final Term score (0-50): "))
        ct_total = ct_ct + ct_mid + ct_final
        
        # Electronics course
        print("\n--- Electronics Course (3 credits) ---")
        elec_ct = float(input("Enter Class Test score (0-20): "))
        elec_mid = float(input("Enter Mid Term score (0-30): "))
        elec_final = float(input("Enter Final Term score (0-50): "))
        elec_total = elec_ct + elec_mid + elec_final
        
        # Power Systems course
        print("\n--- Power Systems Course (3 credits) ---")
        ps_ct = float(input("Enter Class Test score (0-20): "))
        ps_mid = float(input("Enter Mid Term score (0-30): "))
        ps_final = float(input("Enter Final Term score (0-50): "))
        ps_total = ps_ct + ps_mid + ps_final
        
        # Machines course
        print("\n--- Machines Course (3 credits) ---")
        mach_ct = float(input("Enter Class Test score (0-20): "))
        mach_mid = float(input("Enter Mid Term score (0-30): "))
        mach_final = float(input("Enter Final Term score (0-50): "))
        mach_total = mach_ct + mach_mid + mach_final
        
        # Control Systems course
        print("\n--- Control Systems Course (3 credits) ---")
        cs_ct = float(input("Enter Class Test score (0-20): "))
        cs_mid = float(input("Enter Mid Term score (0-30): "))
        cs_final = float(input("Enter Final Term score (0-50): "))
        cs_total = cs_ct + cs_mid + cs_final
        
        # Calculate grades and grade points
        ct_grade = calculate_grade(ct_total)
        elec_grade = calculate_grade(elec_total)
        ps_grade = calculate_grade(ps_total)
        mach_grade = calculate_grade(mach_total)
        cs_grade = calculate_grade(cs_total)
        
        ct_point = grade_to_point(ct_grade)
        elec_point = grade_to_point(elec_grade)
        ps_point = grade_to_point(ps_grade)
        mach_point = grade_to_point(mach_grade)
        cs_point = grade_to_point(cs_grade)
        
        total_credits = 15
        total_points = (ct_point * 3) + (elec_point * 3) + (ps_point * 3) + (mach_point * 3) + (cs_point * 3)
        cgpa = total_points / total_credits
        
    elif department == "BBA":
        print("\n=== BBA Department - Fixed Credit System ===")
        print("Courses: Accounting (3 credits), Marketing (3 credits),")
        print("Finance (3 credits), Management (3 credits), Economics (3 credits)")
        
        # Accounting course
        print("\n--- Accounting Course (3 credits) ---")
        acc_ct = float(input("Enter Class Test score (0-20): "))
        acc_mid = float(input("Enter Mid Term score (0-30): "))
        acc_final = float(input("Enter Final Term score (0-50): "))
        acc_total = acc_ct + acc_mid + acc_final
        
        # Marketing course
        print("\n--- Marketing Course (3 credits) ---")
        mk_ct = float(input("Enter Class Test score (0-20): "))
        mk_mid = float(input("Enter Mid Term score (0-30): "))
        mk_final = float(input("Enter Final Term score (0-50): "))
        mk_total = mk_ct + mk_mid + mk_final
        
        # Finance course
        print("\n--- Finance Course (3 credits) ---")
        fin_ct = float(input("Enter Class Test score (0-20): "))
        fin_mid = float(input("Enter Mid Term score (0-30): "))
        fin_final = float(input("Enter Final Term score (0-50): "))
        fin_total = fin_ct + fin_mid + fin_final
        
        # Management course
        print("\n--- Management Course (3 credits) ---")
        mgt_ct = float(input("Enter Class Test score (0-20): "))
        mgt_mid = float(input("Enter Mid Term score (0-30): "))
        mgt_final = float(input("Enter Final Term score (0-50): "))
        mgt_total = mgt_ct + mgt_mid + mgt_final
        
        # Economics course
        print("\n--- Economics Course (3 credits) ---")
        eco_ct = float(input("Enter Class Test score (0-20): "))
        eco_mid = float(input("Enter Mid Term score (0-30): "))
        eco_final = float(input("Enter Final Term score (0-50): "))
        eco_total = eco_ct + eco_mid + eco_final
        
        # Calculate grades and grade points
        acc_grade = calculate_grade(acc_total)
        mk_grade = calculate_grade(mk_total)
        fin_grade = calculate_grade(fin_total)
        mgt_grade = calculate_grade(mgt_total)
        eco_grade = calculate_grade(eco_total)
        
        acc_point = grade_to_point(acc_grade)
        mk_point = grade_to_point(mk_grade)
        fin_point = grade_to_point(fin_grade)
        mgt_point = grade_to_point(mgt_grade)
        eco_point = grade_to_point(eco_grade)
        
        total_credits = 15
        total_points = (acc_point * 3) + (mk_point * 3) + (fin_point * 3) + (mgt_point * 3) + (eco_point * 3)
        cgpa = total_points / total_credits
        
    elif department == "CE":
        print("\n=== CE Department - Fixed Credit System ===")
        print("Courses: Structural Analysis (3 credits), Geotech (3 credits),")
        print("Surveying (3 credits), Transportation (3 credits), Environmental (3 credits)")
        
        # Structural Analysis course
        print("\n--- Structural Analysis Course (3 credits) ---")
        sa_ct = float(input("Enter Class Test score (0-20): "))
        sa_mid = float(input("Enter Mid Term score (0-30): "))
        sa_final = float(input("Enter Final Term score (0-50): "))
        sa_total = sa_ct + sa_mid + sa_final
        
        # Geotechnical Engineering course
        print("\n--- Geotechnical Engineering Course (3 credits) ---")
        geo_ct = float(input("Enter Class Test score (0-20): "))
        geo_mid = float(input("Enter Mid Term score (0-30): "))
        geo_final = float(input("Enter Final Term score (0-50): "))
        geo_total = geo_ct + geo_mid + geo_final
        
        # Surveying course
        print("\n--- Surveying Course (3 credits) ---")
        sur_ct = float(input("Enter Class Test score (0-20): "))
        sur_mid = float(input("Enter Mid Term score (0-30): "))
        sur_final = float(input("Enter Final Term score (0-50): "))
        sur_total = sur_ct + sur_mid + sur_final
        
        # Transportation Engineering course
        print("\n--- Transportation Engineering Course (3 credits) ---")
        trans_ct = float(input("Enter Class Test score (0-20): "))
        trans_mid = float(input("Enter Mid Term score (0-30): "))
        trans_final = float(input("Enter Final Term score (0-50): "))
        trans_total = trans_ct + trans_mid + trans_final
        
        # Environmental Engineering course
        print("\n--- Environmental Engineering Course (3 credits) ---")
        env_ct = float(input("Enter Class Test score (0-20): "))
        env_mid = float(input("Enter Mid Term score (0-30): "))
        env_final = float(input("Enter Final Term score (0-50): "))
        env_total = env_ct + env_mid + env_final
        
        # Calculate grades and grade points
        sa_grade = calculate_grade(sa_total)
        geo_grade = calculate_grade(geo_total)
        sur_grade = calculate_grade(sur_total)
        trans_grade = calculate_grade(trans_total)
        env_grade = calculate_grade(env_total)
        
        sa_point = grade_to_point(sa_grade)
        geo_point = grade_to_point(geo_grade)
        sur_point = grade_to_point(sur_grade)
        trans_point = grade_to_point(trans_grade)
        env_point = grade_to_point(env_grade)
        
        total_credits = 15
        total_points = (sa_point * 3) + (geo_point * 3) + (sur_point * 3) + (trans_point * 3) + (env_point * 3)
        cgpa = total_points / total_credits
        
    elif department == "PHARM":
        print("\n=== Pharmacy Department - Fixed Credit System ===")
        print("Courses: Pharmacology (3 credits), Medicinal Chemistry (3 credits),")
        print("Pharmaceutics (3 credits), Pharmacy Practice (3 credits), Biochemistry (3 credits)")
        
        # Pharmacology course
        print("\n--- Pharmacology Course (3 credits) ---")
        pharma_ct = float(input("Enter Class Test score (0-20): "))
        pharma_mid = float(input("Enter Mid Term score (0-30): "))
        pharma_final = float(input("Enter Final Term score (0-50): "))
        pharma_total = pharma_ct + pharma_mid + pharma_final
        
        # Medicinal Chemistry course
        print("\n--- Medicinal Chemistry Course (3 credits) ---")
        medchem_ct = float(input("Enter Class Test score (0-20): "))
        medchem_mid = float(input("Enter Mid Term score (0-30): "))
        medchem_final = float(input("Enter Final Term score (0-50): "))
        medchem_total = medchem_ct + medchem_mid + medchem_final
        
        # Pharmaceutics course
        print("\n--- Pharmaceutics Course (3 credits) ---")
        pharmaceutics_ct = float(input("Enter Class Test score (0-20): "))
        pharmaceutics_mid = float(input("Enter Mid Term score (0-30): "))
        pharmaceutics_final = float(input("Enter Final Term score (0-50): "))
        pharmaceutics_total = pharmaceutics_ct + pharmaceutics_mid + pharmaceutics_final
        
        # Pharmacy Practice course
        print("\n--- Pharmacy Practice Course (3 credits) ---")
        practice_ct = float(input("Enter Class Test score (0-20): "))
        practice_mid = float(input("Enter Mid Term score (0-30): "))
        practice_final = float(input("Enter Final Term score (0-50): "))
        practice_total = practice_ct + practice_mid + practice_final
        
        # Biochemistry course
        print("\n--- Biochemistry Course (3 credits) ---")
        biochem_ct = float(input("Enter Class Test score (0-20): "))
        biochem_mid = float(input("Enter Mid Term score (0-30): "))
        biochem_final = float(input("Enter Final Term score (0-50): "))
        biochem_total = biochem_ct + biochem_mid + biochem_final
        
        # Calculate grades and grade points
        pharma_grade = calculate_grade(pharma_total)
        medchem_grade = calculate_grade(medchem_total)
        pharmaceutics_grade = calculate_grade(pharmaceutics_total)
        practice_grade = calculate_grade(practice_total)
        biochem_grade = calculate_grade(biochem_total)
        
        pharma_point = grade_to_point(pharma_grade)
        medchem_point = grade_to_point(medchem_grade)
        pharmaceutics_point = grade_to_point(pharmaceutics_grade)
        practice_point = grade_to_point(practice_grade)
        biochem_point = grade_to_point(biochem_grade)
        
        total_credits = 15
        total_points = (pharma_point * 3) + (medchem_point * 3) + (pharmaceutics_point * 3) + (practice_point * 3) + (biochem_point * 3)
        cgpa = total_points / total_credits
        
    else:
        print("Invalid department selected!")
        return
    
    # Display results
    print("\n" + "=" * 50)
    print("GRADE REPORT - FIXED CREDIT SYSTEM")
    print("=" * 50)
    print(f"Department: {department}")
    print(f"Total Credits: {total_credits}")
    print(f"CGPA: {cgpa:.2f}")
    
    if cgpa >= 3.75:
        print("Letter Grade: A+ (First Class with Distinction)")
    elif cgpa >= 3.50:
        print("Letter Grade: A (First Class)")
    elif cgpa >= 3.25:
        print("Letter Grade: B+ (Second Class)")
    elif cgpa >= 3.00:
        print("Letter Grade: B (Second Class)")
    elif cgpa >= 2.75:
        print("Letter Grade: C+ (Third Class)")
    elif cgpa >= 2.50:
        print("Letter Grade: C (Third Class)")
    else:
        print("Letter Grade: F (Fail)")
    print("=" * 50)

def calculate_grade(total_marks):
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

def grade_to_point(grade):
    if grade == "A+":
        return 4.00
    elif grade == "A":
        return 3.75
    elif grade == "A-":
        return 3.50
    elif grade == "B+":
        return 3.25
    elif grade == "B":
        return 3.00
    elif grade == "B-":
        return 2.75
    elif grade == "C+":
        return 2.50
    elif grade == "C":
        return 2.25
    elif grade == "D":
        return 2.00
    else:
        return 0.00

# Run the fixed credit system
if __name__ == "__main__":
    fixed_credit_system()