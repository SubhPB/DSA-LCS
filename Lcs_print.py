#  -- Byimaan -- 

# DSA --> LCS --> by Top Down

'''
Longest Common Subsequence Problem solution using Top_down
Given two sequences, print the longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

For example, “abc”,  “abg”, “bdf”, “aeg”,  ”acefg”, .. etc are subsequences of “abcdefg”.
'''

from Lcs_Top_down import LCS_Top_down

def print_lcs(str1,str2):

    matrix = LCS_Top_down(str1,str2,get_matrix=True)

    m, n = len(str1), len(str2)
    rev_lcs = ''

    while m != 0 and n != 0:

        if  str1[m-1] == str2[n-1]:
            rev_lcs += str1[m-1]
            m -= 1
            n -= 1 

        else: 
            if matrix[m][n] == matrix[m-1][n]:
                m -= 1

            elif matrix[m][n] == matrix[m][n-1]:
                n -= 1        

    print(rev_lcs[::-1])         
    

if __name__ == '__main__':

    str1 = "abcdgh"
    str2 = "abedfha"

    print_lcs(str1,str2)    