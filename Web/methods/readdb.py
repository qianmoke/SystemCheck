#-*-coding: utf-8 -*-

from db import *

def select(table, column, condition, vaule):
    sql = 'select {} from {} where date_format({},"%Y-%m-%d")="{}"'.format(column, table, condition, vaule)
    cur.execute(sql)
    lines = cur.fetchall()
    return lines
