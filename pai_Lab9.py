def encode(password):
    newpassword = ""
    for i in password:
        i = int(i)
        i += 3
        newpassword += str(i)
    return newpassword

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def main():
    while True:
        menu()
        choice = input("Please enter an option: ")
        if choice == '1': # encodes password
            password = input("Please enter the password to encode: ")
            newpassword = encode(password)
            print("Your password has been encoded and stored!")
            print()

        elif choice == '2': # wait for partner
            pass

        elif choice == '3': # exits program
            exit()

        else:
            print("Incorrect option, please try again.")
            print()

if __name__ == '__main__':
    main()

