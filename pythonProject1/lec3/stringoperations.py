language_name = "python"
print(language_name)
language_name = "jython"
print(language_name)
print(language_name.upper())
print(language_name.capitalize())

digit_input = input("Write digit:")
if(digit_input.isdigit() and len(digit_input) == 1):
    print("Digit")
    digit = int(digit_input)
    print("Digit", + type(digit))


else:
    print("String")

