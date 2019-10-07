'''
Two strings are said to be anagrams of one another if you can turn the
first string into the second by rearranging its letters.

For example, "table" and "bleat" are anagrams, as are "tear" and "rate."
Your job is to write a function that takes in two strings as input and
determines whether they're anagrams of one another.

Solution should run in O(n1 + n2)
There are two solutions:
    one is using counter
    another one is also using dictionary. I thought it'd be faster,
    but thanks @shubham8111 for pointing out, it's faster for strings
    of less than 100 characters, then its performance gets worse.

'''
from collections import Counter
import random
import string
import time


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


def create_random_anagrams(n=10000):
    characters = []
    for c in range(n):
        characters.append(random.choice(string.ascii_letters))
    str1 = ''.join(characters)
    random.shuffle(characters)
    str2 = ''.join(characters)
    return str1, str2


def time_test(str1, str2):
    start = time.time()
    assert are_anagrams(str1, str2)
    print('Time:', time.time() - start)
    start = time.time()
    assert are_anagrams_fast(str1, str2)
    print('Time:', time.time() - start)


test(are_anagrams)
test(are_anagrams_fast)
str1, str2 = create_random_anagrams()
time_test(str1, str2)
