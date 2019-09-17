'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.
'''

def firstNotRepeatingCharacter(s):
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
    for c in s:
        if count[c] == 1:
            return c
    return '_'
    
def firstNotRepeatingCharater_2(s):
    dictionary = {x:s.count(x) for x in s}
    for key, value in dictionary.items():
        if value == 1:
        return key
    return '_'

        
