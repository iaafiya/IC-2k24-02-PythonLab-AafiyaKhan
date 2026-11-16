
🐍 Python Dictionary-Based Applications

A collection of five Python programs demonstrating the practical implementation of dictionaries, nested dictionaries, dictionary methods, comprehensions, searching, sorting, aggregation, and input validation.

Each program solves a real-world problem using Python data structures and follows the requirements of the assigned practical work.

🎯 Project Objectives

- Understand dictionaries and nested dictionaries.
- Perform CRUD operations (Create, Read, Update, Delete).
- Use dictionary methods such as ".get()", ".setdefault()", and ".update()".
- Apply dictionary and list comprehensions.
- Perform grouping, filtering, sorting, and aggregation.
- Validate user input and handle invalid operations safely.
- Generate meaningful reports from stored data.

📂 Programs Included

1. Student Database

Concepts: Nested Dictionaries, Validation, Comprehensions, and Reports.

Features:

- Add, update, delete, and search student records.
- Store student names and subject-wise marks.
- Reject duplicate roll numbers.
- Validate marks within the range of 0–100.
- Calculate individual student averages.
- Identify the overall topper and subject-wise highest scorers.
- Find students scoring below 40 in any subject.
- Group students according to grades (A, B, C, D, and F).

2. Employee Database

Concepts: Dictionary Operations, Grouping, Aggregation, Sorting, and Comprehensions.

Features:

- Add, update salary, delete, and search employees.
- Calculate department-wise payroll and employee count.
- Identify the highest-paid employee in each department.
- Sort employees by salary in descending order.
- Generate a new dictionary applying a 10% raise to employees earning below ₹50,000.
- Identify the department with the highest average salary.
- Handle missing employee records appropriately.

3. Library Record System

Concepts: Nested Dictionaries, Lists, State Management, and Validation.

Features:

- Add books and increase copies for existing ISBNs.
- Issue and return books.
- Track members holding each book.
- Enforce book availability.
- Restrict members to a maximum of two books.
- Prevent duplicate issues and invalid returns.
- Search for books and generate library reports.
- Find books by author, unavailable books, never-issued books, and members holding multiple books.

4. Word Frequency Counter

Concepts: String Processing, Dictionaries as Counters, Sorting, and Comprehensions.

Features:

- Accept a paragraph from the user.
- Convert text to lowercase and remove punctuation.
- Count word frequencies using ".get()".
- Display the top N most frequent words, breaking ties alphabetically.
- Find words appearing exactly once.
- Invert the frequency dictionary.
- Group unique words according to their length.
- Search for words safely, even when they are absent.
- Handle empty input gracefully.

5. Phone Directory

Concepts: Dictionaries with List Values, Reverse Lookup, Validation, and Grouping.

Features:

- Add and delete contacts.
- Add multiple phone numbers to existing contacts.
- Update email addresses and cities.
- Validate phone numbers as exactly 10 digits.
- Prevent duplicate phone numbers across contacts.
- Perform case-insensitive partial-name searches.
- Build a reverse phone lookup dictionary.
- Group contacts by city.
- Find contacts with multiple phone numbers.
- Display the directory alphabetically.

🛠️ Technologies Used

Technology| Description
Language| Python 3.x
Data Structures| Dictionaries, Nested Dictionaries, Lists
Concepts| CRUD Operations, Comprehensions, Loops, Conditions
Tools| VS Code, Git, GitHub

📁 Project Structure

Python-Dictionary-Applications/
│
├── student_database.py
├── employee_database.py
├── library_record_system.py
├── word_frequency_counter.py
├── phone_directory.py
│
└── README.md

▶️ How to Run

Prerequisites

- Install Python 3.x.
- Install VS Code or any Python-supported code editor.
- Clone or download this repository.

Step 1: Clone the Repository

git clone YOUR_REPOSITORY_URL

Step 2: Open the Project Folder

cd Python-Dictionary-Applications

Step 3: Run a Program

Execute any program using:

python student_database.py

Replace "student_database.py" with the filename of the program you want to execute.

🧪 Testing and Validation

The programs are designed to handle different test cases, including:

- Valid and invalid user inputs.
- Duplicate student IDs, employee IDs, ISBNs, and phone numbers.
- Missing records during search, update, or deletion.
- Boundary values such as marks of 0 and 100.
- Library issue and return restrictions.
- Empty paragraphs and words that are not found.
- Reports generated using sample data.

📚 Learning Outcomes

After completing these programs, the following concepts can be understood and implemented:

- Designing and manipulating nested dictionary structures.
- Implementing menu-driven Python applications.
- Performing CRUD operations using dictionaries.
- Applying comprehensions to transform and filter data.
- Performing searches and generating reports.
- Using sorting, grouping, and aggregation techniques.
- Enforcing business rules through input validation.
- Handling common edge cases without unexpected program termination.

👩‍💻 Author

Aafiya Khan
