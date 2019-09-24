'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''

def palindromeRearranging(inputString):
    sample = set()
    for i in inputString:
        if i in sample:
            sample.remove(i)
        else  :
            sample.add(i)
    
    return len(sample) <= 1
