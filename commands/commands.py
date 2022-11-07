from abc import ABC, abstractmethod
from services.services import *
from models.models import *

_user_service = UserService()


class AbstractCommand(ABC):

    @abstractmethod
    def execute(self):
        pass


class LoginCommand(AbstractCommand):

    user_service = _user_service

    def execute(self):
        login = input("Enter login:")
        password = input("Enter password:")
        try:
            self.user_service.login_user(login, password)
        except UserNotFound:
            print("Incorrect login or password")
            return
        print("Successfully logged in")


class RegisterCommand(AbstractCommand):

    user_service = _user_service

    def execute(self):
        login = input("Enter login:")
        password = input("Enter password:")
        try:
            self.user_service.register_user(User(login, password))
        except UserAlreadyExists:
            print(f"User with login {login} already exists")
            return
        print("Successfully registered user")


class ProfileCommand(AbstractCommand):

    user_service = _user_service

    def execute(self):
        user = self.user_service.get_current_user()
        print("Your profile")
        print(f"Login: {user.login}")
        print(f"Balance: {user.balance} \n")


class LogoutCommand(AbstractCommand):

    user_service = _user_service

    def execute(self):
        self.user_service.logout()
        print("Logout successful")


class AddBalanceCommand(AbstractCommand):

    user_service = _user_service

    def execute(self):
        amount = int(input("Enter money amount:"))
        self.user_service.add_balance(amount)


class ListRoomsCommand(AbstractCommand):

    def execute(self):
        pass
