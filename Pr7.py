def main(y):
    res = {'Y1': str(y & 3),
           'Y2': str((y & 15 << 2) >> 2),
           'Y3': str((y & 511 << 6) >> 6),
           'Y4': str((y & 1 << 15) >> 15)}
    return res


print(main(50404))
