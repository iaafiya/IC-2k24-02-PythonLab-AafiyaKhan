"""Q1 - Student database using nested dictionaries."""

students = {
    101: {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chem": 92}},
    102: {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chem": 64}},
    103: {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chem": 69}},
}


def valid_marks(value):
    return 0 <= value <= 100


def add_student():
    try:
        roll = int(input("Roll number: "))
        if roll in students:
            print("Duplicate roll number. Student not added.")
            return
        name = input("Student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        marks = {}
        while True:
            subject = input("Subject name (blank to finish): ").strip()
            if not subject:
                break
            try:
                score = float(input(f"Marks in {subject}: "))
                if not valid_marks(score):
                    print("Marks must be between 0 and 100.")
                    continue
                marks[subject] = score
            except ValueError:
                print("Enter a valid number.")
        students[roll] = {"name": name, "marks": marks}
        print("Student added.")
    except ValueError:
        print("Roll number must be an integer.")


def update_marks():
    try:
        roll = int(input("Roll number: "))
        if roll not in students:
            print("Student not found.")
            return
        subject = input("Subject: ").strip()
        score = float(input("New marks (0-100): "))
        if not valid_marks(score):
            print("Marks must be between 0 and 100.")
            return
        students[roll]["marks"][subject] = score
        print("Marks updated.")
    except ValueError:
        print("Enter a valid roll number and marks.")


def show_record():
    try:
        roll = int(input("Roll number: "))
        if roll not in students:
            print("Student not found.")
        else:
            print(roll, ":", students[roll])
    except ValueError:
        print("Roll number must be an integer.")


def reports():
    if not students:
        print("No student records available.")
        return

    averages = {
        roll: round(sum(record["marks"].values()) / len(record["marks"]), 2)
        if record["marks"] else 0.0
        for roll, record in students.items()
    }
    print("Average marks:", averages)

    topper_roll = max(averages, key=averages.get)
    print("Topper:", students[topper_roll]["name"], f"({averages[topper_roll]})")

    subjects = {subject for record in students.values()
                for subject in record["marks"]}
    highest_by_subject = {}
    for subject in subjects:
        candidates = [
            (record["marks"][subject], record["name"])
            for record in students.values() if subject in record["marks"]
        ]
        if candidates:
            score, name = max(candidates)
            highest_by_subject[subject] = (name, score)
    print("Highest per subject:", highest_by_subject)

    below_40 = {
        record["name"]: {subject: score for subject, score in record["marks"].items()
                         if score < 40}
        for record in students.values()
        if any(score < 40 for score in record["marks"].values())
    }
    print("Below 40 in any subject:", below_40)

    # Grade is based on each student's average.
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for roll, average in averages.items():
        grade = ("A" if average >= 90 else "B" if average >= 75 else
                 "C" if average >= 60 else "D" if average >= 40 else "F")
        grades[grade].append(students[roll]["name"])
    print("Grade-wise grouping:", grades)


def main():
    while True:
        print("\n--- STUDENT DATABASE ---")
        print("1. Add student\n2. Update subject marks\n3. Delete student")
        print("4. Show full record\n5. Reports\n6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            update_marks()
        elif choice == "3":
            try:
                roll = int(input("Roll number to delete: "))
                if students.pop(roll, None) is None:
                    print("Student not found.")
                else:
                    print("Student deleted.")
            except ValueError:
                print("Roll number must be an integer.")
        elif choice == "4":
            show_record()
        elif choice == "5":
            reports()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
