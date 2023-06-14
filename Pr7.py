#Одно значени на входе, выход ключ-значение, умножается на 2 в степени кол-во ячеек, сдвигается на первое значение в партии ячеек
def main(y):
    res = {'Y1': str(y & 3),
           'Y2': str((y & 15 << 2) >> 2),
           'Y3': str((y & 511 << 6) >> 6),
           'Y4': str((y & 1 << 15) >> 15)}
    return res


print(main(50404))

#Несколько значений на входе, одно на выходе, индекс = номеру числа, подаваемого на вход, сдвиг на сдвигается на первое значение в партии ячее
def main(bit_fields):
    result = 0
    result = result | int(bit_fields[0]) << 0
    result = result | int(bit_fields[1]) << 1
    result = result | int(bit_fields[2]) << 9
    result = result | int(bit_fields[3]) << 12
    return result


print(main(('0', '222', '0', '2')))
