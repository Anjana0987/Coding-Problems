'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

'''

def almostIncreasingSequence(sequence):
      #Take out the edge cases
    if len(sequence) <= 2:
        return True

    def increase(test):
        if len(test) == 2:
            return test[0] < test[1]
               
        else:
            for i in range(0, len(test)-1):
                if test[i] >= test[i+1]:
                    return False
            return True
                   
    for i in range (0, len(sequence) - 1):
        if sequence[i] >= sequence [i+1]:
            test_seq1 = sequence[:i] + sequence[i+1:]
            test_seq2 = sequence[:i+1] + sequence[i+2:]
            return increase(test_seq1) == True or increase(test_seq2) == True
              
