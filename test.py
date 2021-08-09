user = {"john":"mypasswordhere"}

def checkPassword():
    username = input("enter a username: ")
    password = input("enter a password: ")
    if username not in user.keys():
        return "invalid username"
    if user[username] == password:
        return "successfully confirmed user account"
    return "invalid account credentials"

print(checkPassword())