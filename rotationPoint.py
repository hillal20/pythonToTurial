# Let's say we're given an alphabetically-sorted list of words that has been rotated at a single point. It might look something like this:

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'Othellolagkage',
]

# Write a function that, given a list of words such as this, returns the index of the rotation point. You can assume that no words will be duplicated.

# print(find_rotation_point(words))  # returns 5

# Can you do this with O(lg n) runtime complexity?


def find_rotation_point(words):
    newWords = []
    newWordsAscii = []
    for element in words:
        print(element[0].lower())
        newWords += element[0].lower()
        # print(ord(element[0]))
    print(newWords)
    newWordsAscii = [ord(element) for element in newWords]
    print(newWordsAscii.index(min(newWordsAscii)))
    return newWordsAscii.index(min(newWordsAscii))


find_rotation_point(words)
