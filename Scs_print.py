# -- Byimaan -- 

'''
Given two strings X and Y, print the shortest string that has both X and Y as subsequences. If multiple shortest supersequence exists, print any one of them.

Examples:

Input: X = "AGGTAB",  Y = "GXTXAYB"
Output: "AGXGTXAYB" OR "AGGXTXAYB" 
'''

from Lcs_Top_down import LCS_Top_down

def shortest_cmn_str(str1,str2,get_length=False):

    m, n = len(str1), len(str2)

    if get_length:
        return m + n - LCS_Top_down(str1,str2)

    lcs_matrix = LCS_Top_down(str1,str2,get_matrix=True)
        
    scs = ''

    # our goal is to print the string   
        
    while m >  0 and n > 0:
        if str1[m-1] == str2[n-1]:
            scs += str1[m-1]
            m -= 1
            n -= 1

        else: 
            if lcs_matrix[m-1][n] > lcs_matrix[m][n-1] :

                scs += str1[m-1]
                m -= 1

            else:
                scs += str2[n-1]
                n -= 1

    if m > 0:
        while m != 0:
            scs += str1[m-1] 
            m -= 1

    elif n > 0:
        while n != 0:
            scs += str2[n-1]
            n -= 1

    #  we have to reverse the string for final answer ...
    return scs[::-1]                                


if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    
    print(shortest_cmn_str(X,Y))        