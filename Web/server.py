#-*-coding: utf-8 -*-

from tornado import ioloop
from tornado.options import define, options, parse_command_line
from tornado import httpserver
from application import application

define('port', default=8081, type=int, help="run on the given port")

def main():
    parse_command_line()
    httpServer = httpserver.HTTPServer(application)
    httpServer.listen(options.port)
    print "Development server is running at http://127.0.0.1:%s" % options.port
    print "Quit the server with Control-C"
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
