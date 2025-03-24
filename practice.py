"""
class Phone:
    line_type = 'проводной'

# Печать содержимого атрибута line_type через объект rotary_phone.
# print(rotary_phone.line_type)
# Печать содержимого атрибута line_type через объект keypad_phone.
# print(keypad_phone.line_type)

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value


rotary_phone = Phone(dial_type_value='disk')
keypad_phone = Phone(dial_type_value='button')

print(rotary_phone.dial_type)
print(rotary_phone.line_type)
"""
"""
class Phone:
    # Атрибут класса.
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        # Атрибут объекта.
        self.dial_type = dial_type_value

# Создать объект класса Phone.
rotary_phone = Phone(dial_type_value='дисковый')
keypad_phone = Phone(dial_type_value='кнопочный')

# Распечатать значение атрибута класса.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута line_type для объекта rotary_phone.
rotary_phone.line_type = 'радио'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута класса через класс.
Phone.line_type = 'спутниковый'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')
"""

"""
class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name='Роберт', second_name='Крузо', gender='м')
# mployee2 = Employee(...)

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
"""


class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        # Сюда добавьте новый атрибут remaining_vacation_days

    def consume_vacation(self, spend_days):  # функция по списанию дней отпуска
        if spend_days > self.remaining_vacation_days:
            return 'Недостаточно дней ,Убавь свой аппетит, измени кол-во дней отпуска в меньшую сторону'
        
        self.remaining_vacation_days -= spend_days

    # функция которая показывает остаток дней отпуска

    def get_vacation_details(self):
        #if self.remaining_vacation_days < 
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


# Пример использования класса:
employee1 = Employee('Роберт', 'Крузо', 'м')
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
employee1.consume_vacation(7)
print(employee1.get_vacation_details())

employee2 = Employee("Дарт", "Мол", "м")
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.')

print(employee2.consume_vacation(33), employee2.get_vacation_details())