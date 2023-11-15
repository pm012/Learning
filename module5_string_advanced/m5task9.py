"""
create function formatted_numbers that returns list of formatted 
rows. After following call:
for el in formatted_numbers():
    print(el)

It should be result:
| decimal  |   hex    |  binary  |
|0         |    0     |         0|
|1         |    1     |         1|
|2         |    2     |        10|
|3         |    3     |        11|
|4         |    4     |       100|
|5         |    5     |       101|
|6         |    6     |       110|
|7         |    7     |       111|
|8         |    8     |      1000|
|9         |    9     |      1001|
|10        |    a     |      1010|
|11        |    b     |      1011|
|12        |    c     |      1100|
|13        |    d     |      1101|
|14        |    e     |      1110|
|15        |    f     |      1111|

- all columns have the same width 10
- header alined center
- the first column (decimals) aligned left
- the second column (hex) is aligned center
- the third column (binary) is aligned right
- vertical line symbol | is not considered as a column width

"""
def formatted_numbers():
    res = []
    txt = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex","binary")
    res.append(txt)
    for i in range(0, 16):
        txt = txt = "|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i)
        res.append(txt)

    return res


for el in formatted_numbers():
    print(el)
