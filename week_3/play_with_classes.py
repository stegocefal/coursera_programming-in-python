class Fake0:
    def __init__(self):
        self.inclass = 'Fake0'
        print(self.inclass)


class Fake1:
    def __init__(self):
        self.inclass = 'Fake1'
        print(self.inclass)


class Fake2(Fake1):
    def __init__(self):
        super().__init__()


class Fake3(Fake1, Fake2):
    def __init__(self):
        super().__init__()


a = Fake2()
b = Fake3()
