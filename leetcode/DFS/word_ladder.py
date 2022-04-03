from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.endword = endWord
        self.word_dict = defaultdict(list)
        self.path = []
        self.shortest = []
        wordList.append(beginWord)
        for word in wordList:
            self.word_dict[word] = [wordList.pop() for i in range(len(wordList)-1, -1, -1) if sum(a!=b for a, b in zip(word, wordList[i])) == 1]

        print(self.word_dict)
        self.dfs(beginWord)
        return self.path
        
    def dfs(self, word):
        if word == self.endword:
            if not self.shortest:
                self.shortest = self.path
            elif len(self.path) < len(self.shortest):
                self.shortest = self.path
        while self.word_dict[word]:
            next_word = self.word_dict[word].pop()
            self.dfs(next_word)
            self.path.append(word)
        return self.shortest

s = Solution()
a = s.ladderLength( beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
print(a)