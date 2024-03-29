# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler
import yaml
import subprocess

def ping_ip_address(ip_addr):
    result = subprocess.run(['ping', '-c', '1', ip_addr], stdout=subprocess.DEVNULL)
    return result.returncode

def ping_ip_addresses(ip_list, limit=3):
    ip_list_avalible = []
    ip_list_not_avalible = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = map(ping_ip_address, ip_list)
        for ip, out in zip(ip_list, result):
            if out == 0:
                ip_list_avalible.append(ip)
            else:
                ip_list_not_avalible.append(ip)
    return ip_list_avalible, ip_list_not_avalible

if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    ip_ls = []
    for device in devices:
        ip_ls.append(device['host'])
        ip_ls.append(device['host']+'1')
    print(ping_ip_addresses(ip_ls))