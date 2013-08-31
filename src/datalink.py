import MySQLdb, random

class DatabaseConnectionDown:
	def __init__(self,adb):
		'''
			This initializes the Database Connection for downlink
			@param DatabeseName
		'''
		self.adb = adb
		try:
			self.db = MySQLdb.connect(user='root', db=adb, passwd='adminpass', host='localhost')
		except MySQLdb.Error, e:
			return "An error has been raised. %s" %e

	def fetchTweet(self):
		'''
			This method returns a random tweet from the Database
		'''
		randomNo = random.randint(1,10000);
		with self.db:
			cur=self.db.cursor()
			query = "Select `text` from `"+self.adb+"`.`tweet` where `iso_language` ='en' LIMIT "+`randomNo`+", "+`randomNo+1`
			cur.execute(query)
			temp = cur.fetchone()
			return temp[0]
