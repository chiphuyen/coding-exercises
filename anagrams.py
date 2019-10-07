'''
Two strings are said to be anagrams of one another if you can turn the
first string into the second by rearranging its letters.

For example, "table" and "bleat" are anagrams, as are "tear" and "rate."
Your job is to write a function that takes in two strings as input and
determines whether they're anagrams of one another.

Solution should run in O(n1 + n2)
There are two solutions:
    one is using counter
    another one is also using dictionary, but slightly faster.
'''
from collections import Counter


def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    dict1 = Counter(list(str1))
    dict2 = Counter(list(str2))
    for char in dict1:
        if char not in dict2 or dict2[char] != dict1[char]:
            return False
    return True


def are_anagrams_fast(str1, str2):
    if len(str1) != len(str2):
        return False

    char_dict = {}
    for char in str1:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

    for char in str2:
        if char not in char_dict or char_dict[char] <= 0:
            return False
        char_dict[char] -= 1
    return True


def test(anagram_fn):
    print('Testing ', anagram_fn)
    assert anagram_fn('table', 'bleat')
    assert not anagram_fn('table', 'bleate')
    assert anagram_fn('honey', 'eyhon')
    assert not anagram_fn('area', 'are3')
    assert not anagram_fn('', ' ')


test(are_anagrams)
test(are_anagrams_fast)
