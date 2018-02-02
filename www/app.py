#!/usr/bin/python
#-*-coding:utf-8-*-

__author__ = 'jasonliuu'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '172.16.111.118', 9000)
    logging.info('server started at http://172.16.111.118:9000...')
    return srv
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
except KeyboardInterrupt:
    print()
    exit()
