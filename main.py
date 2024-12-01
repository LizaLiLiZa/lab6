from all_func import *
def demonstrate_all_methods():
    # === Генерация случайных значений ===
    print("=== Random Generation ===")
    random_num = generate_num()
    random_char = generate_str()
    print(f"Generated random number: {random_num}")
    print(f"Generated random character: {random_char}")

    # === Методы модуля math ===
    print("\n=== Math Methods ===")
    print(f"Value of Pi: {pi_func()}")
    print(f"2^3: {pow_func(2, 3)}")
    print(f"Factorial of 5: {factorial_func(5)}")

    # === Методы модуля locale ===
    locale.setlocale(locale.LC_ALL, '')  # Установить текущую локаль
    print("\n=== Locale Methods ===")
    print(format_number(1234567.8912))
    print(format_currency(12345.67))
    print(locale_str_comparison("яблоко", "банан"))

    # === Методы модуля decimal ===
    getcontext().prec = 10  # Установить точность Decimal
    print("\n=== Decimal Methods ===")
    print(divide_with_rounding(10, 3))
    print(sum_with_decimal([0.1, 0.2, 0.3, 0.4]))

    # === Работа с data-классами ===
    print("\n=== Data Classes ===")
    # Работа с Book
    book1 = Book("Python Basics", "John Doe", Decimal("19.99"), True)
    book2 = Book("Advanced Python", "Jane Smith", Decimal("29.99"), False)
    print_book_info(book1)
    books = [book1, book2]
    print(f"Total price of books: {total_books_price(books)}")

    # Работа с Transaction
    transactions = {
        101: Transaction(101, Decimal("100.00"), "Service payment", True),
        102: Transaction(102, Decimal("200.00"), "Product payment", True),
    }
    mark_transaction_unsuccessful(transactions, 101)
    print(f"Transaction 101 marked as unsuccessful: {transactions[101]}")

    # Работа с Point
    point = Point(3, 4)
    print(f"Original point: ({point.x}, {point.y})")
    update_point_coordinates(point, 10, 10)
    print(f"Updated point: ({point.x}, {point.y})")

    # Создание нового объекта Transaction
    new_transaction = create_discounted_transaction(103, 150.00, "Discounted payment", 20)
    print(f"New discounted transaction: {new_transaction}")

    import_function()


if __name__ == "__main__":
    demonstrate_all_methods()

