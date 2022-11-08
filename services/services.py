from db.database import ShelveRepository
from session.holder import SessionHolder
from .exceptions import *
from models.models import *


class UserService:
    repository = ShelveRepository("users")

    def register_user(self, new_user) -> User:
        users = self.repository.get_all()
        for user in users:
            if user.login == new_user.login:
                raise UserAlreadyExists(new_user.login)
        return self.repository.save(new_user)

    def login_user(self, login, password):
        users = self.repository.get_all()
        for user in users:
            if user.login == login and user.password == password:
                SessionHolder.set_current_user(user)
                return
        raise UserNotFound(login)

    def add_balance(self, amount: int) -> User:
        user = SessionHolder.get_current_user()
        user.balance += amount
        return self.repository.save(user)

    def get_current_user(self) -> User:
        return self.repository.sync(SessionHolder.get_current_user())

    def logout(self):
        SessionHolder.set_current_user(None)


class RoomService:

    repository = ShelveRepository("rooms")

    def get_all_rooms(self) -> list[Room]:
        return self.repository.get_all()