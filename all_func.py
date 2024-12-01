import datetime
import random
import math
import locale
from typing import List, Dict
from decimal import Decimal, getcontext, ROUND_HALF_UP
from dataclasses import dataclass
from exercise_1.person import Person
from exercise_1.model import PersonModel
from exercise_1.filter_age import filter_age
from exercise_1.filter_name import filter_name
from exercise_1.filter_phone import filter_phone
# 2. Функция, в которой демонстрируется работоспособность импортов из п. 1
def import_function():
    persons = Person()
    data = persons.get_all_persons()
    for key, value in data.items():
        print(f"""id: {key}
ФИО : {value.first_name} {value.middle_name} {value.last_name}
День рождения: {value.birthday_at}
""")
    try:
        person = PersonModel(
            first_name="Линда", 
            middle_name="Турецкая", 
            last_name="Владиславовна", 
            birthday_at=datetime.date(2024, 11, 3), 
            phone=88005553535, 
            email="ll@mail.ru", 
            password="kkll123ll11"
        )
        data = persons.create_person(person)
    except ValueError as e:
        print(e)
    finally:
        print("Добавление новых данных")
        person = PersonModel(
                first_name="Линда", 
                middle_name="Турецкая", 
                last_name="Владиславовна", 
                birthday_at=datetime.date(2004, 11, 3), 
                phone=88005553535, 
                email="ll@mail.ru", 
                password="kkll123ll11"
            )
        data = persons.create_person(person)
        data = persons.get_all_persons()
        for key, value in data.items():
            print("Ошибка")
            print(f"""id: {key}
    ФИО : {value.first_name} {value.middle_name} {value.last_name}
    День рождения: {value.birthday_at}
    """)
        print("Отфильтрованные данные")
        data = filter_name(persons)
        for key, value in data.items():
            print(f"""id: {key}
    ФИО : {value.first_name} {value.middle_name} {value.last_name}
    День рождения: {value.birthday_at}
    """)
        print("Отфильтрованные данные")
        data = filter_age(persons)
        for key, value in data.items():
            print(f"""id: {key}
    ФИО : {value.first_name} {value.middle_name} {value.last_name}
    День рождения: {value.birthday_at}
    Номер телефона: {value.phone}
    """)
        print("Отфильтрованные данные")
        data = filter_phone(persons)
        for key, value in data.items():
            print(f"""id: {key}
    ФИО : {value.first_name} {value.middle_name} {value.last_name}
    День рождения: {value.birthday_at}
    Номер телефона: {value.phone}
    """)

# 3. Файлы байт-кода любых 7 модулей, написанных в течение курса (в том числе модулей этой лабораторной).

# 4. Минимум 2 функции, использующие разные методы из модуля random
def generate_num():
    return random.randint(0, 500)

def generate_str():
    d = "фбвгдежзиклмнопрстуфхцчшщэюяьъ"
    return d[random.randint(0, len(d))]
# 5. Минимум 3 функций, использующих разные методы из модуля math
def pi_func():
    return math.pi

def pow_func(num1: int, num2: int):
    return int(math.pow(num1, num2))

def factorial_func(num: int):
    return math.factorial(num)

# 6. Минимум 3 функции, использующие разные методы из модуля locale
locale.setlocale(locale.LC_ALL, '')  # Использует текущую системную локаль

# 1. Функция форматирования чисел
def format_number(number):
    formatted_number = locale.format_string("%.2f", number, grouping=True)
    return f"Formatted number: {formatted_number}"

# 2. Функция работы с валютой
def format_currency(amount):
    formatted_currency = locale.currency(amount, grouping=True)
    return f"Formatted currency: {formatted_currency}"

# 3. Сравнение строк в соответствии с локалью
def locale_str_comparison(str1, str2):
    comparison_result = locale.strcoll(str1, str2)
    if comparison_result < 0:
        return f'"{str1}" меньше "{str2}" в текущей локали'
    elif comparison_result > 0:
        return f'"{str1}" больше "{str2}" в текущей локали'
    else:
        return f'"{str1}" равно "{str2}" в текущей локали'

# print(format_number(1234567.8912))
# print(format_currency(12345.67))
# print(locale_str_comparison("apple", "banana"))


# 7. Минимум 2 функции, использующие разные методы из модуля decimal
getcontext().prec = 10  # Задаем точность до 10 знаков

# 1. Функция для деления с округлением
def divide_with_rounding(a, b, rounding_mode=ROUND_HALF_UP):
    dec_a = Decimal(str(a))
    dec_b = Decimal(str(b))
    result = dec_a / dec_b
    rounded_result = result.quantize(Decimal("0.01"), rounding=rounding_mode)
    return f"Result: {rounded_result} (rounded to 2 decimal places)"

# 2. Функция для сложения списка значений
def sum_with_decimal(values):
    decimal_values = [Decimal(str(value)) for value in values]
    total = sum(decimal_values)
    return f"Total sum: {total}"

# print(divide_with_rounding(10, 3))
# print(sum_with_decimal([0.1, 0.2, 0.3, 0.4]))

# 8. Минимум 3 разных data-класса.
# 1. Класс для описания книги
@dataclass
class Book:
    title: str
    author: str
    price: Decimal
    in_stock: bool

# 2. Класс для описания координат на плоскости
@dataclass
class Point:
    x: float
    y: float

    def distance_to_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

# 3. Класс для описания транзакции
@dataclass
class Transaction:
    id: int
    amount: Decimal
    description: str
    is_successful: bool

    def apply_discount(self, discount_percentage):
        discount = self.amount * Decimal(discount_percentage) / Decimal(100)
        self.amount -= discount

# book = Book("Python Basics", "John Doe", Decimal("19.99"), True)
# print(book)
# point = Point(3, 4)
# print(f"Distance to origin: {point.distance_to_origin()}")
# transaction = Transaction(101, Decimal("100.00"), "Payment for service", True)
# transaction.apply_discount(10)
# print(transaction)

# 9. Минимум 5 функций, использующих в своей работе описанные в п. 7 data-классы
# В функции ДОЛЖНО быть, как минимум, следующее:
# 1. Передача объекта data-класса как параметр
def print_book_info(book: Book) -> None:
    print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}, In stock: {book.in_stock}")

# 2. Работа со списком из объектов data-классов
def total_books_price(books: List[Book]) -> Decimal:
    return sum(book.price for book in books)

# 3. Работа со словарём, где в качестве значения выступает объект data-класса
def mark_transaction_unsuccessful(transactions: Dict[int, Transaction], transaction_id: int) -> None:
    if transaction_id in transactions:
        transactions[transaction_id].is_successful = False

# 4. Модификация значений объекта data-класса
def update_point_coordinates(point: Point, new_x: float, new_y: float) -> None:
    point.x = new_x
    point.y = new_y

# 5. Создание объекта data-класса на основе передаваемых параметров
def create_discounted_transaction(transaction_id: int, amount: float, description: str, discount: float) -> Transaction:
    amount_decimal = Decimal(amount)
    discount_decimal = amount_decimal * Decimal(discount) / Decimal(100)
    final_amount = amount_decimal - discount_decimal
    return Transaction(id=transaction_id, amount=final_amount, description=description, is_successful=True)

