def main():
    marks = [45, 78, 92, 35, 60, 88, 76, 95, 40, 55, 68, 82, 90, 21, 74, 85, 98, 50, 62, 79]

    print("=" * 60)
    print("Welcome to the Student Performance Analyzer!")
    print("=" * 60)

    total_students = len(marks)
    highest_marks = max(marks)
    lowest_marks = min(marks)
    average_marks = sum(marks) / total_students

    passed_students = [m for m in marks if m >= 40]
    failed_students = [m for m in marks if m < 40]
    num_passed = len(passed_students)
    num_failed = len(failed_students)
    
    exact_100 = marks.count(100)

    pass_percentage = (num_passed / total_students) * 100

    print(f"Total Students: {total_students}")
    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Average Marks: {average_marks:.1f}")
    print(f"Passed: {num_passed}")
    print(f"Failed: {num_failed}")
    print(f"Pass Percentage: {pass_percentage:.1f}%")
    print(f"Scored Exactly 100: {exact_100}")

    sorted_asc = sorted(marks)
    sorted_desc = sorted(marks, reverse=True)
    print(f"\nSorted Marks (Ascending): {sorted_asc}")
    print(f"Sorted Marks (Descending): {sorted_desc}")

    unique_sorted = sorted(list(set(marks)))
    second_highest = unique_sorted[-2] if len(unique_sorted) >= 2 else unique_sorted[-1]
    second_lowest = unique_sorted[1] if len(unique_sorted) >= 2 else unique_sorted[0]
    print(f"Second Highest Marks: {second_highest}")
    print(f"Second Lowest Marks: {second_lowest}")

    all_passed = all(m >= 40 for m in marks)
    any_failed = any(m < 40 for m in marks)
    print(f"Did all students pass? {all_passed}")
    print(f"Did any student fail? {any_failed}")

    print("\n--- Mark Search ---")
    try:
        search_mark = int(input("Enter a mark to search in the list: "))
        if search_mark in marks:
            print(f"Mark {search_mark} exists in the records (found {marks.count(search_mark)} time(s)).")
        else:
            print(f"Mark {search_mark} was not found in the student records.")
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        print('')

    print("\n--- Grade Distribution ---")
    grade_a = sum(1 for m in marks if m >= 90)
    grade_b = sum(1 for m in marks if 80 <= m <= 89)
    grade_c = sum(1 for m in marks if 70 <= m <= 79)
    grade_d = sum(1 for m in marks if 60 <= m <= 69)
    grade_e = sum(1 for m in marks if 40 <= m <= 59)
    grade_f = sum(1 for m in marks if m < 40)

    print(f"Grade A (>=90): {grade_a} Students")
    print(f"Grade B (80-89): {grade_b} Students")
    print(f"Grade C (70-79): {grade_c} Students")
    print(f"Grade D (60-69): {grade_d} Students")
    print(f"Grade E (40-59): {grade_e} Students")
    print(f"Grade F (<40): {grade_f} Students")

if __name__ == "__main__":
    main()