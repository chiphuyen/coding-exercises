'''
Question statement:
Return the longest contiguous substring of 2 distinct characters from an
input string.

Example
input: abbaacab
output : abbaa

input: abcefabbabaabefghghfa
return: abbabaab

input: aabceddddcdccecabceftg
return: ddddcdcc

input: acbabbcbca
return : bbcbc
'''


def max_contiguous(string):
    if len(string) <= 2:
        return string

    curr_max_str = curr_blob = string[:2]
    char0, char1 = string[0], string[1]
    last_char = char1
    if char0 == char1:
        last_contiguous_idx = 0
        last_last_char = None
    else:
        last_contiguous_idx = 1
        last_last_char = char0

    for i, char in enumerate(string[2:]):
        if last_last_char is None:
            curr_blob += char

            if char != last_char:
                last_contiguous_idx = i + 2
                last_last_char = last_char
                last_char = char
        else:
            if char == last_char:
                curr_blob += char
            elif char == last_last_char:
                curr_blob += char
                last_contiguous_idx = i + 2
                last_last_char = last_char
                last_char = char
            else:
                curr_blob = string[last_contiguous_idx: i + 3]
                last_contiguous_idx = i + 2
                last_last_char = last_char
                last_char = char

        if len(curr_blob) > len(curr_max_str):
            curr_max_str = curr_blob[:]

    return curr_max_str


assert max_contiguous('abbaacab') == 'abbaa'
assert max_contiguous('abcefabbabaabefghghfa') == 'abbabaab'
assert max_contiguous('aabceddddcdccecabceftg') == 'ddddcdcc'
assert max_contiguous('acbabbcbca') == 'bbcbc'
assert max_contiguous('') == ''
assert max_contiguous('aaaaaaaa') == 'aaaaaaaa'
assert max_contiguous(
    'aaaaabbbbb3dasfa938209320202020202020202') == '20202020202020202'
assert max_contiguous(
    'aaaaabbbbb3dasfa938209320202020202020202afdafsfasdweeweeeeee') == '20202020202020202'
