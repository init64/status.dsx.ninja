import subprocess
from multiprocessing import Process

from servers import Servers

class Status:
    def __init__(self, ip :str, interval :int) -> None:
        self.ip = ip
        self.interval = interval

    def start(self):
        self.process = Process(target=self.__startping)
        self.process.start()

    def stop(self):
        self.process.terminate()

    def restart(self):
        self.process.terminate()
        self.process.start()

    def __startping(self):
        print(f'[ THREAD] [IP] {self.ip}')
        subprocess.run(f'ping {self.ip} -i 5 | python3 parser.py {self.ip}',shell=True)


class Statuses:
    def __init__(self) -> None:
        self.processes = []

    def start(self,servers :Servers):
        print('[THREADS] starting threads')
        for n, i in enumerate(servers.listget()):
            self.processes.append(Status(i, 5))
            self.processes[n].start()
            print(f'[ THREAD] start thread {n}')
        print(f'[THREADS] treads counts: {self.processes.__len__()}')

    def stop(self):
        for i in self.processes:
            i.stop()
        self.processes = []

    def get_status(self, ip :str):
        with open(f'logs/{ip}.log','r') as log:
            return log.readlines()[-1].split()[1]
    
    def get_statuses(self):
        statuses_servers_list = {}
        for i in self.processes:
            with open(f'logs/{i.ip}.log','r') as log:
                statuses_servers_list[i.ip] = log.readlines()[-1].split()[1]
        return statuses_servers_list
