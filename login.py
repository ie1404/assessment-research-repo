username=input("Enter the username: ")
password=input("Enter the password: ")

users=["Isaac", "Shaun", "Carl"]
passwords=["9867","1111","0123"]
# if username== "Isaac" and password == "9867":
#     print("Login Successful")
# else:
#     print("Incorrect Username or password")

RED="\033[31m"
GREEN="\033[32m"
RESET="\033[0m"

for i in range(len(users)):
    if username==users[i] and password==passwords[i]:
        print(GREEN,"Login Successful",RESET)
        exit()

print(RED,"Incorrect Username or password",RESET)

        