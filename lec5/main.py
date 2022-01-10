from datetime import date

from model import User


class UserController:
    def __init__(self):
        self.users = []

    def create_user(self, name, last_name, address, gender, birth_date, start_date=date.today()):
        u = User(name, last_name, address, gender, birth_date)
        self.users.append(u)

    def print_users(self):
        for user in self.users:
            print(user)


m = "male"
f = "female"
gender = m or f
add1 = ("85-796", "Kaliskiego st.", 20)
add2 = ("85-796", "Fordonska st.", 47)
add3 = ("85-796", "Jagellon st.", 52)
add4 = ("85-796", "Gdanski st.", 23)

user_controller = UserController()
user_controller.create_user("Yunus", "Balıkcı", add1, m, date(2001, 8, 29))
user_controller.create_user("Remzi", "Balıkcı", add2, m, date(1975, 11, 23))
user_controller.create_user("Necla", "Balıkcı", add3, f, date(1969, 7, 1))
user_controller.create_user("İrem", "Balıkcı", add4, f, date(1999, 1, 7))

user_controller.print_users()