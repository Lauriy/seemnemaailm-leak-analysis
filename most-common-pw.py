# -*- coding: utf-8 -*-

import operator

with open('seemnemaailm-leak.txt', encoding='utf8') as f:
    with open('most-common-pw.txt', 'w', encoding='utf-8') as out:
        dict = {}
        for line in f.readlines():
            pw = line.split(',')[3].strip()
            if pw not in dict:
                dict[pw] = 1
            else:
                dict[pw] += 1
        for each in sorted(dict.items(), key=operator.itemgetter(1), reverse=True):
            out.write(each[0] + '\n')
