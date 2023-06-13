import math


def main(x, z, y):
    answer = 0
    for i in range(1, len(x) + 1):
        answer += (math.ceil(85 * (x[len(x) - math.ceil(i / 2)]) ** 2 +
                             50 * (y[len(x) - i]) ** 3 +
                             81 * z[len(x) - math.ceil(i / 4)])) ** 4
    return answer


print(main([-0.63, -0.88], [0.2, 0.97], [0.77, 0.38]))
