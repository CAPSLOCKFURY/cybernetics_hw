from abc import ABC, abstractmethod
from services.services import *
from models.models import *
from datetime import datetime
from validators.validators import *

_user_service = UserService()
_room_service = RoomService()
_login_length_validator = StringLengthValidator(4, less=False)
_password_length_validator = StringLengthValidator(5, less=False)
_login_regex_validator = RegexValidator("[a-zA-Z0-9_]+")
_password_regex_validator = RegexValidator("[a-zA-Z0-9_]+")
_money_amount_validator = MinNumberValidator(0)
_date_gte_today_validator = DateGTETodayValidator()
_check_in_date_before_check_out_date_validator = Date1BeforeDate2Validator()
_date_not_equals_validator = DatesNotEqualValidator()


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
        if not _login_length_validator.validate(login):
            print("Login is less than 4 characters")
            return
        if not _login_regex_validator.validate(login):
            print("Login can contain only lowercase and uppercase latin, numbers, underscores")
            return
        if not _password_length_validator.validate(password):
            print("Password is less than 5 characters")
            return
        if not _password_regex_validator.validate(password):
            print("Login can contain only lowercase and uppercase latin, numbers, underscores")
            return
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
        try:
            amount = int(input("Enter money amount:"))
        except ValueError:
            print("Incorrect money amount")
            return
        if not _money_amount_validator.validate(amount):
            print("Money amount is less or equal 0")
            return
        self.user_service.add_balance(amount)
        print("Successfully added money to your balance")


class ListRoomsCommand(AbstractCommand):

    room_service = _room_service

    def execute(self):
        rooms = self.room_service.get_all_rooms()
        rooms.sort(key=lambda val: val.room_name)
        print("------------------------------------")
        for room in rooms:
            print(f"Room number: {room.room_number}")
            print(f"Room name: {room.room_name}")
            print(f"Room capacity: {room.room_capacity}")
            print(f"Room price: {room.room_price}")
            if len(room.booked_dates) != 0:
                print("Booked dates: ")
                for rr in room.booked_dates:
                    print(f"Check in Date: {rr.check_in_date.date()}, Check out Date: {rr.check_out_date.date()}")
            print("------------------------------------")


class BookRoomCommand(AbstractCommand):

    room_service = _room_service

    def execute(self):
        room_number = int(input("Enter room number:"))
        check_in_date = datetime.strptime(input("Enter check in date:"), "%d-%m-%Y")
        check_out_date = datetime.strptime(input("Enter check out date:"), "%d-%m-%Y")
        if not _date_gte_today_validator.validate(check_in_date):
            print("Check in date is before today")
            return
        if not _date_gte_today_validator.validate(check_out_date):
            print("Check out date is before today")
            return
        if not _date_not_equals_validator.validate(check_in_date, check_out_date):
            print("Check in date is check out date")
            return
        if not _check_in_date_before_check_out_date_validator.validate(check_in_date, check_out_date):
            print("Check out date is before check in date")
            return
        try:
            self.room_service.book_room(room_number, check_in_date, check_out_date)
        except BookingDateIntersection:
            print("Booking date overlaps with existing ones")
            return
        except NotEnoughMoney:
            print("You have not enough money to book this room for given dates")
            return
        print(f"Successfully booked room {room_number} on dates {check_in_date.date()} to {check_out_date.date()}")
