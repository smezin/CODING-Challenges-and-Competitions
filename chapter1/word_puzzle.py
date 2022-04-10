from collections import defaultdict
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = defaultdict(bool)











BOARD = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
WORDS = ["oath","pea","eat","rain"]