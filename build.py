import subprocess
import os

# Команда для создания EXE
command = [
    'pyinstaller',
    '--onefile',
    '--windowed',
    '--name=УмныеУстройства',
    '--clean',
    '--noconfirm'
]

# Добавляем файлы изображений
image_files = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']
for img in image_files:
    if os.path.exists(img):
        command.append(f'--add-data={img};.')

# Добавляем основной файл
command.append('smart_devices.py')

# Запускаем сборку
print("Начинаю сборку EXE...")
subprocess.run(command)
print("Готово! EXE файл: dist/УмныеУстройства.exe")