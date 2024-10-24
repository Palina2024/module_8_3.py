class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __number):
        self.model = str(model)
        self.vin = int(__vin)
        self.number = str(__number)
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__number)

    def __is_valid_vin(self, __vin):
         if not isinstance(self.vin, int):
             raise IncorrectVinNumber('Некорректный тип vin номер')
         elif self.vin not in range(1000000, 10000000):
             raise IncorrectVinNumber('Неверный диапазон для vin номера')
         else:
             return True

    def __is_valid_numbers(self, __number):
        if not isinstance(self.number, str):
             raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(self.number) != 6:
             raise IncorrectCarNumbers('Неверная длина номера')
        else:
             return True



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')