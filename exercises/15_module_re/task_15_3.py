# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re
from pprint import pprint

def convert_ios_nat_to_asa(file_in, file_out):
    regex = re.compile(r"(?P<local_ip>[\d\.]+) (?P<local_port>\d+) interface (?P<global_intf>\S+) (?P<global_port>\d+)")
    with open(file_in) as f:
        match = regex.finditer(f.read())
    template = "object network LOCAL_{}\n host {}\n nat (inside,outside) static interface service tcp {} {}\n"
    result_list = []
    for m in match:
        #print(m.groupdict())
        result_list.append(template.format(m.group("local_ip"), m.group("local_ip"), m.group("local_port"), m.group("global_port")))
    #print("="*50)
    #for command in result_list:
    #    print(command)
    with open(file_out,"w") as out:
        out.writelines(result_list)

if __name__ == "__main__":
    convert_ios_nat_to_asa("cisco_nat_config.txt", "out.txt")
