#-*-coding: utf-8 -*-
"""
the url structure of website_delete
"""

from handlers.index import IndexHandler,CicsHandler

url = [
       (r'/', IndexHandler),
       (r'/cics', CicsHandler),
]