import sys


digit_string = sys.argv[1]
assert digit_string.isdigit(), \
    'Переданный аргумент не является числовой строкой.'

sum_ = 0
for char in digit_string:
    sum_ += int(char)

print(sum_)
