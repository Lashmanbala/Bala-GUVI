def login_or_sign_up():
    choice = input("Type 1 for login or Type 2 for registration: ")
    if choice == str(1):
        login()
    elif choice == str(2):
        signup()
    else:
        print("Type a proper number")
        login_or_sign_up()

def mail_validation():
    import re
    global email
    email = input("Enter email: ")
    mail_pattern = "^([a-zA-Z0-9]+)([\.{1}])?([a-zA-Z0-9]+)(@gmail|@yahoo)([\.])(com|in)$"
    if not re.search(mail_pattern,email):
        print("Please enter a valid email")
        print("Example: abcd123@gmail.com or xyz_123@yahoo.com")
        return mail_validation()

def password_validation():
    import re
    global password
    password = input("Enter password(password should contain atleast 1 uppercase 1 lowercase 1 numeric 1 specialcharacter: ")
    password_pattern = "^.*(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).*$"
    if not re.match(password_pattern,password):
        print("Pasword is not strong.It should contain atleast 1 uppercase 1 lowercase 1 numeric 1 specialcharacter")
        return password_validation()
    if not len(password) > 5 :
        print("password is too short")
        print(" password should have atleast 6 characters")
        return password_validation()
    if not len(password) < 16:
        print("password is too long")
        print(" password shouldn't have more than 15 characters")
        return password_validation()

def is_exist():
    email_list = []
    db = open("database.txt", "r")
    for i in db:
        a, b = i.split()
        email_list.append(a)
    if email in email_list:
        print("Email already exists if you have an account please login")
        login()
    db.close()

def verify_user():
    email_list = []
    password_list = []
    db = open("database.txt", "r")
    for i in db:
        a, b = i.split()
        email_list.append(a)
        password_list.append(b)
    global user_dict
    user_dict = dict(zip(email_list, password_list))
    if email not in email_list:
        print("You are not yet registered.Please signup here.")
        signup()
    elif password == user_dict[email]:
        print("Welcome!")
    else:
        print("Wrong password")
        choice = input("If you forget your password type 1 to get it: ")
        if choice == str(1):
            forget_password()
        else:
            print("Type a proper number")

def do_you_know_password():
    global password
    choice = input("If you know password type 1\nIf you forget password type 2\nIf you want to change your password type 3: ")
    if choice == str(1):
        password = input("Type your password: ")
        verify_user()
    elif choice == str(2):
        forget_password()
    elif choice == str(3):
        change_password()
    elif len(choice) == 0:
        print("Type a number")

def forget_password():
    email_list = []
    password_list = []
    db = open("database.txt", "r")
    for i in db:
        a, b = i.split()
        email_list.append(a)
        password_list.append(b)
    global user_dict
    user_dict = dict(zip(email_list, password_list))
    print("Your password is: ",user_dict[email])
    print("To login rerun the program")

def change_password():
    email_list = []
    password_list = []
    db = open("database.txt", "r")
    for i in db:
        a, b = i.split()
        email_list.append(a)
        password_list.append(b)
    db.close()
    global user_dict
    user_dict = dict(zip(email_list, password_list))
    if email in email_list:
        print("Enter your new password here")
        password_validation()
        with open('database.txt', 'r+') as f:
            content = f.read()
            f.seek(0)
            f.write(content.replace(user_dict[email],password))
            print("You've successfully created your new password")
            print("Please login here")
            login()

def record():
    with open("database.txt", "a+") as db:
        db.write(email + " " + password + "\n")
        print("Successfully Registered!")
        print("To login rerun the program")
        exit()

def signup():
    mail_validation()
    is_exist()
    password_validation()
    record()

def login():
    import os
    with open("database.txt", "a+") as db:
        if os.path.getsize("database.txt") > 2:
            mail_validation()
            do_you_know_password()
        else:
            print("You are not yet registered. Please signup here")
            signup()

login_or_sign_up()