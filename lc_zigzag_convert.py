'''
This problem is from leetcode.com
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on
a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion
given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

My solution:
    I just worked out the formula to convert the index of the original string
    to the index of the new zigzag string.

There are two versions:
    The first one I like, but is rejected by leetcode for being too slow.
    The secone one is the hacky one that is accepted by leetcode
'''


class Solution(object):
    '''
    This solution is not accepted by leetcode for being too slow.
    '''

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        line = ''
        skip = 2 * numRows - 2
        for i in range(numRows):
            idx = set([i])
            if i != 0 and i != numRows - 1:
                idx.add(skip - i)
            line += ''.join([s[j] for j in range(len(s)) if j % skip in idx])
        return line


class Solution(object):
    '''
    This solution is accepted by leetcode.
    '''

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        if len(s) <= numRows:
            return s
        line = []
        skip = 2 * numRows - 2
        intervals = len(s) / skip
        for i in range(numRows):
            mods = [i]
            if i != 0 and i != numRows - 1:
                if skip - i < len(s):
                    mods.append(skip - i)
            idx = [j * skip + mod for j in range(intervals) for mod in mods]
            for mod in mods:
                if skip * intervals + mod < len(s):
                    idx.append(skip * intervals + mod)
            line += [s[j] for j in idx]
        return ''.join(line)
