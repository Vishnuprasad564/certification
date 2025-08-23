students = {}

def show_menu():
    print("\n=== Student Database Menu ===")
    print("1. Add student")
    print("2. Update student")
    print("3. Remove student")
    print("4. View all students")
    print("5. Search student by roll number")
    print("6. Show total number of students")
    print("7. Exit")


def addstudent(db):
    roll = input("Enter roll no: ")
    if roll in db:
        print("Roll no aleready exists")
        return
    name = input("Enter name: ")
    db[roll] = name
    print(f"Added: {roll} -> {name}")

def updateDetails(db):
    roll = input("Enter roll no to update: ")

    if roll in db:
        name = input("Enter new name: ")
        db[roll] = name
        print(f"Updated: {roll} -> {name}")

    else:
        print("Roll no not found")
def removestudent(db):
    roll = input("Enter roll no to be deleted")
    removed = db.pop(roll,None)
    if removed is None:
        print("student not found")

    else:
        print(f"Removed: {roll} ->{removed}")

def viewall(db):
    if db:
        print("\n All students: ")
        for roll,name in db.items():
            print(f"{roll}: {name}")

    else:
        print("Database is empty.")

def searchStudent(db):
    roll = input("Enter roll no to search")
    if roll in db:
        print(f"Found: {roll} -> {db[roll]}")
    else:
        print("Roll no not found")

def count(db):
    print(f"Total students: {len(db)}")

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        addstudent(students)

    elif choice == "2":
        updateDetails(students)
    elif choice == "3":
        removestudent(students)

    elif choice == "4":
        viewall(students)

    elif choice == "5":
        searchStudent(students)

    elif choice == "6":
        count(students)

    elif choice == "7":
        print("Thenks")
        break
    else:
        print("Invalid choice")



