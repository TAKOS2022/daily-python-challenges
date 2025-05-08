"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""



def solution(s):
    print(len(s) % 2)
    result = [] # Result
    i = 0 # counter
    for char in s:
        if len(s) == 1: # Case we have one character
            result.append(char + '_') 
            break
        elif len(s) % 2 == 0: # Case we have an even (pair)
            if len(s) != i:
                result.append(s[i:i+2])
                i += 2
        elif len(s) % 2 == 1: # Case we have and odd (impair)
            if i == len(s) - 1: # Last iteration
                res_str = s[i] + '_'
                result.append(res_str)
                break
            result.append(s[i:i+2])
            i += 2
    return result

import re

"""
"."      Matches any character except a newline.
".."     2 consecutifs characters
{2}      Find 2 occurences of any character
s + "_"  Add "_" at the end of the string s. This ensure that the len of string is even (in case of odd)
"""
def solution_regex(s):
    return re.findall(".{2}", s + "_")
    return re.findall("..", s + "_")


if __name__ == "__main__":
    s = "abc"
    s1 = "abcdef"
    # print(solution(s))
    print(solution_regex(s))
