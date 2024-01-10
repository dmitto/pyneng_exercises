# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
from pprint import pprint

def parse_sh_cdp_neighbors(content):
    result = {}
    regexp = r"(?P<neighbor_name>\w+) +(?P<intf_local>\S+ \S+) +\d+.*?\d+ +(?P<intf_neighbor>\S+ \S+)"
    device_name = re.search("(\w+)\>", content).group(1)
    result[device_name] = {}
    match_iter = re.finditer(regexp, content)
    for line in match_iter:
        neigh, intf_l, intf_neigh = line.groups()
        result[device_name][intf_l] = {neigh: intf_neigh}
    return result
   

if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as f:
        pprint(parse_sh_cdp_neighbors(f.read()))
