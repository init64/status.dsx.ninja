#! /bin/python3
import sys

def parser(str_ :str) -> dict:
    data = str_.split()
    data_dict = dict([[i.split('=')[0], float(i.split('=')[1]) if n == 2 else int(i.split('=')[1])] for n, i in enumerate(data[-4:-1])])
    return data_dict

ip = sys.stdin.readline().split()[2][1:-1]
t10 = []
t1 = []
adress = sys.argv[1]
# print(ip)
for i in sys.stdin:
    data = parser(i)
    # print(data)
    with open(f'logs/{adress}.log','a') as log:
        log.write(f'{data["icmp_seq"]} {data["time"]}\n')
    # print('time', data['time'],sep='=')
