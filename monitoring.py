import os
import hashlib
import time
import plyer
from telegram_bot import send_notification

# Глобальные переменные
monitored_files = []

# Словарь для хранения хешей файлов
file_hashes = {}

# Функция для вычисления хеша файла
def calculate_hash(file_path, hash_method):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            file_hash = hashlib.new(hash_method)
            file_hash.update(content)
            return file_hash.hexdigest()
    except Exception as e:
        print(f"Error when calculating the hash of a file {file_path}: {str(e)}")
        return None

# Функция для мониторинга файлов
def start_monitoring():
    try:
        while True:
            for monitored_file in monitored_files:
                if os.path.isfile(monitored_file):  # Проверяем, существует ли файл
                    current_hash = calculate_hash(monitored_file, hash_method) # Вычисляется хеш текущего файла с использованием заданного метода хеширования (hash_method), и результат сохраняется в current_hash.
                    if monitored_file in file_hashes and file_hashes[monitored_file] != current_hash:
                        send_notification('file hash has been changed')
                        print('file hash has been changed')
                        plyer.notification.notify(
                            message='file hash has been changed',
                            app_name='monitoring',
                            title='HASH',
                        )
                    file_hashes[monitored_file] = current_hash # Обновляется значение хеша в словаре file_hashes для данного файла.
                time.sleep(10)
    except KeyboardInterrupt:
        print("Program Completed.")
