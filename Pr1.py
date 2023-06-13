import math


def main(n, b, m, x):
    ans1 = 1
    for c in range(1, m+1):
        ans2 = 0
        for i in range(1, b+1):
            ans3 = 0
            for j in range(1, n+1):
                ans3 += (math.floor(97 * j - 38 * i ** 3)) ** 5 \
                        / 26 + 65 * x ** 3 + (33 * c ** 2) ** 2
            ans2 += ans3
        ans1 *= ans2
    return float("{:.2e}".format(ans1))


print(main(7, 5, 5, -0.0))
