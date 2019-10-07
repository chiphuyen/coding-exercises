'''
This is a medium problem from leetcode.
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab" or
Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"

Note: should solve this in O(n^2)

Solution idea:
Go over each character in the string and find the longest palindrome
that is centered around that character.
A palindrome that centers around that character can either has odd length
or even length.
If it has odd length, the character is the exact center.
If it has even length, there are two cases:
    if the next character is the same as this, their combination is the center.
    if not, the longest palindrome with even length centered around
    that character is ''

'''


class Solution(object):
    def _helper(self, s, start, end, palin):
        while start >= 0 and end <= len(s) - 1:
            if s[start] != s[end]:
                break
            palin = s[start] + palin + s[end]
            start -= 1
            end += 1
        return palin

    def _get_palin(self, s, idx):
        palin1 = self._helper(s, idx - 1, idx + 1, s[idx])
        if idx == len(s) - 1 or s[idx] != s[idx + 1]:
            return palin1
        palin2 = self._helper(s, idx, idx + 1, '')

        return palin2 if len(palin1) <= len(palin2) else palin1

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        best_palin = s[:1]
        for i, char in enumerate(s):
            palin = self._get_palin(s, i)
            if len(palin) > len(best_palin):
                best_palin = palin
        return best_palin


def test():
    solver = Solution()
    assert solver.longest_palindrome('babad') in set(['bab', 'aba'])
    assert solver.longest_palindrome('cbbd') == 'bb'
    assert solver.longest_palindrome('') == ''
    assert solver.longest_palindrome('safljkl23kljaaa') == 'aaa'
    assert solver.longest_palindrome(
        'safasdfbbbabbl23kljaaa') in set(['bbabb', 'safas'])


test()
