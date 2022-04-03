import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        with self.assertRaises(Exception) as context:
            english_to_french(None)
        self.assertTrue('text must be provided' in str(context.exception))
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        with self.assertRaises(Exception) as context:
            french_to_english(None)
        self.assertTrue('text must be provided' in str(context.exception))
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        
unittest.main()