# Python Lab Assignment - Dictionaries

This repository contains solutions for the dictionary-based Python lab assignment.

## Files

| File | Assignment |
|---|---|
| `q1_student_database.py` | Student database using nested dictionaries |
| `q2_employee_database.py` | Employee database, grouping and aggregation |
| `q3_library_record_system.py` | Library issue/return system and rules |
| `q4_word_frequency.py` | Word frequency counter |
| `q5_phone_directory.py` | Phone directory and reverse lookup |
| `part_b_predict_output.py` | Predict-the-output programs |
| `part_c_reasoning.md` | Short reasoning answers |

## Requirements

- Python 3.8 or newer
- No third-party packages are required.

## Run a program

Open a terminal in this folder and run one file at a time:

```bash
python q1_student_database.py
python q2_employee_database.py
python q3_library_record_system.py
python q4_word_frequency.py
python q5_phone_directory.py
python part_b_predict_output.py
```

On Windows, `py filename.py` can be used instead of `python filename.py`.

## Notes

- Q1's grade-wise grouping uses each student's average marks.
- The sample records are preloaded so the expected reports can be checked immediately.
- Menu actions modify the in-memory dictionaries. Changes are not saved to a database or file after the program exits.
- Part B question 6 intentionally demonstrates the `RuntimeError` caused by deleting a dictionary key during direct iteration. Run the file to observe it; because the error stops execution, questions 7 and 8 are best run separately or after commenting out question 6.

## GitHub submission

1. Create/open your Python lab assignment repository on GitHub.
2. Download and extract this project folder.
3. Copy the files into your local repository folder.
4. Open a terminal in that repository folder.
5. Run:

```bash
git status
git add .
git commit -m "Python Lab Assignment - Dictionary Programs"
git push
```

If the repository has not yet been cloned, clone it first using the repository URL:

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholder with your actual GitHub repository URL.
