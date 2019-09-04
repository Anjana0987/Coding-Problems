'''
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
'''
def checkPalindrome(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False
    
