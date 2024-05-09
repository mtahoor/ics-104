# Function to read manager data from manager.txt
def read_manager_data():
    manager_data = {}
    with open("manager.txt", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            manager_data[fields[0]] = {"name": fields[1], "password": fields[2]}
    return manager_data

# Function to validate manager credentials
def validate_manager_login(manager_data, manager_id, password):
    if manager_id in manager_data:
        if manager_data[manager_id]["password"] == password:
            return True
    return False


# Function to view food demand for a specific date
def view_food_demand():
    date=input()
    print("Display Food Demand")
    print("Date            Item            Quantity")
    print("----------------------------------------")
    try:
        with open("FOODDEMAND.txt", "r") as file:
            lines = file.readlines()
            found_date = False
            for line in lines:
                if line.strip() == date:
                    found_date = True
                elif found_date and line.strip() == "":
                    break
                elif found_date:
                    parts = line.strip().split("\t")
                    print(f"{parts[0]}{' '*(15-len(parts[0]))}{parts[1]}{' '*(15-len(parts[1]))}{parts[2]}")
    except FileNotFoundError:
        print("FOODDEMAND.txt not found. Make sure the file exists.")
# Main function for Manager Menu
def manager_menu():
    while True:
        print("\n1. View Food Demand")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_food_demand()
        elif choice == '2':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function for Manager Login
def manager_login():
    manager_data = read_manager_data()
    
    print("Welcome to KFUPM Restaurant Management System")
    print("Manager Login")
    
    manager_id = input("Enter your ID: ")
    password = input("Enter your password: ")
    
    if validate_manager_login(manager_data, manager_id, password):
        print("Login successful!")
        manager_menu()  # After successful login, show the manager menu
    else:
        print("Invalid ID or password. Please try again.")

# Test the manager login function
manager_login()
