"""Q2 - Employee database: grouping, aggregation and dictionary comprehension."""

employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000},
}


def add_employee():
    emp_id = input("Employee ID: ").strip()
    if emp_id in employees:
        print("Duplicate employee ID.")
        return
    name = input("Name: ").strip()
    dept = input("Department: ").strip()
    try:
        salary = float(input("Salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
        employees[emp_id] = {"name": name, "dept": dept, "salary": salary}
        print("Employee added.")
    except ValueError:
        print("Enter a valid salary.")


def update_salary():
    emp_id = input("Employee ID: ").strip()
    if emp_id not in employees:
        print("Employee not found.")
        return
    try:
        salary = float(input("New salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
        employees[emp_id]["salary"] = salary
        print("Salary updated.")
    except ValueError:
        print("Enter a valid salary.")


def reports():
    if not employees:
        print("No employee records.")
        return

    # One pass: each department stores [total payroll, headcount].
    department_totals = {}
    for employee in employees.values():
        dept = employee["dept"]
        summary = department_totals.setdefault(dept, [0, 0])
        summary[0] += employee["salary"]
        summary[1] += 1
    print("Department payroll and headcount:")
    for dept, (payroll, count) in department_totals.items():
        print(f"{dept}: payroll={payroll:.2f}, headcount={count}")

    highest_paid = {}
    for employee in employees.values():
        dept = employee["dept"]
        if (dept not in highest_paid or
                employee["salary"] > highest_paid[dept]["salary"]):
            highest_paid[dept] = employee
    print("Highest paid per department:", {
        dept: (person["name"], person["salary"])
        for dept, person in highest_paid.items()
    })

    print("Employees by salary (high to low):")
    for emp_id, person in sorted(
            employees.items(), key=lambda item: item[1]["salary"], reverse=True):
        print(emp_id, person)

    # Build a separate dictionary so the original salaries and records stay unchanged.
    # The inner dict copy prevents the raised salary from changing the original record.
    raised_employees = {
        emp_id: {**person, "salary": round(person["salary"] * 1.10, 2)}
        if person["salary"] < 50000 else person.copy()
        for emp_id, person in employees.items()
    }
    print("New dictionary after 10% raise below 50000:")
    for person in raised_employees.values():
        if person["salary"] != employees[
                next(k for k, v in employees.items() if v["name"] == person["name"])
        ]["salary"]:
            print(person["name"], person["salary"])
    print("Original salaries remain:", {
        person["name"]: person["salary"] for person in employees.values()
    })

    averages = {
        dept: payroll / count
        for dept, (payroll, count) in department_totals.items()
    }
    best_dept = max(averages, key=averages.get)
    print("Department with highest average salary:",
          best_dept, averages[best_dept])


def main():
    while True:
        print("\n--- EMPLOYEE DATABASE ---")
        print("1. Add\n2. Update salary\n3. Delete\n4. Search by ID\n5. Reports\n6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            update_salary()
        elif choice == "3":
            emp_id = input("Employee ID to delete: ").strip()
            if employees.pop(emp_id, None) is None:
                print("Employee not found.")
            else:
                print("Employee deleted.")
        elif choice == "4":
            emp_id = input("Employee ID: ").strip()
            print(employees.get(emp_id, "Employee not found"))
        elif choice == "5":
            reports()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
