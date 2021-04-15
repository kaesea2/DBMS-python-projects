from occupants import Occupants


class Household:
    Households = []

    def __init__(self, name, custodian, housetype) -> None:
        self.name = name
        self.custodian = custodian
        self.type = housetype
        self.occupants = []

    def __repr__(self):
        return f'household(name={self.name},custodian={self.custodian}, type={self.type})'

    def __str__(self):
        return f'{self.name} has {self.custodian} as custodian and a type of {self.type}'

    def show(self):
        return self.name, self.custodian, self.type

    def add_occupant(self, occupants: Occupants) -> bool:
        if occupants not in self.occupants:
            self.occupants.append(occupants)
            return True
        return False

    def del_occupant(self, occupants: Occupants) -> bool:
        if occupants in self.occupants:
            self.occupants.remove(occupants)
            return True
        return False

    def view_occupant(self) -> bool:
        if len(self.occupants) != 0:
            for occupants in self.occupants:
                print(occupants)
                return True
        return False
