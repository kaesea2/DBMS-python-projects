from household import Household


class Property:
    Properties = []

    def __init__(self, thoroughfare_name, building_name, building_number, building_type, usage_status, completion_date: str):
        self.thoroughfare_name = thoroughfare_name
        self.name = building_name
        self.building_number = building_number
        self.type = building_type
        self.property_status = usage_status
        self.date = completion_date
        self.Households = []
        self.address = self.address()

    def __repr__(self):
        return f'Property(name={self.name},status={self.property_status},completion date={self.date}, address={self.address})'

    def __str__(self):
        return f'{self.name} is {self.property_status} and completed on {self.date}, located at {self.address}'

    def show(self):
        return self.name, self.type, self.property_status, self.date, self.address

    def address(self):
        return self.name, self.building_number, self.thoroughfare_name

    def add_household(self, household: Household) -> bool:
        if household not in self.Households:
            self.Households.append(household)
            return True
        return False

    def del_household(self, household: Household) -> bool:
        if household in self.Households:
            self.Households.remove(household)
            return True
        return False

    def view_household(self) -> bool:
        if len(self.Households) != 0:
            for household in self.Households:
                print(household)
            return True
        return False

    def update_household(self, household: Household, new_name, new_custodian, new_housetype) -> bool:
        if household in self.Households:
            for i, item in enumerate(self.Households):
                if item == household:
                    self.Households[i] = Household(new_name, new_custodian, new_housetype).show()
                    return True
        return False

