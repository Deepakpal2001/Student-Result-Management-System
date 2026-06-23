students = {}

while True:
    print("\n===== Student Result Management System =====")
    print("1. Admin Login")
    print("2. Student Result")
    print("3. Exit")

    choice = input("Enter choice: ")

    # Admin Side
    if choice == "1":
        password = input("Enter Admin Password: ")

        if password == "admin123":

            while True:
                print("\n--- Admin Menu ---")
                print("1. Add Student")
                print("2. View All Students")
                print("3. Back")

                admin_choice = input("Enter choice: ")

                if admin_choice == "1":
                    roll = input("Enter Roll No: ")
                    name = input("Enter Name: ")

                    m1 = int(input("Enter Marks Subject 1: "))
                    m2 = int(input("Enter Marks Subject 2: "))
                    m3 = int(input("Enter Marks Subject 3: "))
                    m4 = int(input("Enter Marks Subject 4: "))
                    m5 = int(input("Enter Marks Subject 5: "))

                    total = m1 + m2 + m3 + m4 + m5
                    percentage = total / 5

                    # Grade
                    if percentage >= 90:
                        grade = "A+"
                    elif percentage >= 80:
                        grade = "A"
                    elif percentage >= 70:
                        grade = "B"
                    elif percentage >= 60:
                        grade = "C"
                    else:
                        grade = "Fail"

                    # Division
                    if percentage >= 60:
                        division = "First"
                    elif percentage >= 45:
                        division = "Second"
                    elif percentage >= 33:
                        division = "Third"
                    else:
                        division = "Fail"

                    students[roll] = {
                        "name": name,
                        "percentage": percentage,
                        "grade": grade,
                        "division": division
                    }

                    print("Student Added Successfully!")

                elif admin_choice == "2":
                    rank = 1

                    sorted_students = sorted(
                        students.items(),
                        key=lambda x: x[1]["percentage"],
                        reverse=True
                    )

                    for roll, data in sorted_students:
                        print("\nRank:", rank)
                        print("Roll No:", roll)
                        print("Name:", data["name"])
                        print("Percentage:", round(data["percentage"], 2))
                        print("Grade:", data["grade"])
                        print("Division:", data["division"])
                        rank += 1

                elif admin_choice == "3":
                    break

        else:
            print("Wrong Password!")

    # Student Side
    elif choice == "2":
        roll = input("Enter Roll No: ")

        if roll in students:

            sorted_students = sorted(
                students.items(),
                key=lambda x: x[1]["percentage"],
                reverse=True
            )

            rank = 1
            for r, data in sorted_students:
                if r == roll:
                    print("\n===== RESULT =====")
                    print("Name:", data["name"])
                    print("Percentage:", round(data["percentage"], 2))
                    print("Grade:", data["grade"])
                    print("Division:", data["division"])
                    print("Rank:", rank)
                    break
                rank += 1

        else:
            print("Student Not Found!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")