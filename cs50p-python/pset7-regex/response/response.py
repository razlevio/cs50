import validators

def main():
    email = ""
    while email == "":
        email = input("Email: ")
    print(email_validation(email))

def email_validation(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
