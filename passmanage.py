#Python password manager
import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")
    
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manger.keys() and password_manager[username] == hashed_password:
        print("Login Successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Enter your choice 1 to create an account, 2 To login, 3 To Exit.")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid Choice.")
    
if __name__ == "__main__":
    main()
