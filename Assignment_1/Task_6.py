while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        print("You entered the integer:", number)
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
