import pandas as pd

def add_students():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        sid = int(input("ID: "))
        name = input("Name: ")
        math = int(input("Math marks: "))
        science = int(input("Science marks: "))
        english = int(input("English marks: "))

        students.append([sid, name, math, science, english])

    columns = ["ID", "Name", "Math", "Science", "English"]
    df = pd.DataFrame(students, columns=columns)

    return df


def update_student(df):
    choice = input("\nDo you want to update any student? (yes/no): ")

    if choice.lower() == "yes":
        update_id = int(input("Enter student ID to update: "))

        if update_id in df["ID"].values:
            new_math = int(input("Enter new Math marks: "))
            new_science = int(input("Enter new Science marks: "))
            new_english = int(input("Enter new English marks: "))

            df.loc[df["ID"] == update_id, ["Math", "Science", "English"]] = [
                new_math, new_science, new_english
            ]

            print("Record updated successfully!\n")
        else:
            print("Student ID not found!\n")

    return df


def main():
    df = add_students()

    df = update_student(df)

    df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
    df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 60 else "Fail")

    df.to_excel("students.xlsx", index=False)

    print("\nFinal Student Records:\n")
    print(df.to_string(index=False))

    print(f"\nTotal Students: {len(df)}")
    print("Excel file created successfully!")


if __name__ == "__main__":
    main()