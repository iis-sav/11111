from tkinter import *
import os

root = Tk()
root.title("Умные устройства")
root.geometry("800x600")
root.configure(bg='white')

# Главный контейнер
main = Frame(root, bg='white')
main.pack(fill=BOTH, expand=True)

# Левая часть
left = Frame(main, bg='white')
left.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

# Кнопки Характеристики/Функции
top_buttons = Frame(left, bg='white')
top_buttons.pack(pady=10)

# Фрейм для изображения
img_frame = Frame(left, bg='white')
img_frame.pack(pady=20)

# Правая часть - кнопки устройств
right = Frame(main, width=200, bg='white')
right.pack(side=RIGHT, fill=Y, padx=10, pady=10)

# Данные устройств
devices_data = {
    "Эл.замок": {
        "file": "1.png",
        "icon": "5.png",
        "характеристики": "• Кодовый доступ\n• Беспроводное управление\n• Журнал событий\n• Уведомления",
        "функции": "• Открытие/закрытие\n• Временный доступ\n• Интеграция с камерами\n• Автоматическая блокировка",
        "инструкция": "1. Установите на дверь\n2. Подключите к Wi-Fi\n3. Настройте код доступа"
    },
    "Умная лампочка": {
        "file": "2.png",
        "icon": "6.png",
        "характеристики": "• LED 9W\n• Цветная RGB\n• Wi-Fi управление\n• Энергосбережение",
        "функции": "• Изменение цвета\n• Регулировка яркости\n• Таймеры\n• Сценарии освещения",
        "инструкция": "1. Вкрутите в патрон\n2. Подключите к приложению\n3. Настройте расписание"
    },
    "Система отопления": {
        "file": "3.png",
        "icon": "7.png",
        "характеристики": "• Термостат\n• Wi-Fi/Bluetooth\n• Точность ±0.5°C\n• Экономичный режим",
        "функции": "• Установка температуры\n• Недельное расписание\n• Удаленный контроль\n• Геолокация",
        "инструкция": "1. Установите на стену\n2. Подключите к котлу\n3. Настройте температуру"
    },
    "Автоматический полив": {
        "file": "4.png",
        "icon": "8.png",
        "характеристики": "• Бак 10л\n• 8 каналов\n• Датчик влажности\n• Программируемый",
        "функции": "• Расписание полива\n• Ручной полив\n• Контроль влажности\n• Уведомления",
        "инструкция": "1. Установите в саду\n2. Подключите шланги\n3. Настройте график"
    }
}

current_device = None

# Загрузка иконок
device_icons = {}
for i, device in enumerate(devices_data.keys()):
    icon_file = devices_data[device]["icon"]
    if os.path.exists(icon_file):
        try:
            img = PhotoImage(file=icon_file).subsample(3, 3)
            device_icons[i] = img
        except:
            device_icons[i] = None
    else:
        device_icons[i] = None

# Функции
def show_img(device_name):
    global current_device
    current_device = device_name
    file = devices_data[device_name]["file"]

    for w in img_frame.winfo_children():
        w.destroy()

    if os.path.exists(file):
        try:
            img = PhotoImage(file=file).subsample(2, 2)
            Label(img_frame, image=img, bg='white').image = img
            Label(img_frame, image=img, bg='white').pack()
        except:
            Label(img_frame, text="Ошибка загрузки", bg='white').pack()
    else:
        Label(img_frame, text=f"Файл {file} не найден", bg='white').pack()

    # Обновляем текст под изображением
    for w in info_frame.winfo_children():
        w.destroy()
    Label(info_frame, text=device_name, font=("Arial", 12, "bold"), bg='white').pack()

def show_info(title, text):
    win = Toplevel(root, bg='white')
    win.title(title)
    Label(win, text=text, justify=LEFT, padx=20, pady=20, bg='white').pack()

def show_characteristics():
    if current_device:
        text = devices_data[current_device]["характеристики"]
        show_info(f"Характеристики: {current_device}", text)
    else:
        show_info("Характеристики", "Выберите устройство")

def show_functions():
    if current_device:
        text = devices_data[current_device]["функции"]
        show_info(f"Функции: {current_device}", text)
    else:
        show_info("Функции", "Выберите устройство")

def show_instruction():
    if current_device:
        text = devices_data[current_device]["инструкция"]
        show_info(f"Инструкция: {current_device}", text)
    else:
        show_info("Инструкция", "Выберите устройство")

# Кнопки устройств справа
Label(right, text="Устройства", font=("Arial", 12, "bold"), bg='white').pack(pady=10)

for i, device in enumerate(devices_data.keys()):
    frame = Frame(right, bg='white')
    frame.pack(pady=5)

    if device_icons.get(i):
        btn = Button(frame, image=device_icons[i],
                     command=lambda d=device: show_img(d),
                     bg='white', relief=RAISED, bd=2)
    else:
        btn = Button(frame, text=device,
                     command=lambda d=device: show_img(d),
                     bg='white', width=15, relief=RAISED, bd=2)
    btn.pack()
    Label(frame, text=device, bg='white', font=("Arial", 9)).pack()

# Кнопки Характеристики, Функции, Инструкция
Button(top_buttons, text="Характеристики", bg='#e6f2ff', width=15,
       command=show_characteristics).pack(side=LEFT, padx=5)

Button(top_buttons, text="Функции", bg='#e6ffe6', width=15,
       command=show_functions).pack(side=LEFT, padx=5)

Button(top_buttons, text="Инструкция", bg='#fff2e6', width=15,
       command=show_instruction).pack(side=LEFT, padx=5)

# Фрейм для информации об устройстве
info_frame = Frame(left, bg='white')
info_frame.pack(pady=10)

# Меню
menubar = Menu(root, bg='white')
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, bg='white')
filemenu.add_command(label="Открыть")
filemenu.add_command(label="Сохранить")
filemenu.add_command(label="Закрыть", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

devicesmenu = Menu(menubar, tearoff=0, bg='white')
for device in devices_data.keys():
    sub = Menu(devicesmenu, tearoff=0, bg='white')
    sub.add_command(label="Изображение", command=lambda d=device: show_img(d))
    sub.add_command(label="Характеристики",
                    command=lambda d=device: show_info(f"Характеристики {d}", devices_data[d]["характеристики"]))
    sub.add_command(label="Функции",
                    command=lambda d=device: show_info(f"Функции {d}", devices_data[d]["функции"]))
    devicesmenu.add_cascade(label=device, menu=sub)
menubar.add_cascade(label="Устройства", menu=devicesmenu)

instructionmenu = Menu(menubar, tearoff=0, bg='white')
for device in devices_data.keys():
    instructionmenu.add_command(label=device,
                                command=lambda d=device: show_info(f"Инструкция {d}", devices_data[d]["инструкция"]))
menubar.add_cascade(label="Инструкция", menu=instructionmenu)

helpmenu = Menu(menubar, tearoff=0, bg='white')
helpmenu.add_command(label="Помощь",
                     command=lambda: show_info("Помощь", "Для работы выберите устройство справа\nи используйте кнопки для просмотра информации"))
menubar.add_cascade(label="Помощь", menu=helpmenu)

root.mainloop()