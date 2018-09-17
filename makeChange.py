import functools


def make_change(amount, denominations):
    c = sorted(denominations)
    # print(c)
    count = 0
    result = []
    count = 0

    def total(x, y):
        return x+y

    def make(count, total, c, z):
        while(z < amount):
            for i in c:
                result.append(c[i])
                z = functools.reduce(total, result)
                if z == amount:
                    count += 1

                    make(count, total, c, z)
                else:
                    make(count, total, c, z)

    return count


make_change(4, [1, 3, 2])
