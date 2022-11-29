class Bank:
    def __init__(self, money, name):
        self.__money = money
        self.__name = name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def MoneyX(self):
        self.money += int(input('Пополнение: '))

    def _kill(self):
        self.money = 0

    def __jackpot(self):
        self.money *= 10


bank = Bank(600, 'm bank')
bank.money = 500
bank.name = 'Optima'
print(bank.money, bank.name)
bank.MoneyX()
print(bank.money)
bank._kill()
print(bank.money)