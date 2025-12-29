#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#

from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        adj = defaultdict(set) # add possible nodes as neighbors to the node containing the bottom two

        for u, v, w in allowed:
            adj[(u, v)].add(w)

        visited = set()

        def get_next_floor(bottom):
            candidates = ['']
            for i in range(1, len(bottom)):
                base = (bottom[i - 1], bottom[i])
                possibilities = adj[base]

                if possibilities:
                    candidates = [a + e for e in possibilities for a in candidates]
                else:
                    return []
            
            return candidates

        def dfs(node):
            if len(node) == 1:
                return True # the fact that we reached this point means this was a valid block
            
            for candidate in get_next_floor(node):
                if dfs(candidate):
                    return True

            visited.add(node)

            return False

        return dfs(bottom)
                
        
# @lc code=end

