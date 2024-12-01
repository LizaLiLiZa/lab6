from exercise_1.person import Person
from exercise_1.model import PersonModel

def filter_name(person: Person) -> dict[int, PersonModel]:
    data = person.get_all_persons()
    sorted_persons = sorted(data.items(), key=lambda item: item[1].first_name.lower())
    sorted_persons_dict = {person_id: person_model for person_id, person_model in sorted_persons}
    return sorted_persons_dict
