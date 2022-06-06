#!/bin/python3
from flask import Flask, jsonify, request

from servers import Servers
from statuses import Statuses


# test = [
# 	{
# 	'test':'yes',
# 	'erorr':'no'
# 	}
# ]

class Hendler():
    def __init__(self,app :Flask):
        self.app = app

    def create_routs(self, servers :Servers, statuses :Statuses):

        #  statuses
        @self.app.route('/statuses/server', methods=['GET'])
        def status_server():
            try:
                ip = request.args.get("ip")
                status = {
                        'erorr':0,
                        'ip': ip,
                        'time': statuses.get_status(ip)
                }
            except:
                print('[ ERORR ] /statuses/server')
                status = {'erorr':1}

            return jsonify(status)


        @self.app.route('/statuses/list', methods=['GET'])
        def status_list():
            try:
                status = {
                    'erorr':0,
                    'status':statuses.get_statuses()
                    }
            except:
                print('[ ERORR ] /statuses/list')
                status = {'erorr':1}

            return jsonify(status)

        @self.app.route('/statuses/restart', methods=['GET'])
        def status_restart():
            try:
                statuses.stop()
                statuses.start(servers)
                status = {'erorr':0}
            except:
                print('[ ERORR ] /statuses/restart')
                status = {'erorr':1}

            return jsonify(status)

        @self.app.route('/statuses/stop', methods=['GET'])
        def status_stop():
            try:
                statuses.stop()
                status = {'erorr':0}
            except:
                print('[ ERORR ] /statuses/stop')
                status = {'erorr':1}

            return jsonify(status)

        @self.app.route('/statuses/start', methods=['GET'])
        def status_start():
            try:
                statuses.start(servers)
                status = {'erorr':0}
            except:
                print('[ ERORR ] /statuses/start')
                status = {'erorr':1}

            return jsonify(status)

        #  servers
        @self.app.route('/servers/add', methods=['GET'])
        def servers_add():
            try:
                ip = request.args.get("ip")
                erorr = servers.add(ip)
                status = {
                    'erorr':erorr,
                    'add':ip
                    }
            except:
                print('[ ERORR ] /servers/add')
                status = {'erorr':1}

            return jsonify(status)


        @self.app.route('/servers/remove', methods=['GET'])
        def servers_remove():
            try:
                ip = request.args.get("ip")
                erorr = servers.remove(ip)
                status = {'erorr':erorr}
            except:
                print('[ ERORR ] /servers/remove')
                status = {'erorr':1}

            return jsonify(status)


        @self.app.route('/servers/removeall', methods=['GET'])
        def servers_removeall():
            try:
                servers.removeall()
                status = {'erorr':0}
            except:
                print('[ ERORR ] /servers/removeall')
                status = {'erorr':1}

            return jsonify(status)


        @self.app.route('/servers/list/get', methods=['GET'])
        def servers_list_get():
            try:
                status = {
                    'erorr':0,
                    'servers':servers.listget()
                    }
            except:
                print('[ ERORR ] /servers/list/get')
                status = {'erorr':1}

            return jsonify(status)


        @self.app.route('/servers/list/set', methods=['GET'])
        def servers_list_set():
            try:
                list = request.args.get("list")
                servers.listset(list)
                status = {'erorr':0}
            except:
                print('[ ERORR ] /servers/list/set')
                status = {'erorr':1}

            return jsonify(status)
