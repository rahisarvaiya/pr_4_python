# Student Performance Analyzer

## Description
A Python console application that analyzes exam scores using built-in functions, sorting algorithms, logical quantifiers (`all`/`any`), and grade categorization.

## Features
- Computes total students, highest, lowest, and average marks.
- Determines pass/fail statistics and pass percentages.
- Generates ascending/descending sorted lists and identifies second highest/lowest marks.
- Evaluates class performance using `all()` and `any()`.
- Includes interactive mark lookup and grade distribution breakdowns.

## How to Run
1. Ensure Python 3.x is installed.
2. Clone the repository.
3. Run: `python student_performance_analyzer.py`

## Sample Output
```text
============================================================
Welcome to the Student Performance Analyzer!
============================================================
Total Students: 20
Highest Marks: 98
Lowest Marks: 21
Average Marks: 68.4
Passed: 17
Failed: 3
Pass Percentage: 85.0%
Scored Exactly 100: 0

Sorted Marks (Ascending): [21, 35, 40, 45, 50, 55, 60, 62, 68, 74, 76, 78, 79, 82, 85, 88, 90, 92, 95, 98]
Sorted Marks (Descending): [98, 95, 92, 90, 88, 85, 82, 79, 78, 76, 74, 68, 62, 60, 55, 50, 45, 40, 35, 21]
Second Highest Marks: 95
Second Lowest Marks: 35
Did all students pass? False
Did any student fail? True

--- Mark Search ---
Enter a mark to search in the list: 88
Mark 88 exists in the records (found 1 time(s)).

--- Grade Distribution ---
Grade A (>=90): 4 Students
Grade B (80-89): 4 Students
Grade C (70-79): 4 Students
Grade D (60-69): 3 Students
Grade E (40-59): 2 Students
Grade F (<40): 3 Students

Author
Rahi Sarvaiya
