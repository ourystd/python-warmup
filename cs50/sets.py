from oop_students import Student

students: list[Student] = [
    Student("Lily", "Gryffindor", "Otter"),
    Student("Hedwig", "Ravenclaw", "Otter"),
    Student("Hermione", "Gryffindor", "Stag"),
    Student("Harry", "Gryffindor", "Jack Russel Terrier"),
    Student("Ron", "Gryffindor", "Jack Russel Terrier"),
    Student("Draco", "Slytherin", "Jack Russel Terrier"),
    Student("Luna", "Ravenclaw", "Otter"),
    Student("Neville", "Gryffindor", "Otter"),
    Student("Cho", "Ravenclaw", "Otter"),
]


def get_all_houses(students):
    return set(student["house"] for student in students)


if __name__ == "__main__":
    houses = get_all_houses(students)
    print(houses)
