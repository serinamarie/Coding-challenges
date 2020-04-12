# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # output: min number of deletions as int
    # input: number of queries as int, a bunch of queries
    # constraints: must be at least 1 query
    # edge cases: if query has a length of 1
    

        # if next char different from last_valid_char:
            # last_valid_char = curr_char
            # move on to the next char
        # if next char same as last_valid_char:
            
            # deletions += 1
 
    # return deletions

    # FIRST PASS SOLUTION

    # # start with no deletions, last valid char is the starting char
    # deletions = 0
    # last_valid_char = s[0]
    
    # # iterate through
    # for i in range(len(s)-1):

    #     # if the next char is different from the last valid char
    #     if s[i+1] != last_valid_char:

    #         # update the last valid char
    #         last_valid_char = s[i+1]
            
    #     # if next char is same as last valid char
    #     else:

    #         # increase deletion count
    #         deletions += 1
            
    # return deletions

    # FINAL SOLUTION

    # start with no deletions
    deletions = 0
    
    # iterate through
    for i in range(len(s)-1):

        # if the next char is different from the curr char
        if s[i+1] != s[i]:
            
            # ignore
            continue
            
        # if next char is same as last valid char, increase deletion count
        deletions += 1
            
    return deletions