def main(): ...


class Student:
    def __init__(self, name: str, house: str, patronus: str | None = None):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        if value not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = value

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russel Terrier":
                return "🐶"
            case "Puffin":
                return "🦩"
            case "Badger":
                return "🐾"
            case "Owl":
                return "🦉"
            case _:
                return "🪄"


if __name__ == "__main__":
    # main()
    student = Student("Harry", "Gryffindor")
    student.name = ""
    print(student.charm())
