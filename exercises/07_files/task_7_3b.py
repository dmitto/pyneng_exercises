# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan_num = input("Введите номер VLAN: ")
with open("CAM_table.txt") as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0].isdigit() and line_list[0] == vlan_num:
            line_list.remove(line_list[2])
            vlan, mac, intf = line_list
            print(f"{vlan:<9}{mac:<20}{intf}")