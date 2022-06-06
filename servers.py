class Servers:
    def __init__(self) -> None:
        self.__servers_list = readservers()

    def add(self, ip :str):
        if not ip in self.__servers_list:
            self.__servers_list.append(ip)
            writeservers(self.__servers_list)
            return 0
        return 1

    def remove(self, ip :str):
        if ip in self.__servers_list:
            self.__servers_list.remove(ip)
            writeservers(self.__servers_list)
            return 0
        return 1

    def removeall(self):
        self.__servers_list = []
        writeservers(self.__servers_list)
        return 0
    
    def listget(self):
        return self.__servers_list
    
    def listset(self, list :str):
        self.__servers_list = list.lstrip('[').rstrip(']').split(',')
        writeservers(self.__servers_list)
        return 0


def writeservers(list_ :list[str]):
    with open('servers', 'w') as cfg:
        cfg.write('\n'.join(list_))

def readservers():
    with open('servers', 'r') as cfg:
        return cfg.read().split('\n')