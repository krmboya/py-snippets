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

# see related solutions: http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python


