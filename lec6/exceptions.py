
class WrongPostalCode(Exception):
    def __init__(self):
        print("Postal code must be a number")


class WrongHouseNumber(Exception):
    def __init__(self):
        print("House number must be a number")


class WrongGenderSelection(Exception):
    def __init__(self):
        print("Gender can only be Male or Female")


class WrongBirthDateSelection(Exception):
    def __init__(self):
        print("Birth date must be express in numbers")


class WrongBirthDate(Exception):
    def __init__(self):
        print("Birth date can't be in the future")