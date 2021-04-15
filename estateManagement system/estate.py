from thoroughfare import Thoroughfare
from thoroughfare import Property


class Estate:
    Estates = []

    def __init__(self, name):
        self.name: str = name
        self.Thoroughfares = []
        self.Properties = 0

    def __repr__(self):
        return f'estate(name={self.name}'

    def __str__(self):
        return f'{self.name}'

    def show(self):
        return self.name

    def add_thoroughfare(self, thoroughfare: Thoroughfare) -> bool:
        if thoroughfare not in self.Thoroughfares:
            self.Thoroughfares.append(thoroughfare)
            return True
        return False

    def del_thoroughfare(self, thoroughfare: Thoroughfare) -> bool:
        if thoroughfare in self.Thoroughfares:
            self.Thoroughfares.remove(thoroughfare)
            return True
        return False

    def view_thoroughfare(self) -> bool:
        if len(self.Thoroughfares) != 0:
            for thoroughfare in self.Thoroughfares:
                print(thoroughfare)
            return True
        return False

    def update_thoroughfare(self, thoroughfare: Thoroughfare, new_name, new_type, new_property_position) -> bool:
        if thoroughfare in self.Thoroughfares:
            for i, item in enumerate(self.Thoroughfares):
                if item == thoroughfare:
                    self.Thoroughfares[i] = Thoroughfare(new_name, new_type, new_property_position).show()
                    return True
        return False

    def add_property(self, thoroughfare: Thoroughfare, property: Property) -> bool:
        add = thoroughfare.add_property(property)
        if add:
            self.Properties += 1
            return True
        return False

    def del_property(self) -> bool:
        if self.Properties != 0:
            self.Properties -= 1
            return True
        return False

    def view_property(self) -> bool:
        if self.Properties != 0:
            print(self.Properties)
            return True
        return False
