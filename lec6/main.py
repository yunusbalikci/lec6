from datetime import date
from exceptions import WrongPostalCode, WrongHouseNumber, WrongGenderSelection, WrongBirthDateSelection, WrongBirthDate
from model import User
import csv


class UserController:
    def __init__(self):
        self.users = []

    def add_user(self, start_date=date.today()):
        name = input("User name: ")
        last_name = input("User last name: ")
        try:
            pc = int(input("User address - postal code: "))
        except WrongPostalCode:
            print("Postal code must be a number")
        st = input("User address - street: ")
        try:
            cn = int(input("User address - house number: "))
        except WrongHouseNumber:
            print("House number must be a number")
        address = (pc, st, cn)
        gen = input("User gender: ")
        if (gen == "male" or "female"):
            gender = gen
        else:
            WrongGenderSelection.__init__()
        try:
            yy = int(input("User birth date - year: "))
            mm = int(input("User birth date - month: "))
            dd = int(input("User birth date - day: "))
        except WrongBirthDateSelection:
            print("Birth date must be express in numbers")
        bd = date(yy, mm, dd)
        if (start_date > bd):
            birth_date = bd
        else:
            WrongBirthDate.__init__()
        self.create_user(name, last_name, address, gender, birth_date)

    def create_user(self, name, last_name, address, gender, birth_date, start_date=date.today()):
        u = User(name, last_name, address, gender, birth_date)
        self.users.append(u)

    def print_users(self):
        for user in self.users:
            print(user)

    def save_user_to_file(self, path):
        with open(path, "a", encoding="utf-8") as file:
            for user in self.users:
                file.write(user.__str__() + '\n')

    def read_data_from_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    print(line.strip())
        except FileNotFoundError:
            print("File not found")
        except Exception:
            print("There is an exception")

    def file_conversion(self, path):
        try:
            with open(path, "r", encoding="utf-8") as in_file, open("users.csv", 'a') as out_file:
                stripped = (line.strip() for line in in_file)
                lines = (line.split(",") for line in stripped if line)
                writer = csv.writer(out_file, delimiter=';')
                writer.writerow(lines)
            with open("users.csv", 'r') as file:
                reader = csv.reader(file)
                for lin in reader:
                    print(lin)
        except FileNotFoundError:
            print("File not found")
        except Exception:
            print("There is an exception")


user_contr = UserController()
for i in range(0, 5):
    user_contr.add_user()

user_contr.print_users()
user_contr.save_user_to_file("users.txt")
user_contr.read_data_from_file("users.txt")
user_contr.file_conversion("users.txt")