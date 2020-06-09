from unittest import TestCase
from pybricks.ev3devices.__stub.__infraredsensor import InfraredSensor
from pybricks.parameters.__stub.__port import Port


class TestInfraredSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, InfraredSensor, Port.A)
        self.assertRaises(ValueError, InfraredSensor, Port.B)
        self.assertRaises(ValueError, InfraredSensor, Port.C)
        self.assertRaises(ValueError, InfraredSensor, Port.D)
        
        try:
            InfraredSensor(Port.S1)
            InfraredSensor(Port.S2)
            InfraredSensor(Port.S3)
            InfraredSensor(Port.S4)
        except:
            self.fail()

    def test_distance(self):
        sensor = InfraredSensor(Port.S1)
        result = sensor.distance()
        self.assertTrue(isinstance(result, int))
        self.assertEqual(0, result)

    def test_beacon(self):
        sensor = InfraredSensor(Port.S1)
        result = sensor.beacon(0)
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(2, len(result))
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])

    def test_buttons(self):
        sensor = InfraredSensor(Port.S1)
        result = sensor.buttons(0)
        self.assertTrue(isinstance(result, list))

    def test_keypad(self):
        sensor = InfraredSensor(Port.S1)
        result = sensor.keypad()
        self.assertTrue(isinstance(result, list))

