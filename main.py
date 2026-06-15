# Login & Registration System

users = {}

while True:
    print("\n===== Login & Registration System =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Register
    if choice == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in users:
            print("Username already exists!")
        else:
            users[username] = password
            print("Registration Successful!")

    # Login
    elif choice == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in users and users[username] == password:
            print("Login Successful! Welcome,", username)
        else:
            print("Invalid Username or Password!")

    # Exit
    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")