# Function to read student data from student.txt
def read_student_data():
    student_data = {}
    with open("student.txt", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            student_data[fields[0]] = {"name": fields[1], "password": fields[2]}
    return student_data

# Function to validate student credentials
def validate_student_login(student_data, student_id, password):
    if student_id in student_data:
        if student_data[student_id]["password"] == password:
            return True
    return False

# Function to read available food items from FOODITEMS.txt
def read_food_items():
    food_items = {}
    try:
        with open("fooditems.txt", "r") as file:
            for line in file:
                fields = line.strip().split(" ")
                try:
                    item_id = int(fields[0])
                    name = " ".join(fields[1:-1])
                    price = float(fields[-1])
                    food_items[item_id] = {"name": name, "price": price}
                except ValueError:
                    print(f"Ignore line: {line.strip()} - Invalid item ID")
    except FileNotFoundError:
        print("fooditems.txt not found. Make sure the file exists.")
    return food_items

# Function to input food preferences for a specific date
def input_food_preferences():
    date = input("Enter the date for the meal (YYYY-MM-DD): ")
    food_items = read_food_items()
    preferences = []
    
    print("Available food items:")
    for item_id, item_info in food_items.items():
        print(f"{item_id}: {item_info['name']} - {item_info['price']} SAR")
    
    while True:
        choice = input("Enter the item number and quantity (e.g., 1 2), or type 'done' to finish: ").strip()
        if choice.lower() == 'done':
            break
        else:
            try:
                item_id, quantity = map(int, choice.split())
                if item_id in food_items and quantity > 0:
                    preferences.append((item_id, quantity))
                else:
                    print("Invalid item number or quantity. Please try again.")
            except ValueError:
                print("Invalid input format. Please enter item number and quantity separated by space.")
    
    return date, preferences

    # Function to update payment details in PAYMENT.txt
def update_payment_details(student_id, date, total_payment):
    with open("PAYMENT.txt", "a") as file:
        file.write(f"{student_id}\t{date}\t{total_payment}\n")

# Main function for Advance Food Preference
def advance_food_preference(student_id):
    print("Advance Food Preference")
    date, preferences = input_food_preferences()
    
    # Calculate total payment
    total_payment = 0
    food_items = read_food_items()
    for item_id, quantity in preferences:
        total_payment += food_items[item_id]["price"] * quantity
    
    print(f"Total payment for the order: {total_payment} SAR")
    
    # Update payment details in PAYMENT.txt
    # student_id = input("Enter your ID: ")
    update_payment_details(student_id, date, total_payment)
    
    print("Food preferences submitted successfully!")



# Function to pay the dues
def pay_dues(student_id):
    print("Pay the dues")
    try:
        # Read student bank details
        student_bank = {}
        with open("studentbank.txt", "r") as bank_file:
            for line in bank_file:
                fields = line.strip().split("\t")
                student_bank[fields[0]] = fields[1]
        
        # Get student bank account and verify
        if student_id in student_bank:
            bank_account = student_bank[student_id]
            entered_account = input("Enter your bank account number: ")
            if entered_account == bank_account:
                # Verify bank account password
                password = input("Enter your bank account password: ")
                # Read student password from student.txt
                with open("student.txt", "r") as student_file:
                    for line in student_file:
                        fields = line.strip().split("\t")
                        if fields[0] == student_id and fields[2] == password:
                            print("Payment successful!")
                            break
                    else:
                        print("Incorrect password.")
            else:
                print("Incorrect bank account number.")
        else:
            print("Bank account not found for the student.")
    except FileNotFoundError:
        print("Error: Required files not found.")

# Main function for Student Menu
def student_menu(student_id):
    while True:
        print("\n1. Advance Food Preference")
        print("2. Pay the dues")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            advance_food_preference(student_id)
        elif choice == '2':
            pay_dues(student_id)  # Implement this function later
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function for Student Login
def student_login():
    student_data = read_student_data()
    
    print("Welcome to KFUPM Restaurant Management System")
    print("Student Login")
    
    student_id = input("Enter your ID: ")
    password = input("Enter your password: ")
    
    if validate_student_login(student_data, student_id, password):
        print("Login successful!")
        student_menu(student_id)  # After successful login, show the student menu
    else:
        print("Invalid ID or password. Please try again.")

# Test the student login function
student_login()
