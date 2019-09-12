'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
'''
def isLucky(n):
    num_list = [int(x) for x in str(n)]
    length = len(num_list)//2
    return sum(num_list[:length]) == sum(num_list[length:])
