"""
(This come from Codewars)

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
Example:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

"""
knowledge:
- Continue: continue statement is used to skip the current iteration of a loop and move to the next iteration.
- Pass: pass statement is a null operation; it is a placeholder that does nothing when executed. It is often used in situations where syntactically some code is required but no action is needed.


"""
def filter_list_basic(l):
    result = []
    for element in l:
        if type(element) == str:
            continue
            result.append(0)
        else:
            result.append(element)
    return result

""""
 Knowledge:
 - isinstance: isinstance() is a built-in function in Python that checks if an object or variable is an instance of a specified class or data type.
"""
def filter_list_medium(l):
    return [item for item in l if isinstance(item, int)]

"""
Knowledge:
- The filter(func, iterable) function returns an iterator where the items are filtered through a function to test if the item is accepted or not..
- lambda arguments : expression : A lambda function is a small anonymous function that can take any number of arguments but can only have one expression. It is often used for short, throwaway functions.
"""
def filter_list_advanced(lst):
    return list(filter(lambda x: isinstance(x, int), lst))



if __name__ == "__main__":
    print(filter_list_basic([1,2,'a','b']))
    print(filter_list_medium([1,2,'a','b'])) 
    print(filter_list_advanced([1,2,'a','b'])) 
    

  