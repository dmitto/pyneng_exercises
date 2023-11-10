# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_int =[]
key = True
ip = input("Введите ip-адрес: ")
ip_list = ip.split(".")
mk = 0
if ip.count(".") == 3 and len(ip_list) == 4:
    for ip_l in ip_list:
        if ip_l.isdigit() and 0 <= int(ip_l) <= 255:
            #ip_int.append(int(ip_l))
            mk += 1
if mk == 4:
    #oct1 = ip_int[0]
    oct1 = int(ip_list[0])
    if 1 <= oct1 <=223:
        print("unicast")
    elif 224 <= oct1 <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
else:
    print("Неправильный IP-адрес")