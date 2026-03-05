from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0

    while(location <= n and S[location] != x):
        location = location + 1

    if(location > n):
        location = 0

    # Complete the code here
    return location