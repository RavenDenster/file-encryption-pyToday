import pyAesCrypt
import os

def encryption(file, password):
    buffer_size = 512 * 1024
    
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )
    print("[Файл '"+ str(os.path.splitext(file)[0]) + "' зашифрован]") # делает кортеж root + ext

    os.remove(file) # удаляем файл по ранее склеяному пути


def walking_by_dirs(dir, password):
    for name in os.listdir(dir): # os.listdir(dir) - название всех файлов в дириктории
        path = os.path.join(dir, name) # слепляет путь и название файла в одно
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password) # если есть другие вложености, то они тоже будут шифроваться

password = input('Введите пароль для шифрования: ')
walking_by_dirs("d:/code/python/mini-project/encryption-file/file", password)