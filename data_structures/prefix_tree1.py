from typing import List

END_OF_WORD = '**'

class Trie:
    def __init__(self) -> None:
        self.root = dict()

    def insert (self, *words: List[str]) -> None:
        for word in words:
            current_dict = self.root
            for ch in word:
                current_dict = current_dict.setdefault(ch, {})
            current_dict[END_OF_WORD] = END_OF_WORD

    def search (self, word: str) -> bool:
        current_dict = self.root
        for ch in word:
            if ch not in current_dict:
                return False
            current_dict = current_dict[ch]
        return END_OF_WORD in current_dict
              
    def list_words(self, ch_dict: dict) -> List[str]:
        words = []
        for ch, next_ch_dict in ch_dict.items():
            if ch != END_OF_WORD:
                for next_ch in self.list_words(next_ch_dict):
                    words.append(ch + next_ch)
            else:
                words.append('')
        return words

    def list_starts_with(self, prefix: str) -> List[str]:
        current_dict = self.root
        for ch in prefix:
            if ch not in current_dict.keys():
                return []
            current_dict = current_dict[ch]
        return [prefix + suffix for suffix in self.list_words(current_dict)]


trie =Trie()
trie.insert('abc', 'ab', 'abcde', 'xy', 'wxy', 'xyz')
print('all:', trie.list_words(trie.root))

search_item = 'abcx'
print(f'word: {search_item} is {"in" if trie.search(search_item) else "not in"} trie')
prefix = 'x'
print(f'starts with-> {prefix}: {trie.list_starts_with(prefix)}')

            
