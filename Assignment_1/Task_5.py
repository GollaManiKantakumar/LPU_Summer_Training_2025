text=input("Enter the number(string): ")
try:
    number=int(text)
    print("String converted to Integer:",number)
except ValueError:
    print("That's not a valid integer.")
