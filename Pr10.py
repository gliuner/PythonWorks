class MealyError(Exception):
    pass


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


class Meely:
    def __init__(self):
        self.status = 'A'
        self.root = {'A': {'apply': ['B', 0]},
                     'B': {'apply': ['C', 1]}, 'C': {'apply': ['D', 2], 'pluck': ['G', 3]},
                     'D': {'apply': ['E', 4]},
                     'E': {'pluck': ['F', 5]},
                     'F': {'pluck': ['F', 7], 'apply': ['G', 6]},
                     'G': {'pluck': ['G', 8], 'apply': ['D', 9]}}

    def apply(self):
        if 'apply' in self.root[self.status].keys():
            a = self.root[self.status]['apply'][1]
            self.status = self.root[self.status]['apply'][0]
            return a
        else:
            raise MealyError("apply")

    def pluck(self):
        if 'pluck' in self.root[self.status].keys():
            a = self.root[self.status]['pluck'][1]
            self.status = self.root[self.status]['pluck'][0]
            return a
        else:
            raise MealyError("pluck")


def main():
    o = Meely()
    return o

#Прописывается то, как дойти до этой точки, а не то откуда из нее можно выйти
#Как я поняла, если из нее можно выйти через оба метода, проверка не нужна, иначе делать проверку на другой метод
#Прописываем как мы пришли в эту точку, и смотрим как мы можем из нее выйти, если только одним из методов, то делаем проверку на второй
def test():
    o = main()  # A
    raises(lambda: o.pluck(), MealyError)
    o.apply()  # B
    raises(lambda: o.pluck(), MealyError)
    o.apply()  # C
    o.pluck()  # G
    o.pluck()  # G
    o.apply()  # D
    raises(lambda: o.pluck(), MealyError)
    o.apply()  # E
    raises(lambda: o.apply(), MealyError)
    o.pluck()  # F
    o.pluck()  # F
    o.apply()  # G
    o = main()  # A
    o.apply()  # B
    o.apply()  # C
    o.apply()  # D
#----------------------------------------------------------------------------



'''class MealyError(Exception):
    pass


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


class Meely:
    def __init__(self):
        self.status = 'A'
        self.root = {'A': {'widen': ['B', 0]}, 'B': {'mix': ['C', 1]},
                     'C': {'mix': ['D', 2]}, 'D': {'widen': ['E', 3]},
                     'E': {'mix': ['F', 4], 'widen': ['B', 5]},
                     'F': {'mix': ['G', 6], 'widen': ['B', 7]},
                     'G': {'mix': ['C', 8], 'widen': ['D', 9]}}

    def widen(self):
        if 'widen' in self.root[self.status].keys():
            a = self.root[self.status]['widen'][1]
            self.status = self.root[self.status]['widen'][0]
            return a
        else:
            raise MealyError("widen")

    def mix(self):
        if 'mix' in self.root[self.status].keys():
            a = self.root[self.status]['mix'][1]
            self.status = self.root[self.status]['mix'][0]
            return a
        else:
            raise MealyError("mix")


def main():
    o = Meely()
    return o


def test():
    o = main()
    raises(lambda: o.mix(), MealyError)
    o.widen()
    raises(lambda: o.widen(), MealyError)
    o.mix()
    raises(lambda: o.widen(), MealyError)
    o.mix()
    raises(lambda: o.mix(), MealyError)
    o.widen()
    o.widen()
    o.mix()
    o.mix()
    o.widen()
    o.mix()
    o.widen()
    o.mix()
    o.mix()
    o.widen()
    o.mix()
    o.mix()
    o.widen()
    o.widen()
    o.mix()
    o.mix()
    o.mix()
'''


class MealyError(Exception):
    pass


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


class Meely:
    def __init__(self):
        self.status = 'A'
        self.root = {'A': {'mask': ['B', 0], 'snap': ['D', 1]},
                     'B': {'snap': ['C', 2]}, 'C': {'turn': ['D', 3]},
                     'D': {'snap': ['E', 4], 'mask': ['F', 5]},
                     'E': {'mask': ['F', 6]},
                     'F': {'mask': ['C', 8], 'snap': ['A', 7]}}

    def mask(self):
        if 'mask' in self.root[self.status].keys():
            a = self.root[self.status]['mask'][1]
            self.status = self.root[self.status]['mask'][0]
            return a
        else:
            raise MealyError("mask")

    def snap(self):
        if 'snap' in self.root[self.status].keys():
            a = self.root[self.status]['snap'][1]
            self.status = self.root[self.status]['snap'][0]
            return a
        else:
            raise MealyError("snap")

    def turn(self):
        if 'turn' in self.root[self.status].keys():
            a = self.root[self.status]['turn'][1]
            self.status = self.root[self.status]['turn'][0]
            return a
        else:
            raise MealyError("turn")


def main():
    o = Meely()
    return o


def test():
    o = main()  # A
    # raises(lambda: o.mix(), MealyError)
    raises(lambda: o.turn(), MealyError)
    o.mask()  # B
    raises(lambda: o.turn(), MealyError)
    raises(lambda: o.mask(), MealyError)
    o.snap()  # C
    raises(lambda: o.snap(), MealyError)
    raises(lambda: o.mask(), MealyError)
    o.turn()  # D
    raises(lambda: o.turn(), MealyError)
    o.snap()  # E
    raises(lambda: o.turn(), MealyError)
    raises(lambda: o.snap(), MealyError)
    o.mask()  # F
    raises(lambda: o.turn(), MealyError)
    o.mask()  # C
    o.turn()  # D
    o.mask()  # F
    o.snap()  # A
    o.snap()  # D
    o.mask()  # F
    o.snap()  # A
