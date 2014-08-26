# Collecting a Bunch of named items

class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


import operator
class MurkierBunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def __getitem__(self, key):
        return operator.getitem(self.__dict__, key)
    def __setitem__(self, key, value):
        return operator.setitem(self.__dict__, key, value)
    def __delitem__(self, key):
        return operator.delitem(self.__dict__, key)


class MurkierBunch2(dict):
    def __init__(self, **kwargs):
        dict.__init__(self, **kwargs)
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

# however, the above two are not preferable. Use getattr, setattr and delattr


# Assigning and testing in one statement

"""
To imitate (e.g. in C):

while (x=foo()) {
  bar(x)
}

i.e. do something with x while is True

"""

class DataHolder:
    def __init__(self, value=None):
        self.value = value
    def set(self, value):
        self.value = value
        return value
    def get(self):
        return self.value


"""
data = DataHolder()

while data.set(foo()):
    bar(data.get())

"""

# Get the intersect of two dicts

# >>> print [k for k in some_dict if k in another_dict]

# or

# >>> print filter(some_dict.has_key, another_dict.keys())


# flattening a deeply-nested list
# -----------------

# define a function `is_scalar` that returns True or False based on whether
# and item is scalar or not

def flatten(sequence, item_is_scalar, result=None):
    if result is None: result = []
    for item in sequence:
        if item_is_scalar(item):
            result.append(item)
        else:
            flatten(item, item_is_scalar, result)
    return result

# if memory is an issue, generators can be used instead

# a definition of `is_scalar`. 
# check if item is iterable using built-in `iter`

def is_scalar(item):
    try: iter(item)
    except: return True
    else: return False

# however a string will cause cause: RuntimeError: maximum recursion depth exceeded
# Why? 

# upgrade is_scalar to treat strings as scalar items

def is_string(item):
    try:
        item + ''
    except TypeError:
        return False
    else:
        return True

def is_scalar_upgraded(item):
    return is_string(item) or is_scalar(item)

# see related: http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python


# Pairing each item in a list to each item in another list
# >>> a = [1, 2, 3]
# >>> b = [4, 5]
# [(x, y) for x in a for b in y]
# i.e. looping over b for each item in a


# Transposing a 2d array
# array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# [[row[col] for row in arr] for col in range(len(array[0]))]


# Looking up many items in a long list
# ------------------------------------
# >>> import bisect
# >>> the_list.sort()
# >>> the_item = foo
# >>> insertion_point = bisect.bisect(the_list, the_item)
# >>> exists = the_list[insertion_point-1:insertion_point] == [the_item]

# Why slicing?
# What about using an auxilliary dictionary?
# Why not brute force comparisons?


# Finding the list of indices leading to an item in a deeply nested sequence
# --------------------------------------------------------------------------
import types, sys

class ItemFound(Exception):
    """Raised when the item is found storing the list of indices """

    def __init__(self, path):
        self.path = path

def find_indices_path(sequence, target):
    """Finds the list of indices into sequence that will get you to target

    If item is found, returns the list of indices, otherwise returns None"""

    def is_sequence(item):
        """Returns true if item is list or tuple"""

        return isinstance(item, types.ListType) or isinstance(item, types.TupleType)

    def recursive_find(seq, current_path):
        """Runs through possibly nested `seq` saving the path until it finds target"""

        for index, item in enumerate(seq):
            if item == target:
                current_path.append(index)
                raise ItemFound(current_path)
            elif is_sequence(item):
                new_path = current_path + [index]
                recursive_find(item, new_path)

    try:
        recursive_find(sequence, [])
    except ItemFound as e:
        return e.path
    else:
        return None
    



