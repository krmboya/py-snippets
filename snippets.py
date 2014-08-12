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
print [k for k in some_dict if k in another_dict]
# or
print filter(some_dict.has_key, another_dict.keys())

