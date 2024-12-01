from exercise_1.data  import list_data
from exercise_1.model import PersonModel

class Person():
    """
        Person
    """
    data = list_data
    @classmethod
    def get_all_persons(self) -> dict[int, PersonModel]:
        """
            Get all persons
        """
        return self.data

    def get_person(self, id_: int) -> PersonModel:
        """
            Get person by id
        """
        for key, value in self.data.items():
            if key == id_:
                return value
        raise ValueError(detail=f"Нет пользователя id = {id_}.")

    def create_person(self, person: PersonModel) -> dict[PersonModel]:
        """
            Create person
        """
        max_id = 1 + max([key for key, value in self.data.items()])
        self.data[max_id] = person
        return self.data
