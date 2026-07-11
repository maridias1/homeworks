1. 
def group_lists(list1, list2):
    zipped = zip(list1, list2)
    result = []
    for pair in zipped:
        result.append(str(pair))
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(group_lists(list1, list2))

2.
from functools import reduce

def calculate(numbers):
    try:
        result = reduce(lambda x, y: x * y, numbers)
        return result
    except TypeError:
        return "Error"

numbers = [1, 2, 3, 4, 5]
print(calculate(numbers))

3.
numbers = [1, 2, 3, 4, 5, 6, 7]
get_odds = lambda lst: [x for x in lst if x % 2 != 0]
print(get_odds(numbers))

4. 
def check_words(strings_list, ending):
    try:
        result = list(filter(lambda s: s.endswith(ending), strings_list))
        return result
    except TypeError:
        return "Type Error"
    except Exception:
        return "Error"

words = ['hello', 'world', 'coding', 'nod']
suffix = 'ing'
print(check_words(words, suffix))