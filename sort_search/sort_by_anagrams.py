def sort_by_anagrams(arr):
    dic = {}
    for word in arr:
        s_word = ''.join(sorted(word))
        if dic.get(s_word) is not None:
            dic.update({s_word: dic.get(s_word) + [word]})
        else:
            dic.update({s_word: [word]})
    res = [word for sublist in dic.values() for word in sublist]
    print(res)

sort_by_anagrams(['abc', 'ba', 'xvx', 'bca', 'popo', 'baca', 'bac', 'poop', 'ab'])

#O(nk)