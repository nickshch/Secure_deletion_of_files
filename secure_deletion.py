import sys
import os
import random
import struct


def nop_file_bytes(path, rounds):
    file_size = os.stat(path).st_size
    for x in range(rounds):
        f = open(path, 'rb+')
        for pos in range(file_size):
            f.write(b'\x00\x00\x00\x00')  # TODO check null bytes
        f.close()


def randomize_file_bytes(path, rounds):
    random.seed()
    file_size = os.stat(path).st_size

    for x in range(rounds):
        f = open(path, 'rb+')
        for pos in range(file_size):
            random_int = random.randint(0, 255)
            random_byte = struct.pack('>B', random_int)
            print(random_byte)
            f.write(random_byte)
        f.close()


def wipe_file(path, erase_count, is_rand):
    if is_rand:
        randomize_file_bytes(path, erase_count)
    else:
        nop_file_bytes(path, erase_count)


def check_args():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        sys.exit('You need to specify the path to file as first argument')

    if len(sys.argv) > 2:
        erase_count = int(sys.argv[2])
    else:
        erase_count = 1

    if len(sys.argv) > 3:
        is_rand = bool(int(sys.argv[3]))
    else:
        is_rand = False

    return path, erase_count, is_rand


def main():
    path, erase_count, is_rand = check_args()
    wipe_file(path, erase_count, is_rand)
    # os.remove(path)
    # print('Deleted successfully')


if __name__ == "__main__":
    main()
