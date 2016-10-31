#-*-coding: utf-8 -*-

from url import url
from tornado import web
import os
from handlers.index import RegionModule
from Web.handlers.index import TpsModule, PoolModule

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
    ui_modules = {'RegionModule': RegionModule,'TpsModule':TpsModule, 'PoolModule':PoolModule},
    debug = True
)

application = web.Application(
    handlers= url,
    **settings
)