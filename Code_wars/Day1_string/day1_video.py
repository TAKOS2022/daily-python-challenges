"""
(This come from Codewars)

Convert all the first letters of each word in a string to uppercase.
Example:
Input: "How can mirrors be real if our eyes aren't real"
Ouput: "How Can Mirrors Be Real If Our Eyes Aren't Real"
[]

"""


def capitalize_words_basic(string):
    str_list = string.split()
    list_mot_capitalise = []
    str_output = ''
    for mot in str_list:
        if mot[0].islower():
            new_mot = mot[0].upper() + mot[1:]
            list_mot_capitalise.append(new_mot)
        else:
            list_mot_capitalise.append(mot)
    for mot in list_mot_capitalise:
        str_output += mot + ' '
    return str_output


def capitalize_words_advanced(string):

    return ' '.join([word.capitalize() for word in string.split()])


import string
def capitalize_words_master(string, sep=None):
    return (sep or ' ').join(map(str.capitalize, string.split(sep)))
    


if __name__ == "__main__":
    input = "How can mirrors be real if our eyes aren't real"
    print(string.capwords(input))