'''
This problem is taken from Stanford's CS 9: Problem-Solving for the CS Technical Interview.

Question statement:
Reverse all the words in a string of words and spaces / tabs
while preserving the word order and spacing.
Example
'moo cow bark dog' -> 'oom woc krab god'

Potential pitfalls:
Don't reverse the entire string -- preserve the word ordering and the spaces.
We make no guarantee about how many spaces / tabs there are between words,
so you can't split (using the .split() method) and then reverse
the words individually.

My solution:
Start with current word to be None.
Iterate over each character in the string.
    + if it's space/tabs:
        + if the current word is not None, reverse it and add it to result.
        + add current character to the result.
    + else:
        + if the previous character is space/tab, make it the first 
        character of current word.
        + else, add the current character to the current word

'''


def reverse_string(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string(string[:-1])


def reverse_words(string):
    curr_word = ''
    results = ''
    for char in string:
        if char == ' ' or char == '\t':
            if not curr_word == '':
                results += reverse_string(curr_word)
                curr_word = ''
            results += char
        else:
            curr_word += char
    results += reverse_string(curr_word)
    return results


assert reverse_words('moo cow  bark dog') == 'oom woc  krab god'
assert reverse_words('moo  ') == 'oom  '
assert reverse_words('  moo moo') == '  oom oom'
assert reverse_words('  ') == '  '
