import doctest

class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0)-> None:
        """
        Класс, который инициализирует новый банковский счет.

        :param account_number: str: Номер банковского счета.
        :param initial_balance: float: Начальный баланс счета (по умолчанию 0.0).
        """
        self.account_number: str = account_number
        self._balance: float = initial_balance
        self.total_deposited: float = 0.0

    @property
    def balance(self) -> float:
        """
        Свойство с декоратором @property, которое возвращает текущий баланс счета.

        :return: Текущий баланс.
        """
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Сеттер с декоратором @balance.setter, который устанавливает новый баланс счета.

        :param value: float: Новый баланс.
        :raise ValueError: Если новый баланс отрицательный.
        """
        if value < 0:
            raise ValueError('Баланс не может быть отрицательным.')
        self._balance: float = value

    def deposit(self, amount: int) -> None:
        """
        Метод, который вносит сумму на счет.

        :param amount: int: Сумма для внесения.
        :raise ValueError: Если сумма вклада не положительная.


        >>> test_account = BankAccount('123456789', 1000)
        >>> test_account.deposit(500)
        >>> test_account.balance    #1500
        >>> test_account.total_deposited    #500
        >>> test_account.deposit(-100)
        Traceback (most recent call last):
            ...
        ValueError: Сумма вклада должна быть положительной!
        """
        if amount <= 0:
            raise ValueError('Сумма вклада должна быть положительной!')
        self._balance += amount
        self.total_deposited += amount
        print(f'Внесено: {amount}. Новый баланс: {self.balance}')

    def withdraw(self, amount: int) -> None:
        """
        Метод, который снимает сумму со счета.

        :param amount: int: Сумма для снятия.
        :raise ValueError: Если сумма снятия не положительная или превышает текущий баланс.


        >>> test_account = BankAccount('123456789', 1000)
        >>> test_account.withdraw(300)
        >>> test_account.balance    #700
        >>> test_account.withdraw(-100)    #Это вызовет исключение
        Traceback (most recent call last):
            ...
        ValueError: Сумма снятия должна быть положительной!
        >>> test_account.withdraw(800)     #Это вызовет исключение
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно средств на счете для снятия!
        """
        if amount <= 0:
            raise ValueError ('Сумма снятия должна быть положительной!')
        if amount > self._balance:
            raise ValueError ('Недостаточно средств на счете для снятия!')
        self._balance -= amount
        print(f'Снято: {amount}. Новый баланс: {self.balance}')

    def calculate_interest(self, rate: float) -> None:
        """
        Метод, который начисляет проценты на текущий баланс.

        :param rate: float: Процентная ставка.
        :raise ValueError: Если процентная ставка отрицательная.


        >>> test_account = BankAccount('123456789', 1000)
        >>> test_account.calculate_interest(0.3)    #0.3% от 1000.0
        >>> test_account.balance    #1050
        >>> test_account.calculate_interest(-3)    #Это вызовет исключение
        Traceback (most recent call last):
            ...
        ValueError: Процентная ставка не может быть отрицательной!
        """
        if rate < 0:
            raise ValueError('Процентная ставка не может быть отрицательной!')
        interest: float = self._balance * (rate / 100)
        self._balance += interest
        print(f'Начисленные проценты: {interest}. Новый баланс: {self.balance}')



if __name__ == '__main__':

    account = BankAccount('123456789', 1000)
    print(f'Текущий баланс: {account.balance}')

    while True:
        try:
            deposit_amount = int(input('Внесение на счет дополнительной суммы: '))
            account.deposit(deposit_amount)
            break
        except ValueError as e:
            print(f'Ошибка при внесении средств - {e}. Попробуйте еще раз.')

    while True:
        try:
            withdraw_amount = int(input('Введите сумму для снятия: '))
            account.withdraw(withdraw_amount)
            break
        except ValueError as e:
            print(f'Ошибка при снятии средств - {e}. Попробуйте еще раз.')


    account.calculate_interest(0.3)



doctest.testmod()