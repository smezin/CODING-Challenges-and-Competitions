from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dests = defaultdict(list)
        for departue, arrival in tickets:
            dests[departue].append(arrival)
        for key in dests:
            dests[key].sort(reverse=True)
        print(dests)
        path = ['JFK']
    
        def dfs(current):
            print(path, current)
            if len(path) == len(tickets) + 1:
                return path.append(current)
            if current in dests:
                next_dest = dests[current].pop()
                path.append(next_dest)
                return dfs(next_dest)
            return
        dfs('JFK')

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

s = Solution()
s.findItinerary(tickets)