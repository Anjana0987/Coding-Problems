'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''
def sortByHeight(a):
    one_positions = []
    for i in range(len(a)):
        if a[i] == -1:
            one_positions.append(i)
    while -1 in a:
        a.remove(-1)
    a = sorted(a)
    for i in one_positions:
        a.insert(i, -1)
    return a
