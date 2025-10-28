import csv


def main() -> None:
    with open("data.csv") as file:
        #"""
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
        #"""
        """
        #reader = csv.DictReader(file)
        users = list()
        for row in reader:
            users.append(User(*row.values()))

        for user in users:
            print(user)
        #"""


class User:

    def __init__(self, iid: int, name: str, age: int):
        self._id  = iid
        self.name = name
        self.age  = age

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, iid) -> None:
        self._id = iid

    def __str__(self) -> str:
        return f"User(id={self._id}, name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"User(id={self._id}, name={self.name}, age={self.age})"


if "__main__" == __name__:
    main()

