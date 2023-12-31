# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
file_in  = argv[1]
file_out = argv[2]
#file = "config_sw1.txt"
with open(file_in) as f_in, open(file_out, "w") as f_out:
    for line in f_in:
        if not line.startswith("!"):
            if (ignore[0] in line) or (ignore[1] in line) or (ignore[2] in line):
                pass
            else:
                f_out.write(line)
