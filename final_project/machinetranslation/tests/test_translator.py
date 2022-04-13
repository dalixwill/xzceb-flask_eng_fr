import unittest
import sys

sys.path.insert(0, "../translator")

from translator.translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(), None)
        self.assertEqual(englishToFrench(""), None)

    def test_assertNotEqual(self):
        self.assertNotEqual(englishToFrench("Hello"), "Au Revoir")
        self.assertNotEqual(englishToFrench(""), "")
        self.assertNotEqual(englishToFrench(None), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(), None)
        self.assertEqual(frenchToEnglish(""), None)

    def test_assertNotEqual(self):
        self.assertNotEqual(frenchToEnglish("Au Revoir"), "Hello")
        self.assertNotEqual(frenchToEnglish(), "")
        self.assertNotEqual(frenchToEnglish(""), "Hello")

if __name__ == "__main__":
    unittest.main()