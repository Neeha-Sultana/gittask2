def treePoints(g_nodes, g_from, g_to, A, K):
    from collections import defaultdict
    
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for u, v in zip(g_from, g_to):
        tree[u].append(v)
        tree[v].append(u)
    
    # To store the maximum points collected
    total_points = 0
    
    # DFS function to traverse the tree
    def dfs(node, parent):
        nonlocal total_points
        
        # Initial value collected from the node using Method 1
        method1_points = A[node] - K
        
        # Collect points from the node using Method 1 if it's valid
        if method1_points > 0:
            total_points += method1_points
        
        # Prepare to collect points using Method 2
        subtree_points = 0
        # Iterate through the children
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            
            # Recursive DFS call
            child_points = dfs(neighbor, node)
            
            # Calculate points for Method 2 (floor division)
            subtree_points += child_points // 2
        
        # Collect points from the node using Method 2 if the current value is positive
        if A[node] > 0:
            total_points += A[node] // 2
            
            # Update the current node's value after using Method 2
            A[node] //= 2
        
        return subtree_points + A[node]
    
    # Start DFS from the root node (0) with no parent (-1)
    dfs(0, -1)
    
    return total_points

# Example test case
g_nodes = 2
g_edges = 1
g_from = [0]
g_to = [1]
A = [15,10]
K = 7

# Function call
print(treePoints(g_nodes, g_from, g_to, A, K))  # Output should be 11



"""
from itertools import combinations

def findLongestSubsequence(arr):
    n = len(arr)
    max_len = 0
    
    # Generate all subsequences by iterating over every possible length
    for r in range(2, n + 1):  # Subsequence length should be at least 2
        for subseq in combinations(arr, r):
            sorted_subseq = sorted(subseq)
            sum_diff = 0
            
            # Calculate the sum of differences
            for i in range(1, len(sorted_subseq)):
                sum_diff += sorted_subseq[i] - sorted_subseq[i - 1]
            
            # Check if the sum of differences is even
            if sum_diff % 2 == 0:
                max_len = max(max_len, len(sorted_subseq))
    
    return max_len

# Example usage:
arr = [87,99,85,50,93]
print(findLongestSubsequence(arr))  # Output should be 6


"""
