'''Tests for GetAhead+ Week 5, Word Hunting'''

import unittest
from week5 import Dictionary, importDictionary, findLongestWord

class LongestWordTest(unittest.TestCase):
	def test_1(self):
		grid = [
			['a', 'x', 'v', 's'],
			['z', 'g', 'h', 'y'],
			['r', 'w', 'e', 'g'],
			['f', 'e', 't', 'r']
		]

		dictionary = importDictionary(Dictionary(), 'dictionary.txt')
		longestWord = findLongestWord(grid, dictionary)

		self.assertEqual(longestWord, ['agree'])


	def test_more_than_one_longest_word(self):
		grid = [
			['s', 'c', 'm', 'z'],
    		['r', 'e', 'a', 'x'],
    		['p', 'w', 'l', 't'],
   			['e', 'o', 'y', 'v']
		]

		dictionary = importDictionary(Dictionary(), 'dictionary.txt')
		longestWord = findLongestWord(grid, dictionary)

		self.assertEqual(longestWord, ['screw', 'meaty', 'elope'])

	def test_no_longest_word(self):
		grid = [
			['e', 'o', 'a', 'h'],
		    ['p', 'm', 'c', 't'],
		    ['e', 'p', 'o', 'e'],
		    ['v', 'r', 'i', 't']
	    ]

		dictionary = importDictionary(Dictionary(), 'dictionary.txt')
		longestWord = findLongestWord(grid, dictionary)
		
		self.assertEqual(longestWord, [''])

	def test_longest_word_appeared_more_than_once(self):
		grid = [
			['c', 'a', 'a', 't'],
		    ['h', 'h', 's', 'i'],
		    ['i', 't', 't', 'y'],
		    ['s', 't', 'y', 'i']
	    ]

		dictionary = importDictionary(Dictionary(), 'dictionary.txt')
		longestWord = findLongestWord(grid, dictionary)
		
		self.assertEqual(longestWord, ['chastity'])

	def test_word_isPrefix_and_isWord(self):
		grid = [
			['a', 'f', 'd', 'd'],
		    ['i', 'd', 'e', 'e'],
	        ['x', 'l', 'n', 'd'],
	        ['k', 'i', 'e', 'g']
        ]

		dictionary = importDictionary(Dictionary(), 'dictionary.txt')
		longestWord = findLongestWord(grid, dictionary)
		
		self.assertEqual(longestWord, ['addend'])


if __name__ == '__main__':
	unittest.main()