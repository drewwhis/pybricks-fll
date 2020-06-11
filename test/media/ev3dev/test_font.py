from unittest import TestCase
from pybricks.media.ev3dev.__stub.__font import Font


class TestFont(TestCase):
    def test_constructor(self):
        try:
            Font()
            Font('test')
            Font('test', 24)
            Font('test', 24, True)
            Font('test', 24, True, True)
            Font('test', 24, True, True, 'test')
            Font('test', 24, True, True, 'test', 'test')
        except:
            self.fail()

    def test_default(self):
        self.assertIsNotNone(Font.DEFAULT)
        self.assertTrue(isinstance(Font.DEFAULT, Font))

    def test_properties(self):
        font = Font('a', 24, True, True, 'b', 'c')
        self.assertTrue(isinstance(font.family, str))
        self.assertEqual(font.family, '')
        self.assertTrue(isinstance(font.style, str))
        self.assertEqual(font.style, '')
        self.assertTrue(isinstance(font.width, int))
        self.assertEqual(font.width, 0)
        self.assertTrue(isinstance(font.height, int))
        self.assertEqual(font.height, 0)

    def test_text_width(self):
        font = Font()
        result = font.text_width('test')
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 0)

    def test_text_height(self):
        font = Font()
        result = font.text_height('test')
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 0)
