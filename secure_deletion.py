import sys
import os
import random
import struct


def nop_file(path, rounds):
    file_size = os.stat(path).st_size
    for x in range(rounds):
        f = open(path, 'rb+')
        for pos in range(file_size):
            f.write(b'\x00\x00\x00\x00')
        f.close()


def rand_file(path, rounds):
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
    path = ''
    erase_count = 1
    is_rand = False

    random.seed()

    if len(sys.argv) > 1:
        path = sys.argv[1]
        if len(sys.argv) > 2:
            erase_count = int(sys.argv[2])
        if len(sys.argv) > 3:
            is_rand = int(sys.argv[3])
    else:
        sys.exit('You need to specify the path to the file as argument')

    if is_rand:
        rand_file(path, erase_count)
    else:
        nop_file(path, erase_count)

    os.remove(path)

    print('Deleted successfully')
if __name__ == "__main__":
    main()
