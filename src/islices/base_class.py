

class IntOrNone:
    def __new__(cls, initial=None):
        if initial is None or isinstamce(initial, int):
            return initial
        raise TypeError('expected a int or None, not {!r}'.format(initial))
          

class ISlice:

    start = None
    stop = None
    step = None
    getter = None

    def __new__(cls, start=None, stop=None, stride=None):
        self = super().__new__(cls)
        self.start, self.stop, self.stride = (IntOrNone(i) for i in (start, stop, stride))
        return self

