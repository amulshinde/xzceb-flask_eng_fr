"""
write the unit test for the English to French translator and
French to English translator function in test.py 
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
	def test1(self):
		self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
	def test1(self):
		self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()