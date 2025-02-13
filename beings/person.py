class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def forename(self) -> str:
        return self.name.split(" ")[0]

    @property
    def surname(self) -> str:
        name = self.name.split(" ")[-1]
        return name if name != self.forname else None

    def celebrate_birthday(self) -> None:
        self.age += 1
