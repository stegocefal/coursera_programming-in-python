def MyRangeGenerator(top):
    current = 0
    while current < top:
        yield current
        current += 1


if __name__ == '__main__':
    counter = MyRangeGenerator(3)
    print(counter)

    for it in counter:
        print(it)
