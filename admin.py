# Function to display all food items
def display_food_items():
    print("List of Food Items:")
    print("ID\tName\t\tPrice (SAR)")
    print("-" * 30)
    try:
        with open("fooditems.txt", "r") as file:
            for line in file:
                fields = line.strip().split(" ")
                item_id = fields[0]
                name = " ".join(fields[1:-1])
                price = fields[-1]
                print(f"{item_id}\t{name.ljust(16)}\t{price}")
    except FileNotFoundError:
        print("No food items found.")
# Function to update a food item
def update_food_item():
    display_food_items()
    item_id = input("Enter item ID to update: ")
    new_name = input("Enter new item name (press Enter to keep the current name): ").strip()
    new_price_str = input("Enter new item price (SAR) (press Enter to keep the current price): ").strip()

    try:
        new_price = float(new_price_str) if new_price_str else None

        updated_data = []
        with open("fooditems.txt", "r") as file:
            for line in file:
                fields = line.strip().split(" ")
                if fields[0] == item_id:
                    if new_name:
                        fields[1] = new_name
                    if new_price is not None:
                        fields[2] = str(new_price)
                    updated_data.append(" ".join(fields) + "\n")
                else:
                    updated_data.append(line)

        with open("fooditems.txt", "w") as file:
            file.writelines(updated_data)

        print("Food item updated successfully!")
    except ValueError:
        print("Invalid price. Please enter a valid number.")

# Function to delete a food item
def delete_food_item():
    display_food_items()
    item_id = input("Enter item ID to delete: ")

    updated_data = []
    with open("fooditems.txt", "r") as file:
        for line in file:
            fields = line.strip().split(" ")
            if fields[0] != item_id:
                updated_data.append(line)

    with open("fooditems.txt", "w") as file:
        file.writelines(updated_data)

    print("Food item deleted successfully!")
# Function to add a new food item
def add_new_food_item():
    try:
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        price = float(input("Enter item price (SAR): "))

        with open("fooditems.txt", "a") as file:
            file.write(f"{item_id} {name} {price}\n")

        print("New food item added successfully!")
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        
# Function to delete a manager by ID
def delete_manager():
    display_managers()
    manager_id = input("Enter manager ID to delete: ")

    # Read existing manager data
    updated_data = []
    try:
        with open("manager.txt", "r") as file:
            for line in file:
                fields = line.strip().split("\t")
                if fields[0] != manager_id:
                    updated_data.append(line)

        # Write updated manager data back to manager.txt
        with open("manager.txt", "w") as file:
            file.writelines(updated_data)

        print("Manager information deleted successfully!")
    except FileNotFoundError:
        print("manager.txt not found. Make sure the file exists.")
# Function to delete a student by ID
def delete_student():
    display_students()
    student_id = input("Enter student ID to delete: ")

    # Read existing student data
    updated_data = []
    try:
        with open("student.txt", "r") as file:
            for line in file:
                fields = line.strip().split("\t")
                if fields[0] != student_id:
                    updated_data.append(line)

        # Write updated student data back to student.txt
        with open("student.txt", "w") as file:
            file.writelines(updated_data)

        print("Student information deleted successfully!")
    except FileNotFoundError:
        print("student.txt not found. Make sure the file exists.")
# Function to display list of all managers
def display_managers():
    print("List of Managers:")
    try:
        with open("manager.txt", "r") as file:
            for line in file:
                manager_id, name, password = line.strip().split("\t")
                print(f"ID: {manager_id}, Name: {name}, Password: {password}")
    except FileNotFoundError:
        print("manager.txt not found. Make sure the file exists.")

# Function to update manager information
def update_manager():
    display_managers()
    manager_id = input("Enter manager ID: ")

    # Read existing manager data
    updated_data = []
    try:
        with open("manager.txt", "r") as file:
            for line in file:
                fields = line.strip().split("\t")
                if fields[0] == manager_id:
                    name = input(f"Enter name (if you don't want to update this field press enter key): ")
                    password = input(f"Enter password (if you don't want to update this field press enter key): ")

                    # If name or password is empty, keep the existing value
                    if name == "":
                        name = fields[1]
                    if password == "":
                        password = fields[2]

                    updated_data.append(f"{manager_id}\t{name}\t{password}\n")
                else:
                    updated_data.append(line)

        # Write updated manager data back to manager.txt
        with open("manager.txt", "w") as file:
            file.writelines(updated_data)

        print("MANAGER information updated successfully!")
    except FileNotFoundError:
        print("manager.txt not found. Make sure the file exists.")
# Function to display list of all students
def display_students():
    print("List of Students:")
    try:
        with open("student.txt", "r") as file:
            for line in file:
                student_id, name, password = line.strip().split("\t")
                print(f"ID: {student_id}, Name: {name}, Password: {password}")
    except FileNotFoundError:
        print("student.txt not found. Make sure the file exists.")

# Function to update student information
def update_student():
    display_students()
    student_id = input("Enter user ID: ")

    # Read existing student data
    updated_data = []
    try:
        with open("student.txt", "r") as file:
            for line in file:
                fields = line.strip().split("\t")
                if fields[0] == student_id:
                    name = input(f"Enter name (if you don't want to update this field press enter key): ")
                    password = input(f"Enter password (if you don't want to update this field press enter key): ")

                    # If name or password is empty, keep the existing value
                    if name == "":
                        name = fields[1]
                    if password == "":
                        password = fields[2]

                    updated_data.append(f"{student_id}\t{name}\t{password}\n")
                else:
                    updated_data.append(line)

        # Write updated student data back to student.txt
        with open("student.txt", "w") as file:
            file.writelines(updated_data)

        print("STUDENT information updated successfully!")
    except FileNotFoundError:
        print("student.txt not found. Make sure the file exists.")
# Function to add a new manager
def add_new_manager():
    print("Add a New Manager")
    manager_id = input("Enter the manager ID: ")
    name = input("Enter the manager name: ")
    password = input("Enter the manager password: ")

    # Write manager data to manager.txt
    with open("manager.txt", "a") as file:
        file.write(f"{manager_id}\t{name}\t{password}\n")

    print("New manager added successfully.")
# Function to add a new student
def add_new_student():
    print("Add a New Student")
    student_id = input("Enter the student ID: ")
    name = input("Enter the student name: ")
    password = input("Enter the student password: ")
    account_number = input("Enter the student's bank account number: ")

    # Write student data to student.txt
    with open("student.txt", "a") as file:
        file.write(f"{student_id}\t{name}\t{password}\n")

    # Write account number to studentbank.txt
    with open("studentbank.txt", "a") as file:
        file.write(f"{student_id}\t{account_number}\n")

    print("New student added successfully.")

# Main function for Admin Menu
def admin_menu():
     while True:
        print("\n1. Add a New Student")
        print("2. Add a New Manager")
        print("3. Update a Student")
        print("4. Update a Manager")
        print("5. Delete a Student")
        print("6. Delete a Manager")
        print("7. Add a New Food Item")
        print("8. Update a Food Item")
        print("9. Delete a Food Item")
        print("10. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_student()
        elif choice == '2':
            add_new_manager()
        elif choice == '3':
            update_student()
        elif choice == '4':
            update_manager()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            delete_manager()
        elif choice == '7':
            add_new_food_item()
        elif choice == '8':
            update_food_item()
        elif choice == '9':
            delete_food_item()
        elif choice == '10':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
# Function to read admin data from ADMINISTER.txt
def read_admin_data():
    admin_data = {}
    try:
        with open("ADMINISTER.txt", "r") as file:
            for line in file:
                fields = line.strip().split("\t")
                admin_data[fields[0]] = {"name": fields[1], "password": fields[2]}
    except FileNotFoundError:
        print("ADMINISTER.txt not found. Make sure the file exists.")
    return admin_data

# Function to validate admin credentials
def validate_admin_login(admin_data, admin_id, password):
    if admin_id in admin_data:
        print('heehe')
        if admin_data[admin_id]["password"] == password:
            return True
    return False

# Main function for Admin Login
def admin_login():
    admin_data = read_admin_data()
    
    print("Welcome to KFUPM Restaurant Management System")
    print("Admin Login")
    
    admin_id = input("Enter your ID: ")
    password = input("Enter your password: ")
    
    if validate_admin_login(admin_data, admin_id, password):
        print("Login successful!")
        admin_menu()  # After successful login, show the admin menu
    else:
        print("Invalid ID or password. Please try again.")

# Test the admin login function
admin_login()
