import unittest
import sys

sys.path.insert(0, "../translator")

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(), None)
        self.assertEqual(englishToFrench(""), None)

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(), None)
        self.assertEqual(frenchToEnglish(""), None)

unittest.main()