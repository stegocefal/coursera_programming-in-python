class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            print(super())
            cls.instance = super().__new__(cls)

        return cls.instance


a = Singleton()
b = Singleton()
print(a is b)
