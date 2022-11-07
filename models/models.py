class User:

    def __init__(self, login, password, balance=0, pk=None):
        self.login = login
        self.password = password
        self.balance = balance
        if pk is not None:
            self.pk = pk
