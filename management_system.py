
# ==========================================
# SMART MANAGEMENT SYSTEM
# Python Menu-Based Project
# ==========================================

records = []


def display_menu():
    print("\n" + "=" * 45)
    print("       SMART MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add New Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Calculate Total")
    print("7. Exit")
    print("=" * 45)


def add_record():
    print("\n--- ADD NEW RECORD ---")

    name = input("Enter name: ")
    amount = float(input("Enter amount: "))

    record = {
        "name": name,
        "amount": amount
    }

    records.append(record)

    print("Record added successfully!")


def view_records():
    print("\n--- ALL RECORDS ---")

    if not records:
        print("No records found.")
        return

    for index, record in enumerate(records, start=1):
        print(
            f"{index}. Name: {record['name']} "
            f"| Amount: {record['amount']:.2f}"
        )


def search_record():
    print("\n--- SEARCH RECORD ---")

    name = input("Enter name to search: ").lower()

    found = False

    for record in records:
        if record["name"].lower() == name:
            print("Record found!")
            print(record)
            found = True

    if not found:
        print("Record not found.")


def update_record():
    print("\n--- UPDATE RECORD ---")

    name = input("Enter name to update: ").lower()

    for record in records:
        if record["name"].lower() == name:

            record["name"] = input("Enter new name: ")
            record["amount"] = float(
                input("Enter new amount: ")
            )

            print("Record updated successfully!")
            return

    print("Record not found.")


def delete_record():
    print("\n--- DELETE RECORD ---")

    name = input("Enter name to delete: ").lower()

    for record in records:
        if record["name"].lower() == name:
            records.remove(record)
            print("Record deleted successfully!")
            return

    print("Record not found.")


def calculate_total():
    total = sum(record["amount"] for record in records)

    print("\n--- TOTAL AMOUNT ---")
    print(f"Total: Rs. {total:.2f}")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    display_menu()

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_record()

        elif choice == 2:
            view_records()

        elif choice == 3:
            search_record()

        elif choice == 4:
            update_record()

        elif choice == 5:
            delete_record()

        elif choice == 6:
            calculate_total()

        elif choice == 7:
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please select 1-7.")

    except ValueError:
        print("Please enter a valid number.")
