import pandas as pd

def create_excel_file():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        name = input("Name: ")
        math = int(input("Math marks: "))
        science = int(input("Science marks: "))
        english = int(input("English marks: "))

        students.append({
            'name': name,
            'Math': math,
            'Science': science,
            'English': english
        })

    df = pd.DataFrame(students)

    df.to_excel("students.xlsx", index=False)
    print("\nExcel file created successfully.\n")


def count_students_with_high_average(df):
    count = 0

    for index, row in df.iterrows():
        name = row['name']
        scores = row.drop('name')
        average = scores.mean()

        if average > 60:
            count += 1
            print(f"{name} has an average score of {average:.2f}")

    return count


def display_students(df):
    print("Students' Scores:")
    print("-" * 50)
    print(df.to_string(index=False))


def main():
    create_excel_file()

    df = pd.read_excel("students.xlsx")

    display_students(df)

    print("\n" + "=" * 50)
    print("Students with average score greater than 60:")
    print("=" * 50)

    result = count_students_with_high_average(df)

    print("\n" + "-" * 50)
    print(f"Total students with average > 60: {result}")
    print(f"Total students: {len(df)}")


if __name__ == "__main__":
    main()