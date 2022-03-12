import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

while True:
    name = input("Please Enter Your Name:")
    if name.isalpha():
        name = str(name)
        break


def check(Email):

    if re.fullmatch(regex, Email):
        return True

    else:
        return False


while True:
    email = input("Enter Your Mail: ")
    checking = check(email)
    if checking:
        email=str(email)
        break


print("Hello ["+name+"] Your Email is : "+email)