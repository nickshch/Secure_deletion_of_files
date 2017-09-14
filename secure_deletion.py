import sys
import os
import random
import struct

#обнуляем все биты файла заданное кол-во раз (так называемые круги обхода файла)
def nop_file_bytes(path, rounds):
    file_size = os.stat(path).st_size #вычисляем размер файла
    for x in range(rounds): #цикл на заданное кол-во затираний
        f = open(path, 'rb+') #открываем файл для чтения и записи в битовом режиме
        for pos in range(file_size): #проходим по всем байтам
            f.write(b'\x00') #заполняем нулями
        f.close() #закрываем файловый поток

#присваиваем каждому байту случайное значение заданное кол-во раз
def randomize_file_bytes(path, rounds):
    random.seed() # инициируем рандомизацию
    file_size = os.stat(path).st_size #вычисляем размер файла

    for x in range(rounds): #цикл на заданное кол-во затираний
        f = open(path, 'rb+') #открываем файл для чтения и записи в битовом режиме
        for pos in range(file_size): #проходим по всем байтам
            random_int = random.randint(0, 255) #выбираем случайное десятичное значение для байта
            random_byte = struct.pack('>B', random_int) #переводим значение в двоичный вид
            f.write(random_byte) #записываем байт
        f.close() #закрываем файловый поток 

#затираем файл одним из способов
def wipe_file(path, erase_count, is_rand):
    if is_rand:
        randomize_file_bytes(path, erase_count)
    else:
        nop_file_bytes(path, erase_count)

#проверяем кол-во аргументов из консоли
def check_args():
    if len(sys.argv) > 1: #минимум один аргумент надо указать - путь к файлу. проверяем аргумент
        path = sys.argv[1]
    else:
        sys.exit('You need to specify the path to file as first argument')

    if len(sys.argv) > 2: #второй аргумент, кол-во затираний
        erase_count = int(sys.argv[2])
    else:
        erase_count = 1

    if len(sys.argv) > 3: #третий аргумент, случайные числа или нули
        is_rand = bool(int(sys.argv[3]))
    else:
        is_rand = False

    return path, erase_count, is_rand


def main(): #главная функция программы
    path, erase_count, is_rand = check_args()
    wipe_file(path, erase_count, is_rand)
    os.remove(path)
    print('Deleted successfully')


if __name__ == "__main__":
    main()
