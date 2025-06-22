from string_utils import string_operations as ops
from string_utils import string_validations as val
def main():
    text = input("Enter a string: ")

    print("Reversed:", ops.reverse_string(text))
    print("Uppercase:", ops.to_uppercase(text))
    print("Length:", ops.get_length(text))

    print("Is palindrome?", val.is_palindrome(text))
    print("Is alphabetic?", val.is_alpha(text))
if __name__=="__main__":
    main()

