#-*-coding: utf-8 -*-

from MySQLdb import connect

conn = connect(host='localhost', user='root', passwd = '123456', db = 'entegor', charset = 'utf8')
cur = conn.cursor()
