#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
@description : 描述
@Time : 2020/7/25 5:38 PM
@Auth : Minhang
@File : flask_process2.py
@IDE  : PyCharm
"""
from multiprocessing import Process
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("TornadoProcess2")

class TornadoProcess2(Process):

    def run(self):

        print("2")
        tornado.options.parse_command_line()
        app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(10002)
        tornado.ioloop.IOLoop.instance().start()
