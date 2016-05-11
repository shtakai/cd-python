import unittest
from bulb_classes import LightBulb, LightBulbFactory

class LightBulbTest(unittest.TestCase):
    def setUp(self):
        self.bulb_factory = LightBulbFactory()
        self.bulb = self.bulb_factory.create_bulb("GE")

    def testNewBulbIsLightBulb(self):
        return self.assertIsInstance(self.bulb, LightBulb)

    def testBulbHasBrand(self):
        return self.assertEqual("GE", self.bulb.brand)

    def testBulbDefaultOff(self):
        return self.assertEqual(False, self.bulb.on_or_off())

    def testTurnOnBulb(self):
        self.bulb.switch_on()
        return self.assertEqual(True, self.bulb.on_or_off())


if __name__ == "__main__":
    unittest.main()
