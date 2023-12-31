# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate
#from task_12_1 import ping_ip_addresses


def print_ip_table(ip_reach,ip_unreach):
    result = {"Reachable": ip_reach, "Unreachable": ip_unreach}
    print(tabulate(result, headers='keys'))

#ip_l = ['1.1.1.1', '10.4.3.2', '100.100.100.36', '192.168.1.1']
#ip_l_tested = ping_ip_addresses(ip_l)
#print(ip_l_tested)

#print_ip_table(*ip_l_tested)
