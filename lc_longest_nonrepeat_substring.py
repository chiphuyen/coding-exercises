'''
This problem is from leetcode
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string, find the length of the longest substring without
repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not
a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        max_str = curr_blob = s[:1]
        for char in s[1:]:
            if char not in set(list(curr_blob)):
                curr_blob += char
            else:
                idx = curr_blob.find(char)
                curr_blob = curr_blob[idx + 1:] + char
            if len(curr_blob) > len(max_str):
                max_str = curr_blob
        return len(max_str)
