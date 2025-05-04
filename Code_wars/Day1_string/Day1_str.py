import string

"""
(This come from Codewars)

Convert all the first letters of each word in a string to uppercase.
Example:
Input: "How can mirrors be real if our eyes aren't real"
Ouput: "How Can Mirrors Be Real If Our Eyes Aren't Real"

"""

"""
knowledge:
- string.split() : split a string into a list of words
- str[0].upper() : convert the first letter of a string to uppercase
- str[1:] : get the rest of the string after the first letter
- str.join() : join a list of strings into a single string with a separator (Space in this case). We use to concatenate elements of an iterable (list, tuple or set)
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


"""
Adavanced knowledge:
- list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

newlist = [x for x in fruits if "a" in x]

- str.capitalize() : convert the first letter of a string to uppercase and the rest to lowercase
"""
def capitalize_words_advanced(string):
    # Use a list comprehension to capitalize the first letter of each word
    return ' '.join([word.capitalize() for word in string.split()])



"""
Master knowledge: string.capwords(input_string) 
- The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

"""
# Capitalize the words in a string, e.g. " aBc  dEf " -> "Abc Def".
def capitalize_words_master(string, sep=None):
    """capwords(s [,sep]) -> string

    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join.  If the optional second argument sep is absent or None,
    runs of whitespace characters are replaced by a single space
    and leading and trailing whitespace are removed, otherwise
    sep is used to split and join the words.

    """
    return (sep or ' ').join(map(str.capitalize, string.split(sep)))


if __name__ == "__main__":
    # Test the function with an example input
    input_string = "How can mirrors be real if our eyes aren't real"
    print("Basic output : " + capitalize_words_basic(input_string))
        
    print("Advanced output : " + capitalize_words_advanced(input_string))

    print("Advanced 2 output : " + string.capwords(input_string))
    print("Advanced Python output : " + string.capwords(input_string))