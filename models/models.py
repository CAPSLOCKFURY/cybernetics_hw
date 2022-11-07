class User:

    def __init__(self, login, password, balance=0, pk=None):
        self.login = login
        self.password = password
        self.balance = balance
        if pk is not None:
            self.pk = pk


class Room:

    def __init__(self, room_number, room_name, room_price, booked_dates, pk=None):
        self.room_number = room_number
        self.room_name = room_name
        self.room_price = room_price
        self.booked_dates = booked_dates
        if pk is not None:
            self.pk = pk
