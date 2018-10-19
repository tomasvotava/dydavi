#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__=='__main__':
	print("This is not intended to be run standalone")


MAX_ROWS	= 10000 #Not working yet

import mysql.connector as msc
	
class Connection:
	"""
	Interface for maintaining connection to MySQL server
	"""
	def __init__(self,host="127.0.0.1",user="root",password=None,database=None):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		self.cursor = None
		self.connector = None
		
	def connect(self):
		"""
		Create mysql.connector instance and connect to the server.
		"""
		self.connector = msc.connect(host=self.host,user=self.user,password=self.password,database=self.database)
		
	def query(self,query,*args):
		"""
		Execute single query and return output (if any)
		Returns:
			Null on no output (e.g. CREATE, INSERT, UPDATE statements)
			Result object on result
		"""
		if self.cursor==None:
			self.cursor = self.connector.cursor(buffered=True)

		self.cursor.execute(query,tuple(args))
		
		if (self.cursor.rowcount==0):
			return None
		else:
			return Result(query%args,self.cursor.column_names,self.cursor.fetchall())


class Result:
	"""
	Object for storing query results
	"""
	def __init__(self,query,columns,data):
		self.query = query
		self.columns = columns
		self.data = data
	def __str__(self):
		return "<Result: %d rows, original query \'%s\'>"%(len(self.data),(self.query[:80]+"..." if len(self.query)>80 else self.query))