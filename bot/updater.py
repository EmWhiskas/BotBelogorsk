import subprocess
import os
import shutil


os.remove('bot/bot.py')

# Путь к исходной папке
source_folder = 'апдейты'

# Путь к целевой папке
target_folder = 'bot'

# Имя файла для переименования и перемещения
file_name = 'file_0.py'

# Новое имя файла
new_file_name = 'bot.py'

# Полный путь к исходному файлу
source_file_path = os.path.join(source_folder, file_name)

# Полный путь к новому файлу в целевой папке
target_file_path = os.path.join(target_folder, new_file_name)

# Переименовываем и перемещаем файл
shutil.move(source_file_path, target_file_path)

# Удаляем исходный файл, если он все еще существует
if os.path.exists(source_file_path):
    os.remove(source_file_path)

filename = 'bot.py'
subprocess.run(['python', filename])

