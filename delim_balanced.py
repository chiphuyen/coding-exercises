'''
This problem is taken from
Stanford's CS 9: Problem-Solving for the CS Technical Interview.

Write a function that takes as input a string and returns
whether the parenthesis are "balanced".

If the candidate solves this question quickly, add the following difficulty:
the string may also contain "[]" or "{}". Return whether all three types of
brackets are balanced.

Example
"(())", "(()())", or "()(()())" should return true
 "(()" or "())" should return false

My solution:
    You can pass in a list of opening delimiters with
    a list of their corresponding closing delimiters.
    Returns True if all delims are balanced, False otherwise.

    The idea here is that everytime you encounter an opening delim of a
    certain type, increase the count for that delim by 1.
    When you encouter a closing delim:
        + decrease the count by 1
        + if the count now is negative, it's not balanced.

'''


def is_balanced(string, delims=[], closes=[]):
    offsets = [0 for _ in delims]
    delims_map = {delims[i]: i for i in range(len(delims))}
    closes_map = {closes[i]: i for i in range(len(closes))}

    for char in string:
        if char in delims_map:
            offsets[delims_map[char]] += 1
        elif char in closes_map:
            offsets[closes_map[char]] -= 1
            if offsets[closes_map[char]] < 0:
                return False
    for i in offsets:
        if i != 0:
            return False
    return True


assert not is_balanced('(()', delims=['('], closes=[')'])
assert is_balanced('(())', delims=['('], closes=[')'])
assert is_balanced('()(()())', delims=['('], closes=[')'])
assert is_balanced('()(()())()', delims=['('], closes=[')'])
assert is_balanced('(()())', delims=['('], closes=[')'])
assert not is_balanced('(()))', delims=['('], closes=[')'])
assert not is_balanced('(()))', delims=['(', '{'], closes=[')', '}'])
assert not is_balanced('(())){', delims=['(', '{'], closes=[')', '}'])
assert not is_balanced('(({)))}', delims=['(', '{'], closes=[')', '}'])
assert is_balanced('(({))()}', delims=['(', '{'], closes=[')', '}'])
assert not is_balanced('[(', delims=['(', '{', '['], closes=[')', '}', ']'])
assert is_balanced('()({(})([]))[()]',
                   delims=['(', '{', '['],
                   closes=[')', '}', ']'])
assert not is_balanced('()({(}{)([]))[()]',
                       delims=['(', '{', '['],
                       closes=[')', '}', ']'])
