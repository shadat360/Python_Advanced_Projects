import re

student_grades = {}

def calculate_grade(total):
    if total >= 80:
        return "A+", 4.00, "Outstanding"
    elif total >= 75:
        return "A", 3.75, "Excellent"
    elif total >= 70:
        return "A-", 3.50, "Very Good"
    elif total >= 65:
        return "B+", 3.25, "Good"
    elif total >= 60:
        return "B", 3.00, "Satisfactory"
    elif total >= 55:
        return "B-", 2.75, "Above Average"
    elif total >= 50:
        return "C+", 2.50, "Average"
    elif total >= 45:
        return "C", 2.25, "Below Average"
    elif total >= 40:
        return "D", 2.00, "Pass"
    else:
        return "F", 0.00, "Fail"

def add_student(roll, name, dept, section, semester, marks):
    if roll in student_grades:
        print(f"Roll {roll} already exists!")
    else:
        total = marks["total"]
        grade, gp, remarks = calculate_grade(total)
        student_grades[roll] = {
            "name": name,
            "department": dept,
            "section": section,
            "semester": semester,
            "marks": marks,
            "grade": grade,
            "grade_point": gp,
            "remarks": remarks
        }
        print(f"Added {name} (Roll: {roll})")

def update_student(roll=None):
    while True:
        if not roll:
            roll = input("Enter roll to update (or type 'cancel' to go back): ").strip()
            if roll.lower() == "cancel":
                return
        if roll not in student_grades:
            print("Data not found! Try again.")
            roll = None
            continue

        while True: 
            print(f"\nUpdating marks for {roll} ({student_grades[roll]['name']})")
            print("Which mark do you want to update?")
            print("1. Quiz 1")
            print("2. Quiz 2")
            print("3. Quiz 3")
            print("4. Midterm")
            print("5. Final")
            print("6. Attendance")
            print("7. Assignment")
            print("8. Presentation")
            print("9. Cancel")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Invalid input! Please enter a number between 1 to 9.")
                continue

            marks = student_grades[roll]["marks"]

            if choice in [1, 2, 3]:
                while True:
                    try:
                        q_mark = float(input(f"Enter new Quiz {choice} mark (out of 15): "))
                        if q_mark > 15:
                            print("Quiz mark cannot exceed 15!")
                        else:
                            quizzes = [marks.get("Quiz1", marks["Quiz Average"]),
                                       marks.get("Quiz2", marks["Quiz Average"]),
                                       marks.get("Quiz3", marks["Quiz Average"])]
                            quizzes[choice-1] = q_mark
                            marks["Quiz1"] = quizzes[0]
                            marks["Quiz2"] = quizzes[1]
                            marks["Quiz3"] = quizzes[2]
                            marks["Quiz Average"] = sum(quizzes)/3
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif choice == 4:
                while True:
                    try:
                        mid = float(input("Enter new Midterm mark (out of 25): "))
                        if mid > 25:
                            print("Midterm cannot exceed 25!")
                        else:
                            marks["Mid"] = mid
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif choice == 5:
                while True:
                    try:
                        final = float(input("Enter new Final mark (out of 40): "))
                        if final > 40:
                            print("Final cannot exceed 40!")
                        else:
                            marks["Final"] = final
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif choice == 6:
                while True:
                    try:
                        att = float(input("Enter new Attendance mark (out of 7): "))
                        if att > 7:
                            print("Attendance cannot exceed 7!")
                        else:
                            marks["Attendance"] = att
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif choice == 7:
                while True:
                    try:
                        assign = float(input("Enter new Assignment mark (out of 5): "))
                        if assign > 5:
                            print("Assignment cannot exceed 5!")
                        else:
                            marks["Assignment"] = assign
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif choice == 8:
                while True:
                    try:
                        pres = float(input("Enter new Presentation mark (out of 8): "))
                        if pres > 8:
                            print("Presentation cannot exceed 8!")
                        else:
                            marks["Presentation"] = pres
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif choice == 9:
                print("Update cancelled!")
                return

            else:
                print("Invalid choice! Please enter between 1 to 9.")
                continue

            total = marks["Quiz Average"] + marks["Mid"] + marks["Final"] + marks["Attendance"] + marks["Assignment"] + marks["Presentation"]
            marks["total"] = total
            grade, gp, remarks = calculate_grade(total)
            student_grades[roll]["grade"] = grade
            student_grades[roll]["grade_point"] = gp
            student_grades[roll]["remarks"] = remarks

            print(f"Updated {roll} successfully.")
            return

def delete_student():
    while True:
        roll = input("Enter roll to delete (or type 'cancel' to go back): ").strip()
        if roll.lower() == "cancel":
            return
        if roll in student_grades:
            del student_grades[roll]
            print(f"Deleted roll {roll}")
            return
        else:
            print("Roll not found! Try again.")

def display_all_students():
    if student_grades:
        for roll, info in student_grades.items():
            print_student_info(roll, info)
    else:
        print("No students added yet!")

def display_single_student(roll):
    if roll in student_grades:
        info = student_grades[roll]
        print_student_info(roll, info)
    else:
        print("Roll not found!")

def print_student_info(roll, info):
    print(f"\nRoll: {roll}, Name: {info['name']}")
    print(f"Dept: {info['department']}, Section: {info['section']}, Semester: {info['semester']}")
    print(f"Total Marks (100): {info['marks']['total']}")
    print(f"Grade: {info['grade']}, CGPA: {info['grade_point']}, Remarks: {info['remarks']}")
    for key, val in info["marks"].items():
        if key != "total":
            print(f"{key} = {val}")

def input_semester():
    while True:
        print("Choose Semester:")
        print("1. Fall")
        print("2. Summer")
        print("3. Spring")
        try:
            sem_choice = int(input("Enter choice: "))
            if sem_choice == 1:
                sem = "Fall"
            elif sem_choice == 2:
                sem = "Summer"
            elif sem_choice == 3:
                sem = "Spring"
            else:
                print("Invalid choice!")
                continue
        except ValueError:
            print("Enter a number between 1 to 3!")
            continue
        break

    while True:
        try:
            year = int(input("Enter year : "))
            if 2000 <= year <= 2100:
                break
            else:
                print("Enter a valid year between 2000 and 2100!")
        except ValueError:
            print("Invalid year!")

    return f"{sem}-{year}"

def input_marks():
    marks = {}

    quizzes = []
    for i in range(1, 4):
        while True:
            try:
                q = float(input(f"Enter Quiz {i} mark (out of 15): "))
                if q > 15:
                    print("Quiz mark cannot exceed 15!")
                else:
                    quizzes.append(q)
                    break
            except ValueError:
                print("Invalid input!")
    marks["Quiz1"] = quizzes[0]
    marks["Quiz2"] = quizzes[1]
    marks["Quiz3"] = quizzes[2]
    marks["Quiz Average"] = sum(quizzes)/3

    while True:
        try:
            mid = float(input("Enter Midterm mark (out of 25): "))
            if mid > 25:
                print("Midterm cannot exceed 25!")
            else:
                marks["Mid"] = mid
                break
        except ValueError:
            print("Invalid input!")

    while True:
        try:
            final = float(input("Enter Final mark (out of 40): "))
            if final > 40:
                print("Final cannot exceed 40!")
            else:
                marks["Final"] = final
                break
        except ValueError:
            print("Invalid input!")

    while True:
        try:
            att = float(input("Enter Attendance mark (out of 7): "))
            if att > 7:
                print("Attendance cannot exceed 7!")
            else:
                marks["Attendance"] = att
                break
        except ValueError:
            print("Invalid input!")

    while True:
        try:
            assign = float(input("Enter Assignment mark (out of 5): "))
            if assign > 5:
                print("Assignment cannot exceed 5!")
            else:
                marks["Assignment"] = assign
                break
        except ValueError:
            print("Invalid input!")

    while True:
        try:
            pres = float(input("Enter Presentation mark (out of 8): "))
            if pres > 8:
                print("Presentation cannot exceed 8!")
            else:
                marks["Presentation"] = pres
                break
        except ValueError:
            print("Invalid input!")

    total = marks["Quiz Average"] + marks["Mid"] + marks["Final"] + marks["Attendance"] + marks["Assignment"] + marks["Presentation"]
    marks["total"] = total

    return marks

def input_student_details():
    while True:
        roll = input("Enter roll (NNN-NN-NNN or NNN-NN-NNNN): ").strip()
        if not re.fullmatch(r"\d{3}-\d{2}-\d{3,4}", roll):
            print("Invalid roll format!")
            continue
        if roll in student_grades:
            print(f"Roll {roll} already exists! Try another.")
            continue
        break

    name = input("Enter name: ").strip()
    dept = input("Enter department(Only 'CSE' allowed): ").strip().upper()
    if dept != "CSE":
        print("Only 'CSE' allowed! Set to CSE.")
    dept = "CSE"

    while True:
        section = input("Enter section (example: 60-A): ").strip()
        if re.match(r"^\d{1,3}-[A-Za-z]$", section):
            section = section.upper()
            break
        else:
            print("Invalid section!")

    semester = input_semester()
    marks = input_marks()

    return roll, name, dept, section, semester, marks

def main():
    while True:
        print("\n____Student Grade Management System____")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            roll, name, dept, section, semester, marks = input_student_details()
            add_student(roll, name, dept, section, semester, marks)

        elif choice == 2:
            update_student()

        elif choice == 3:
            delete_student()

        elif choice == 4:
            while True:
                print("\nView Options:")
                print("1. View All Students")
                print("2. View Single Student by Roll")
                print("3. Back")
                try:
                    view_choice = int(input("Enter choice: "))
                except ValueError:
                    print("Invalid input!")
                    continue

                if view_choice == 1:
                    display_all_students()
                elif view_choice == 2:
                    roll = input("Enter roll to view: ").strip()
                    display_single_student(roll)
                elif view_choice == 3:
                    break
                else:
                    print("Invalid choice!")

        elif choice == 5:
            print("Exiting.....")
            break
        else:
            print("Invalid choice!")

main()
