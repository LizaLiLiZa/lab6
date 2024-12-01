import datetime
from exercise_1.model import PersonModel
list_data = {
    1: PersonModel(
        first_name="Елизавета",
        last_name="Гурченкова",
        middle_name="Владимировна",
        birthday_at=datetime.date(2005, 10, 23),
        email="lizzka@mail.ru",
        phone=88005553535,
        password="parol1234"
    ),
    2: PersonModel(
        first_name="Александр",
        last_name="Иванов",
        middle_name="Сергеевич",
        birthday_at=datetime.date(1997, 6, 15),
        email="alex.ivanov@mail.ru",
        phone=89261234567,
        password="password123"
    ),
    3: PersonModel(
        first_name="Мария",
        last_name="Петрова",
        middle_name="Игоревна",
        birthday_at=datetime.date(1995, 3, 9),
        email="masha.pet@mail.ru",
        phone=89172345678,
        password="qwerty2024"
    ),
    4: PersonModel(
        first_name="Дмитрий",
        last_name="Смирнов",
        middle_name="Алексеевич",
        birthday_at=datetime.date(2000, 11, 25),
        email="dima.smirnov@mail.ru",
        phone=89312349876,
        password="smirnov982000"
    ),
    5: PersonModel(
        first_name="Анна",
        last_name="Кузнецова",
        middle_name="Владиславовна",
        birthday_at=datetime.date(1992, 8, 12),
        email="anna.kuz@mail.ru",
        phone=89031112233,
        password="annapass2022"
    ),
    6: PersonModel(
        first_name="Игорь",
        last_name="Морозов",
        middle_name="Николаевич",
        birthday_at=datetime.date(1989, 4, 4),
        email="igor.morozov@mail.ru",
        phone=89998887766,
        password="igorm8999"
    )
}
