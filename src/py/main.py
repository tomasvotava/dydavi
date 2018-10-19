#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql.model as m
import pymysql.connection as c

con = c.Connection(host="zumpa-vps.tk",user="dydavi",password="12345",database="dydavi")
con.connect()

r = con.query("SELECT * FROM crime WHERE victim_age>15 AND date_occurred != %s AND victim_sex!=%s LIMIT %s","2013-01-01","K",150)

print(r)