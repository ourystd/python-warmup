from email.utils import parseaddr


def is_valid_email(email):
    return "@" in parseaddr(email)[1]


email = input("Enter an email: ")
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")
