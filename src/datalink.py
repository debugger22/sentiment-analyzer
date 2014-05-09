import MySQLdb
import random
import time


class DatabaseConnectionDown:

    def __init__(self, adb):
        '''
        This initializes the Database Connection for downlink
        @param DatabeseName
        '''
        self.adb = adb
        try:
            self.db = MySQLdb.connect(
                user='root',
                db=adb,
                passwd='adminpass',
                host='localhost')
        except MySQLdb.Error as e:
            print "An error has been raised. %s" % e

    def fetchTweet(self):
        '''
        This method returns a dictionary of tweet and its timestamp from the Database
        DictKeys: 'tweet', 'time'
        '''
        randomNo = random.randint(1, 10000)
        with self.db:
            cur = self.db.cursor()
            query = "Select `text`, `created_at` from `" + self.adb + \
                "`.`tweet` where `iso_language` ='en' LIMIT " + repr(randomNo) + ", " + repr(randomNo + 1)
            cur.execute(query)
            temp = cur.fetchone()
            return {'tweet': temp[0], 'time': int(
                time.mktime(time.strptime(str(temp[1]), '%Y-%m-%d %H:%M:%S')))}

    def fetchTweets(self, limit):
        '''
        This method returns a dictionary of list of tweets and list of timestamps from the Database
        DictKeys: 'tweets', 'time'
        '''
        with self.db:
            cur = self.db.cursor()
            query = "Select `text`, `created_at` from `" + self.adb + \
                "`.`tweet` where `iso_language` ='en' LIMIT 0," + repr(limit)
            cur.execute(query)
            temp = cur.fetchall()
            tweets = []
            timestamps = []
            for i in temp:
                tweets.append(i[0])
                timestamps.append(
                    int(time.mktime(time.strptime(str(i[1]), '%Y-%m-%d %H:%M:%S'))))
            return {'tweets': tweets, 'time': timestamps}
