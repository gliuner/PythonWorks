import math


def main(n):
    if n >= 1:
        return main(n-1) ** 4 / 92 + math.tan(main(n-1)) ** 3 / 62 + 1
    elif n == 0:
        return 0.07


print(main())