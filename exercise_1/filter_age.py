from exercise_1.person import Person
from exercise_1.model import PersonModel

def filter_age(person: Person) -> dict[int, PersonModel]:
    data = person.get_all_persons()
    persons = data.values()
    sorted_persons = sorted(persons, key=lambda person: person.birthday_at)
    sorted_persons_dict = {}
    for i in sorted_persons:
        for key, value in data.items():
            if value == i:
                sorted_persons_dict[key] = value
    return sorted_persons_dict