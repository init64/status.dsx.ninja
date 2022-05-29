#! /bin/python3
import sys, test3

ip = sys.stdin.readline().split()[2][1:-1]
t10 = []
t1 = []
print(ip)
for i in sys.stdin:
        #print(f'> {i}')
        data = test3.parser(i)
        print('time', data['time'],sep='=')