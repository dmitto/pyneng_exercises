# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open("ospf.txt") as f:
    for line in f:
        line_list = line.rstrip().split()
        #print(line_list)
        print("{:<22}{:<22}".format("Prefix",line_list[1]))
        print("{:<22}{:<22}".format("AD/Metric",line_list[2].strip("[]")))
        print("{:<22}{:<22}".format("Next-Hop",line_list[4][:-1]))
        print("{:<22}{:<22}".format("Last update",line_list[5][:-1]))
        print("{:<22}{:<22}".format("Outbound Interface",line_list[6]))
        #print("="*50)