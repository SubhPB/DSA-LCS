#  -- Byimaan -- 

# DSA --> LCS --> by Recursion

'''
Longest Common Subsequence Problem solution using recursion
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

For example, “abc”,  “abg”, “bdf”, “aeg”,  ”acefg”, .. etc are subsequences of “abcdefg”.
'''

def LCS_by_recursion(seq1 : str,seq2 : str ,l_1 : int or None = None,l_2: int or None = None) -> int:

    #  l_1 and l_2 represents the length of corresponding

    if (l_1 == None or l_2 == None):
       l_1, l_2 = len(seq1), len(seq2)

    # Base Case
    if (l_1 <= 0 or l_2 <= 0):
        # if one of them 's length s zero there will be no more longest subsequence possible.
        return 0
    
    # We will compare the chars of both given string from the ends of string. [ right end  to left end ]

    if (seq1[l_1 - 1] == seq2[l_2 - 1]):
        # If both chars are the same then we want to increment the result by one.
        #  decrement the l_1 and l_2 by one. So, we can reach the next char for comparsion.

        return 1 + LCS_by_recursion(seq1,seq2,l_1-1,l_2-1)
    
    else:
        #  If they are not same then we have two choices either to decrement the l_1 or l_2.
        # we will choose one that maximize our result. like following

        first_choice = LCS_by_recursion(seq1,seq2,l_1-1,l_2)

        second_choice = LCS_by_recursion(seq1,seq2,l_1,l_2-1)

        # As per condition, two chars were not equal during comparsion so we will not increment 1 as we did in 'if' statement  
        return max(first_choice,second_choice)
    

if __name__ == '__main__':

    #  testing --> 
    str1 = "abcdgh"
    str2 = "abedfha"

    print(LCS_by_recursion(str1,str2,6,7))    
