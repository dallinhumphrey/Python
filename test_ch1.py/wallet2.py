
balance = 500
access = True


def mainMenu(): balance  access


print(" ")
print("Hello, welcome to your virtual wallet!")
print(" ")
print("Please choose one of the following options:")
print(" ")
print("1. Check balance")
print(" ")
print("2. Withdraw")
print(" ")
print("3. Deposit")
print(" ")
print("4. Exit the program")
print(" ")
original_input = int(input("Please enter a number -> "))

    if original_input == 8:
        access = False
        lockout_func()

    elif original_input == 1:
        print(" ")
        print(f"You're current balance is ${balance}")
        print(" ")
        anykey = input("Press enter to return to the Main Menu")
        mainMenu()

    elif original_input == 2:
        print(" ")
        withdraw_amount = int(input("How much would you like to withdraw?  $"))
        end_amount_withdraw = balance - withdraw_amount
        balance = end_amount_withdraw
        print(" ")
        print(
            f"Withdrawl complete.  Your current balance is ${end_amount_withdraw}")
        print(" ")
        anykey = input("Press enter to return to the Main Menu")
        mainMenu()

    elif original_input == 3:
        print(" ")
        deposit_amount = int(input("How much would you like to deposit?  $"))
        end_amount_deposit = balance + deposit_amount
        balance = end_amount_deposit
        print(" ")
        print(
            f"Deposit complete.  Your current balance is ${end_amount_deposit}")
        print(" ")
        anykey = input("Press enter to return to the Main Menu")
        mainMenu()

    elif original_input == 4:
        exit

    else:
        print(
            f"{original_input} is not a valid input.  Please enter a number between 1 - 4")
        anykey = input("Press enter to return to the Main Menu")
        mainMenu()


mainMenu() '''
