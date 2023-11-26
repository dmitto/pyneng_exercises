# -*- coding: utf-8 -*-
"""
Задание 11.2a

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

С помощью функции create_network_map из задания 11.2 создать словарь topology
с описанием топологии для файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

С помощью функции draw_topology из файла draw_network_graph.py нарисовать
схему для словаря topology, полученного с помощью create_network_map.
Как работать с функцией draw_topology надо разобраться самостоятельно,
почитав описание функции в файле draw_network_graph.py.
Полученная схема будет записана в файл svg - его можно открыть браузером.

С текущим словарем topology на схеме нарисованы лишние соединения. Они
возникают потому что в одном файле CDP (sh_cdp_n_r1.txt) описывается соединение
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
а в другом (sh_cdp_n_sw1.txt)
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

В этом задании надо создать новую функцию unique_network_map, которая из этих
двух соединений будет оставлять только одно, для корректного рисования схемы.
При этом все равно какое из соединений оставить.

У функции unique_network_map должен быть один параметр topology_dict,
который ожидает как аргумент словарь.
Это должен быть словарь полученный в результате выполнения
функции create_network_map из задания 11.2.

Пример словаря:
{
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
}


Функция должна возвращать словарь, который описывает соединения между
устройствами. В словаре надо избавиться от "дублирующих" соединений
и оставлять только одно из них.

Структура итогового словаря такая же, как в задании 11.2:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

После создания функции, попробовать еще раз нарисовать топологию,
теперь уже для словаря, который возвращает функция unique_network_map.

Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg

При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций create_network_map и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from pprint import pprint
from task_11_2 import create_network_map
from draw_network_graph import draw_topology

def unique_network_map(topology_dict):
    #print("dict keys =", list(topology_dict.keys()))
    #print("="*50)
    #print("dict values =", list(topology_dict.values()))
    #print("="*50)
    #print("dict items =", list(topology_dict.items()))
    #print("="*50)
    #pprint(topology_dict)
    #print("="*50)
    new_dict = {}
    key_list = []
    for key, value in list(topology_dict.items()):
        for key_2, value_2 in list(topology_dict.items()):
            if (key_2 == value) and (key != key_2) and (not value_2 in key_list):
                #print("key =",key,"value =",value)
                #print("key_2 =",key_2,"value_2 =",value_2)
                key_list.append(key_2)
                del topology_dict[key_2]
    return topology_dict

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

neighbors_dict = (create_network_map(infiles))
draw_topology(unique_network_map(neighbors_dict))