from unittest import TestCase
from pybricks.ev3devices.__stub.__colorsensor import ColorSensor
from pybricks.parameters.__stub.__port import Port

class TestColorSensor(TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, ColorSensor, Port.A)
        self.assertRaises(ValueError, ColorSensor, Port.B)
        self.assertRaises(ValueError, ColorSensor, Port.C)
        self.assertRaises(ValueError, ColorSensor, Port.D)
        
        try:
            ColorSensor(Port.S1)
            ColorSensor(Port.S2)
            ColorSensor(Port.S3)
            ColorSensor(Port.S4)
        except:
            self.fail()

    def test_color(self):
        sensor = ColorSensor(Port.S1)
        self.assertIsNone(sensor.color())

    def test_ambient(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.ambient()
        self.assertTrue(isinstance(result, int))
        self.assertEqual(0, result)

    def test_reflection(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.reflection()
        self.assertTrue(isinstance(result, int))
        self.assertEqual(0, result)

    def test_rgb(self):
        sensor = ColorSensor(Port.S1)
        result = sensor.rgb()
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(3, len(result))
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])
        self.assertEqual(0, result[2])