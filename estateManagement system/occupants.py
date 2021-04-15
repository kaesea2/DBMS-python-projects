from sex import Sex


class Occupants:
    def __init__(self, name, sex: Sex) -> None:
        self.name = name
        self.gender = sex

    def __str__(self) -> str:
        return f'{self.name} is a {self.gender.name}'

    def show(self):
        return self.name, self.gender.value
