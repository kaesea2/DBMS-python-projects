import unittest

from estate import Estate
from housetype import HouseType
from household import Household
from occupants import Occupants
from property_position import PropertyPosition
from sex import Sex

from property import Property
from buildingtype import BuildingType
from thoroughfare_type import ThoroughfareType
from usageStatus import UsageStatus
from thoroughfare import Thoroughfare


class TestHousehold(unittest.TestCase):
    def test_add_occupants(self):
        house=Household('ay','mide', HouseType.single)
        test = house.add_occupant(Occupants('bill',Sex.male).show())
        test2 = house.view_occupant()
        expect = True
        self.assertEqual(test,expect)
        self.assertEqual(test2,expect)

    def test_del_occupants(self):
        house = Household('ay', 'mide', HouseType.single)
        house.add_occupant(Occupants('bill', Sex.male).show())
        house.view_occupant()
        test = house.del_occupant(Occupants('bill', Sex.male).show())
        expect = True
        self.assertEqual(test, expect)


class TestProperty(unittest.TestCase):
    def test_add_household(self):
        property = Property('fare1','bricks','b45', BuildingType.semi_detached, UsageStatus.owned, '12-32-12')
        test = property.add_household(Household('bill', 'mide', HouseType.multiple.name).show())
        expect = True
        self.assertEqual(test,expect)

    def test_del_household(self):
        property = Property('fare1','bricks','b45', BuildingType.semi_detached, UsageStatus.owned, '12-32-12')
        property.add_household(Household('bill', 'mide', HouseType.multiple.name).show())
        test = property.del_household(Household('bill', 'mide', HouseType.multiple.name).show())
        expect = True
        self.assertEqual(test, expect)

    def test_view_household(self):
        property = Property('fare1','bricks','b45', BuildingType.semi_detached, UsageStatus.owned, '12-32-12')
        property.add_household(Household('bill', 'mide', HouseType.multiple.name).show())
        test = property.view_household()
        expect = True
        self.assertEqual(test, expect)

    def test_update_household(self):
        property = Property('fare1','bricks','b45', BuildingType.semi_detached, UsageStatus.owned, '12-32-12')
        property.add_household(Household('bill', 'mide', HouseType.multiple.name).show())
        test = property.update_household(Household('bill', 'mide', HouseType.multiple.name).show(), 'ayo', 'abiola',
                                         HouseType.single.name)
        property.view_household()
        expect = True
        self.assertEqual(test, expect)


class TestThoroughfare(unittest.TestCase):
    def test_add_property(self):
        thoroughfare = Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name)
        test = thoroughfare.add_property(Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name,
                                                  '12-32-12').show())
        expect = True
        self.assertEqual(test, expect)

    def test_del_property(self):
        thoroughfare = Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name)
        thoroughfare.add_property(Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name,
                                           '12-32-12').show())
        test = thoroughfare.del_property(Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name,
                                                  '12-32-12').show())
        expect = True
        self.assertEqual(test, expect)

    def test_view_property(self):
        thoroughfare = Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name)
        thoroughfare.add_property(
            Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name, '12-32-12').show())
        test = thoroughfare.view_property()
        expect = True
        self.assertEqual(test, expect)

    def test_update_property(self):
        thoroughfare = Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name)
        thoroughfare.add_property(Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name,
                                           '12-32-12').show())
        test = thoroughfare.update_property(Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name,
                                                     '12-32-12').show(), 'complex','b32', BuildingType.terrance.name,
                                            UsageStatus.owned.name, '21-31-12')
        thoroughfare.view_property()
        expect = True
        self.assertEqual(test, expect)


class TestEstate(unittest.TestCase):
    def test_add_thoroughfare(self):
        estate = Estate('zion')
        test = estate.add_thoroughfare(Thoroughfare('swizz', ThoroughfareType.close.name,
                                                    PropertyPosition.both_sides.name).show())
        expect = True
        self.assertEqual(test, expect)

    def test_del_thoroughfare(self):
        estate = Estate('zion')
        estate.add_thoroughfare(Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name).show())
        test = estate.del_thoroughfare(Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name).show())
        expect = True
        self.assertEqual(test, expect)

    def test_view_thoroughfare(self):
        estate = Estate('zion')
        estate.add_thoroughfare(Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name).show())
        test = estate.view_thoroughfare()
        expect = True
        self.assertEqual(test, expect)

    def test_update_thoroughfare(self):
        estate = Estate('zion')
        estate.add_thoroughfare(Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name).show())
        test = estate.update_thoroughfare(Thoroughfare('swizz', ThoroughfareType.close.name,
                                                       PropertyPosition.both_sides.name).show(), 'banks',
                                          ThoroughfareType.avenue.name, PropertyPosition.one_side.name)
        estate.view_thoroughfare()
        expect = True
        self.assertEqual(test, expect)

    def test_add_property(self):
        estate = Estate('zion')
        test = estate.add_property(Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name),
                                   Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name, '12-32-12').show())
        expect =True
        self.assertEqual(test, expect)

    def test_del_property(self):
        estate = Estate('zion')
        estate.add_property(Thoroughfare('swizz', ThoroughfareType.close.name, PropertyPosition.both_sides.name),
                            Property('fare1','bricks','b45', BuildingType.semi_detached.name, UsageStatus.owned.name, '12-32-12').show())

        estate.add_property(Thoroughfare('swizz', ThoroughfareType.avenue.name, PropertyPosition.both_sides.name),
                            Property('fare1','bricks','b45', BuildingType.block_of_flat.name, UsageStatus.owned.name, '12-32-12').show())
        estate.view_property()
        test = estate.del_property()
        estate.view_property()
        expect = True
        self.assertEqual(test, expect)


if __name__ == '__main__':
    unittest.main()