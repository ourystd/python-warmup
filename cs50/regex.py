import re

email = input("Enter a email: ")
match = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

if match:
    print("Valid email")
else:
    print("Invalid email")
