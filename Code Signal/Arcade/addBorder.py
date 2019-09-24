'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''
def addBorder(picture):
    pic = []
    pic.append('*' * (len(picture[0]) + 2))
    for i in range(len(picture)):
        pic.append('*' + picture[i] + '*')
    pic.append('*' * (len(picture[0]) + 2))
    return pic
