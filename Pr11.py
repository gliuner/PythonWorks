'''from struct import unpack_from, calcsize


class Types:
    uint16 = 'H'
    int8 = 'b'
    int32 = 'i'
    int16 = 'h'
    int64 = 'q'
    uint8 = 'B'
    uint64 = 'Q'
    uint32 = 'I'
    uint8 = 'B'
    float = 'f'
    double = 'd'
    char = 's'


class BinaryReader:
    def __init__(self, data, offset, order='<'):
        self.data = data
        self.offset = offset
        self.order = order

    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_e(reader):
    e1 = reader.read(Types.int8)
    e2 = reader.read(Types.int16)
    return dict(E1=e1, E2=e2)


def read_d(reader):
    # d1 = [reader.read(Types.uint8) for _ in range(5)]
    d1 = reader.read(Types.int16)
    d2 = reader.read(Types.int32)
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1_size = reader.read(Types.uint32)
    c1_offset = reader.read(Types.uint16)
    c1_reader = reader.jump_to(c1_offset)
    c1 = [c1_reader.read(Types.uint16) for i in range(c1_size)]
    c2 = reader.read(Types.int16)
    c3 = reader.read(Types.double)
    c4 = reader.read(Types.int64)
    c5_size = reader.read(Types.uint32)
    c5_offset = reader.read(Types.uint16)
    c5_reader = reader.jump_to(c5_offset)
    c5 = [c5_reader.read(Types.int16) for i in range(c5_size)]
    c6 = reader.read(Types.int16)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6)


def read_b(reader):
    b1 = reader.read(Types.uint8)
    b2_offset = [reader.read(Types.uint16) for i in range(3)]
    b2 = [read_c(reader.jump_to(i)) for i in b2_offset]
    b3 = reader.read(Types.int64)
    b4 = reader.read(Types.int32)
    b5 = reader.read(Types.int32)
    b6 = reader.read(Types.int8)
    b7 = reader.read(Types.float)
    b8 = [reader.read(Types.uint8) for i in range(2)]
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8)


def read_a(reader):
    a1 = b''.join([reader.read(Types.char) for i in range(3)]).decode()
    a2_offset = reader.read(Types.uint16)
    a2_reader = reader.jump_to(a2_offset)
    a2 = read_b(a2_reader)
    a3 = reader.read(Types.uint32)
    a4 = read_d(reader)
    a5_offset = reader.read(Types.uint32)
    a5_reader = reader.jump_to(a5_offset)
    a5 = read_e(a5_reader)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5)


def main(data):
    return read_a(BinaryReader(data, 3))


print(main((b'IXCzvb\x9e\x00\xe1\x05\xa5\xde\x8f\xf5\x1b@\x9c}\xbc\x00\x00\x00Ia\xa1Z&\x93'
            b'\xeb3\xbcD\xc2Sm\x119\x9e\x04\x00\x00\x00\x16\x00\x07\xf3<\xe7!{\xefR'
            b'\xdd?\xae\xef\x07\x9e\xe0\xe9$:\x04\x00\x00\x00\x1e\x001\xe2r+\xc3\xfb*\xef'
            b'\x04SbC\xff\xcb\xa7K\x03\x00\x00\x00F\x00-\x13\xd4\x9b\xee\x8b3\xd4\xe3\xbf'
            b'o\xae\xc6\xb9Ah\x9f\xac\x04\x00\x00\x00L\x00\x0bgnE/\xe7\x1c#\x9a^'
            b'\x88\x8d\x02\x00\x00\x00t\x00\xa1\xfc\xd4_J\xbc\xd8\xc7\xeb?0\x8c\x9eH\x0b='
            b'N\x92\x03\x00\x00\x00x\x00J-\x99&\x00T\x00~\x00\x14\x17\x1dh\xd4\x91\xba'
            b'?\x1d\xcc[\xe1\x80s\x89i\x0fM\xe1\x81\xbe\x9f\xbf\xe0B\xd7')))'''

from struct import unpack_from, calcsize


class Types:
    uint16 = 'H'
    int8 = 'b'
    int32 = 'i'
    int16 = 'h'
    int64 = 'q'
    uint8 = 'B'
    uint64 = 'Q'
    uint32 = 'I'
    uint8 = 'B'
    float = 'f'
    double = 'd'
    char = 's'


class BinaryReader:
    def __init__(self, data, offset, order='>'):
        self.data = data
        self.offset = offset
        self.order = order

    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_d(reader):
    d1 = reader.read(Types.uint32)
    d2 = reader.read(Types.uint8)
    d3_size = reader.read(Types.uint16)
    d3_offset = reader.read(Types.uint16)
    d3_reader = reader.jump_to(d3_offset)
    d3 = [d3_reader.read(Types.int32) for i in range(d3_size)]
    d4 = reader.read(Types.uint32)
    d5 = reader.read(Types.int8)
    d6 = reader.read(Types.int32)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6)


def read_c(reader):
    c1 = reader.read(Types.uint8)
    c2 = reader.read(Types.uint32)
    c3 = reader.read(Types.uint64)
    c4 = reader.read(Types.uint64)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader):
    b1_size = reader.read(Types.uint32)
    b1_offset = reader.read(Types.uint32)
    b1_reader = reader.jump_to(b1_offset)
    b1 = b''.join([b1_reader.read(Types.char)
                   for i in range(b1_size)]).decode()
    b2_size = reader.read(Types.uint32)
    b2_offset = reader.read(Types.uint16)
    b2_reader = reader.jump_to(b2_offset)
    b2 = [b2_reader.read(Types.int8) for i in range(b2_size)]
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.float)
    a2 = reader.read(Types.int8)
    a3_offsets = [reader.read(Types.uint16) for i in range(6)]
    a3 = [read_b(reader.jump_to(i)) for i in a3_offsets]
    a4_offset = reader.read(Types.uint32)
    a4_reader = reader.jump_to(a4_offset)
    a4 = read_c(a4_reader)
    a5 = reader.read(Types.uint32)
    a6_offset = reader.read(Types.uint32)
    a6_reader = reader.jump_to(a6_offset)
    a6 = read_d(a6_reader)
    a7 = reader.read(Types.int16)
    a8 = [reader.read(Types.int8) for i in range(5)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(data):
    return read_a(BinaryReader(data, 4))


print(main((b'VUQL>\x84\xd6\xe2?\x00-\x00@\x00S\x00e\x00x\x00\x8a\x00\x00\x00'
            b'\x98\xcd\x86\x8a\xe8\x00\x00\x00\xbd\xe9\xf3\x1aL\x13\xf3\xeclno\xf1'
            b';\x00\x00\x00\x03\x00\x00\x00(\x00\x00\x00\x02\x00+zse\xd4W\x00\x00\x00\x03'
            b'\x00\x00\x00;\x00\x00\x00\x02\x00>vk\xd1\xaa\x9c\x00\x00\x00\x02\x00'
            b'\x00\x00N\x00\x00\x00\x03\x00Ptg9\xac\x00\x00\x00\x02\x00\x00\x00'
            b'a\x00\x00\x00\x02\x00cnef\xbc%\x00\x00\x00\x03\x00\x00\x00s\x00\x00\x00\x02'
            b'\x00vll\xe3\xff\x00\x00\x00\x02\x00\x00\x00\x86\x00\x00\x00\x02\x00\x88'
            b'\xd6\x92x\xe8\x8c\xf9\x8dj\x03\x88\xe6\xa3\x1c\x1a~tW\x93\xc8\xc0fsD\xdd'
            b'\xf5\x10\xf7>\x16q\xc0\xd4F\x15\xe9$f\r\xd9\xfc\x13\xa3\x00\x04\x00\xady\xad'
            b'\xc4\x1a/r!-I')))
