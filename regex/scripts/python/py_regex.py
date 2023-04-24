#!/usr/bin/python

import re

# patter = re.compile(r'(^[\d]{4,4})-[\d][\d]-[\d][\d],(.*),Friendly')
patter = re.compile(r'(^[\d]{4,4})-[\d][\d]-[\d][\d],([\w]+),([\w]+),([\d]),([\d]),Friendly')

f = open("..\\..\\files\\results.csv", "r", encoding="utf-8")

for line in f:
    res = re.match(patter, line)
    if res:
        # print("%s\n" % res.group(2))
        gols = 5
        total = int(res.group(4)) + int(res.group(5))
        if total>10:
            print(f"{res.group(1):^} | {res.group(2)} ({res.group(4)}) - ({res.group(5)}) {res.group(3)} | total: {total}")
    
f.close()