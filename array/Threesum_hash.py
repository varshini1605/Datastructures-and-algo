def threesum(arr):
    n=len(arr)
    hashset=set(arr)
    for i in range(n-2):
        for j in range(1,n-1):
            if (i+j)* -1 in hashset:
                return True
            
    return false
        
if __name__=="__main__":
    arr = [0, -1, 2, -3, 1]
    print(threesum(arr))

"""Time Complexity: O(n2), Since two nested loops are required, so the time complexity is O(n2).
Auxiliary Space: O(n), Since a HashSet is required, so the space complexity is linear."""

#With sorting and 2 pointers :
"""Time Complexity: O(n2), Only two nested loops are required, so the time complexity is O(n2).
Auxiliary Space: O(1), no extra space is required, so the space complexity is constant."""
