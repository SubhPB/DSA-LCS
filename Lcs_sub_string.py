#  -- Byimaan -- 

# DSA --> LCS --> by Top Down

'''
Longest Common Substring Problem solution
Given two sequences, find the length of longest subsrting present in both of them.

'''


def length_of_lng_cmn_substr(str1,str2,get_matrix=False,get_length=False):

    l1, l2 = len(str1), len(str2)

    matrix = [ [0 if ( r==0 or c==0) else -1 for c in range(l2+1)] for r in range(l1+1) ]

    #  longest refers to the length of longest substr
    longest = 0
    position = {'m':-1,'n':-1}

    for m in range(1,l1+1):
        for n in range(1,l2+1):

            if str1[m-1] == str2[n-1]:
                matrix[m][n] = 1 + matrix[m-1][n-1]

                if matrix[m][n] > longest:
                    longest = matrix[m][n]
                    position['m'], position['n'] = m,n

            else:
                matrix[m][n] = 0

     
    if get_matrix:
        return matrix  

    if get_length:
        return longest 
    
    print(' start ', position['m'] - 1 - longest)
    print(' end ', position['m'])
    
    lng_substr = str1[ position['m'] - longest : position['m'] ]

    return lng_substr 


if __name__ == '__main__':
    str1 = "lhbadgh"
    str2 = "aedfhba"

    #  to visualise the matrix will help to understand and approach the problem better.
    for r in length_of_lng_cmn_substr(str1,str2,get_matrix=True):
        print(r)

    # our final answer ->
    print(length_of_lng_cmn_substr(str1,str2))