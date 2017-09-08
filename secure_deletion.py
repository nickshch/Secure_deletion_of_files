import sys
import os
import random
import struct


def nop_file(path='examplefile.txt', rounds=1):
    file_size = os.stat(path).st_size
    for x in range(rounds):
        f = open(path, 'rb+')
        for pos in range(file_size):
            f.write(b'\x00\x00\x00\x00')
        f.close()


def rand_file(path='examplefile.txt', rounds=1):
    file_size = os.stat(path).st_size
    for x in range(rounds):
        f = open(path, 'rb+')
        for pos in range(file_size):
            random_int = random.randint(0, 255)
            random_byte = struct.pack('>B', random_int)
            print(random_byte)
            f.write(random_byte)
        f.close()


def main():
    path = 'examplefile.txt'
    erase_count = 1
    is_rand = True

    random.seed()

    print(sys.argv)
    if sys.argv.count(int) > 0:
        path = sys.argv[1]
    if sys.argv.count(int) > 1:
        erase_count = int(sys.argv[2])
    if sys.argv.count(int) > 2:
        is_rand = int(sys.argv[3])

    file_size = os.stat(path).st_size

    print(file_size)
    print(is_rand)
    if is_rand:
        rand_file(path, erase_count)
    else:
        nop_file(path, erase_count)


if __name__ == "__main__":
    main()
