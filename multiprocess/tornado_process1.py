#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
@description : 描述
@Time : 2020/7/25 5:38 PM
@Auth : Minhang
@File : flask_process1.py
@IDE  : PyCharm
"""
from multiprocessing import Process
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import psutil


class IndexHandler(tornado.web.RequestHandler):

    def get(self):

        self.write("TornadoProcess1")

class StopTornadoProcess3(tornado.web.RequestHandler):

    def post(self,*args, **kwargs):
        # pid = self.get_body_argument('pid')
        # print("pid:",pid)
        data = json.loads(self.request.body)
        pid = data.get("pid")
        print(pid,type(pid))
        pause = psutil.Process(pid)  # 传入子进程的pid
        pause.suspend()  # 暂停子进程
        self.write("Tornado进程3被挂起")

class TornadoProcess1(Process):

    def run(self):

        print("1")
        tornado.options.parse_command_line()
        app = tornado.web.Application(handlers=[
            (r"/", IndexHandler),
            (r"/stop-3/", StopTornadoProcess3), # 挂起 tornado 3
        ])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(10001)
        tornado.ioloop.IOLoop.instance().start()
