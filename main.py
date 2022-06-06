#! /bin/python3
from hendler import Hendler
from statuses import Statuses
from servers import Servers
from flask import Flask

IP = '10.10.10.5'
PORT = 80

def main():
    # subprocess.run('ping yaya.ru -i 10 | python3 test2.py',
    #                     shell=True, capture_output=True, text=True)
    # global statuses_servers_list
    # statuses_servers_list = {}
    # global servers_list
    # servers_list = []

    app = Flask(__name__)
    hendler = Hendler(app)
    servers = Servers()
    statuses = Statuses()
    statuses.start(servers)
    hendler.create_routs(servers, statuses)
    app.run(host=IP, port=PORT)


if __name__ == '__main__':
    main()
