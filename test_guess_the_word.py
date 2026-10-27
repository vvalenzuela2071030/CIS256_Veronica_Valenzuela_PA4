# Veronica Valenzuela 
# CIS256 Fall 2026
# Programming Assignment 4

""" Write tests using pytest"""

import unittest
from guess_the_word import get_word, play  

# Test: Does the word select come from the predified list?
class TestGuessTheWord(unittest.TestCase):
    def test_get_word(self):
        word = get_word()
        self.assertIn(get_word(), words)

if __name__ == "__main__"":
    unittest.main()



# Test: Number of incorrect guesses; should not be more than 6 incorrect guesses.
class TestIncorrectGuesses(unittest.TestCase):
    def test_tries_does_not_exceed_six(self):
        self.assertEqual(remaining_tries(0), 6)
        self.assertEqual(remaining_tries(4), 4)
        self.assertEqual(remaining_tries(6), 0)
        self.assertEqual(remaining_tries(7), 0)

        
if __name == "__main__":
    unittest.main()





