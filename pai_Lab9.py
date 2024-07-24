def encode(password): # created by Paige, encodes password, returns string called newpassword after encoded
    newpassword = ""
    for i in password:
        i = int(i)
        i += 3
        newpassword += str(i)
    return newpassword

def decode(password):
    opassword = ''
    for i in password:
        i = int(i)
        i = i - 3
        opassword = opassword + str(i)
    print(f"The encoded password is {password}, and the original password is {opassword}")

def menu(): # prints menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def main(): # main function
    while True:
        menu()
        choice = input("Please enter an option: ")
        if choice == '1': # encodes password
            password = input("Please enter the password to encode: ")
            newpassword = encode(password)
            print("Your password has been encoded and stored!")
            print()

        elif choice == '2': # wait for partner
            decode(newpassword)
            pass

        elif choice == '3': # exits program
            exit()

        else:
            print("Incorrect option, please try again.")
            print()

if __name__ == '__main__':
    main()

