import collections
from typing import Deque

class Dictionary:
    '''A dictionary that implements Trie structure'''

    def __init__(self):
        self.end = '*'
        self.trie = dict()

    def __repr__(self):
        return repr(self.trie)

    def isWord(self, word):
        word = word.upper()
        subTrie = self.trie

        for letter in word:
            if letter in subTrie:
                subTrie = subTrie[letter]
            else:
                return False

        if self.end in subTrie:
            return True
        return False

    def isPrefix(self, word):
        word = word.upper()
        subTrie = self.trie
        
        for letter in word:
            if letter in subTrie:
                subTrie = subTrie[letter]
            else:
                return False

        return True


    def addToDict(self, word):
        word = word.upper()

        # If word already in dictionary,
        # Return trie so that lines 51-61 will be skipped
        # This will improve the algorithm's overall time
        if self.isWord(word):
            return self.trie

        subTrie = self.trie

        for letter in word:
            if letter in subTrie:
                subTrie = subTrie[letter]
            else:
                subTrie = subTrie.setdefault(letter, {})

        subTrie[self.end] = self.end

        return subTrie


def importDictionary(dictionary, pathToText):

    '''Reads a txt file and adds all the words in it to the dictionary.

    Args:
        dictionary: The dictionary where new words will be added.
        pathToText: The location of the txt file that contains valid words.

    Returns:
        The dictionary with new words added to it.
    '''
    with open(pathToText,'r') as file:
        for word in file.read().splitlines(): 
            dictionary.addToDict(word)

    return dictionary

def findLongestWord(grid, dictionary):

    '''Finds the longest word from the dictionary that can be formed in the grid.

    Args:
        grid: The grid to be traversed to find the longest word.
        dictionary: The reference that will be used to check whether a string is a prefix or word.

    Returns:
        The longest word(s) that can be found in the grid.
    '''

    queue = collections.deque([])
    prefixes = collections.deque([])
    longestWord = ['']
    
    width, height = len(grid[0]), len(grid)

    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    for xCoord in range(len(grid)):
        for yCoord in range(len(grid[xCoord])):

            visited = [[False] * width for i in range(height)]

            currLocation = (xCoord, yCoord)
            queue.append(currLocation)
            prefixes.append(grid[xCoord][yCoord])            

            # Start of BFS
            while (len(queue) > 0):
                visited[xCoord][yCoord] = True

                currX, currY = queue.popleft()
                string = prefixes.popleft()

                for d in directions:
                    xDir, yDir = d
                    newX = currX + xDir
                    newY = currY + yDir

                    if (0 <= newX < width and 0 <= newY < height and visited[newX][newY] == False):

                        newStr = string + grid[newX][newY]

                        if dictionary.isPrefix(newStr):
                            queue.append((newX, newY))
                            prefixes.append(newStr)

                        if dictionary.isWord(newStr):
                            if len(longestWord[0]) < len(newStr):
                                longestWord.clear()
                                longestWord.append(newStr)

                            if len(longestWord[0]) == len(newStr) and newStr not in longestWord:
                                longestWord.append(newStr)
    return longestWord
