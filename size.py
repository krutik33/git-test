#Импортируем библиотеку для работы с операционной системой
import os
#Создаем функцию которая обходит каталог и суммирует размер файлов в нем.
def get_size(path):
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                if os.path.isfile(fp):
                    size += os.path.getsize(fp)

    return size
#Создаем функцию для приведения размеров
def human_readable_size(size):
    for unit in [ 'B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            break
        size /= 1024
    return "{:.1f}{}".format(size, unit)
#описываем основную функцию
def main():
#получаем текущий путь в переменную
    pwd = os.getcwd()
#получаем список файлов и каталогов
    items = os.listdir(pwd)
#пустой список под заполнение 
    size_list = []
#заполнение списка размерами и названиями
    for item in items:
        full_path = os.path.join(pwd, item)
        size = get_size(full_path)
        size_list.append((size, item))
#сортрировка списка
    size_list.sort(key=lambda x: x[0], reverse=True)
#Вывод списка не экран
    for size, item in size_list:
        print("{} {}".format(human_readable_size(size), item))

if __name__ == "__main__":
    main()