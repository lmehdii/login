import hashlib
def sign_up():
    user = input("enter your username: ")
    hashed_user = hashlib.sha256(user.encode())
    hexed_user = hashed_user.hexdigest()
    while hexed_user in open("pass.txt", "r").read():
        print("already in")
        user = input("enter another username: ")
        hashed_user = hashlib.sha256(user.encode())
        hexed_user = hashed_user.hexdigest()
        
    password = input("enter a password: ")
    check_pass = input("repeat password: ")
    while password != check_pass:
        print("passwords do not match")
        password = input("enter a password: ")
        check_pass = input("repeat password: ")
    hashed_pass = hashlib.sha256(password.encode())
    hexed_pass = hashed_pass.hexdigest()
    add = open("pass.txt", "a").write("\n"+hexed_user+"+"+hexed_pass)
    print("done.")

def log_in():
    user = input("enter your username: ")
    password = input("enter a password: ")

    hashed_user = hashlib.sha256(user.encode())
    hexed_user = hashed_user.hexdigest()
    hashed_pass = hashlib.sha256(password.encode())
    hexed_pass = hashed_pass.hexdigest()
    
    while (hexed_user) not in open("pass.txt", "r").read() or (hexed_pass) not in open("pass.txt", "r").read():
        print("user or pass incorrect")
        user = input("enter your username: ")
        password = input("enter a password: ")
        
        hashed_user = hashlib.sha256(user.encode())
        hexed_user = hashed_user.hexdigest()
        hashed_pass = hashlib.sha256(password.encode())
        hexed_pass = hashed_pass.hexdigest()

        
    if hexed_user and hexed_pass in open("pass.txt", "r").read():
        print("you are logged in")
    
x=input('''1- Sign up
2- Log in
> ''')

if x == "1":
    sign_up()
elif x =="2":
    log_in()
else:
    print("sorry no")
