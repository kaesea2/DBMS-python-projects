from property import Property


class Thoroughfare:
    Thoroughfares = []

    def __init__(self, thoroughfare_name, thoroughfare_type, property_position):
        self.name = thoroughfare_name
        self.type = thoroughfare_type
        self.p_position = property_position
        self.Properties = []

    def __repr__(self):
        return f'Thoroughfare(name={self.name},type={self.type}, properties={self.p_position})'

    def __str__(self):
        return f'{self.name} is a {self.type} with properties on {self.p_position}'

    def show(self):
        return self.name, self.type, self.p_position

    def add_property(self, property: Property) -> bool:
        if property not in self.Properties:
            self.Properties.append(property)
            return True
        return False

    def del_property(self, property: Property) -> bool:
        if property in self.Properties:
            self.Properties.remove(property)
            return True
        return False

    def view_property(self) -> bool:
        if len(self.Properties) != 0:
            for property in self.Properties:
                print(property)
            return True
        return False

    def update_property(self, property: Property, new_building_name, building_number, new_building_type, new_usage_status,
                        new_completion_date) -> bool:
        if property in self.Properties:
            for i, item in enumerate(self.Properties):
                if item == property:
                    self.Properties[i] = Property(self.name, new_building_name, building_number, new_building_type,
                                                  new_usage_status, new_completion_date).show()
                    return True
        return False
