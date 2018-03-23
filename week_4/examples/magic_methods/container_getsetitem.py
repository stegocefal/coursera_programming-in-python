class CustomContainer(object):
    def __init__(self, *args):
        self.items = list(args)

    def __getitem__(self, item):
        print('I\'m getting item for you...')
        return self.items[item]

    def __setitem__(self, key, value):
        print("I'm setting item for you...")
        self.items[key] = value

    def __str__(self):
        return self.items.__str__()


a = CustomContainer(1, 2, 3, 4)
print(a.items)
