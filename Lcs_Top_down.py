#  -- Byimaan -- 

# DSA --> LCS --> by Top Down

'''
Longest Common Subsequence Problem solution using recursion (Memo)
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

For example, “abc”,  “abg”, “bdf”, “aeg”,  ”acefg”, .. etc are subsequences of “abcdefg”.
'''


def LCS_Top_down(str1,str2):

    #  if length of str1 or str2 is zero then 'LCS' will also be zero else we will put default value of -1.
    matrix = [ [ 0 if (c == 0 or r == 0) else -1 for c in range(len(str2) + 1)] for r in range(len(str1) + 1) ]


    # just for example if m=1 and n=1 means matrix[m][n] will refers to str1[m-1] and str2[n-1]
    for m in range(1,len(str1) + 1):
        # m for targeting str1 elements - row wise
        for n in range(1,len(str2) + 1):    
            #  n for targeting str2 elements - column wise

            if str1[m-1] == str2[n-1]:

                matrix[m][n] = 1 + matrix[m-1][n-1]

            else:

                matrix[m][n] = max(matrix[m][n-1],matrix[m-1][n])        

    return matrix[len(str1)][len(str2)]                

if __name__ == '__main__':

    str1 = "abcdgh"
    str2 = "abedfha"

    print(LCS_Top_down(str1,str2)) 