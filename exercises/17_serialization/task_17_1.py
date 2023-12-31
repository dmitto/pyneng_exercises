# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import csv
import re
from pprint import pprint

regexp = r"^(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<interface>\S+)"
regexp_ip = r"(?:\d+\.){3}\d+"

def write_dhcp_snooping_to_csv(filenames, output):
    headers = ['switch', 'mac', 'ip', 'vlan', 'interface']
    data = []
    print(filenames)
    for name in filenames:
        sw_name = name.split('_')[0]
        with open(name) as f_in:
            table = f_in.read()
            match = re.finditer(regexp, table, re.M)
            for line in match:
                result_dict = {}
                result_dict['switch'] = sw_name
                result_dict.update(line.groupdict())
                data.append(result_dict)
    with open(output, 'w') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


file_list = [
    'sw1_dhcp_snooping.txt',
    'sw2_dhcp_snooping.txt',
    'sw3_dhcp_snooping.txt'
    ]

if __name__ == '__main__':
    write_dhcp_snooping_to_csv(file_list, 'out_17_1.csv')