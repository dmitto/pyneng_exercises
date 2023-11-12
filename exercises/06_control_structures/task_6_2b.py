# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_int = []
ip_lst = []
key = False
while not key:
    mk = 0
    ip = input("Введите ip-адрес: ")
    ip_list = ip.split(".")
    if ip.count(".") == 3 and len(ip_list) == 4:
        for ip_l in ip_list:
            if ip_l.isdigit() and 0 <= int(ip_l) <= 255:
                #ip_int.append(int(ip_l))
                mk += 1
    if mk != 4:
        print("Неправильный IP-адрес")
    else:
        key = True

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
