class UserNotFound(Exception):

    def __init__(self, login):
        super().__init__(f"User with login {login} not found")


class UserAlreadyExists(Exception):

    def __init__(self, login):
        super().__init__(f"User with login {login} already exists")
