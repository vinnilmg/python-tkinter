import psycopg2 as ps


class Postgre():

	def __init__(self):
		self.conn = ps.connect(host='localhost',
				user='postgres',
				password = 'buibui10',
				database='erp')
				#charset='utf8mb4')
				#cursorclass= ps.cursors.DictCursor)

