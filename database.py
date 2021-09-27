import time
import pymongo
from pymongo import MongoClient

from config import monogoUrl
client = pymongo.MongoClient(monogoUrl)
db = client.Instabot
insta_account = db.account



class insert:
    def __init__(self, user):
        self.user=user
    def insert(self):
        account = {
            "account" : self.user[2],
            "user_info" : self.user,
            "time" : time.ctime()
        }


        print(insta_account.insert_one(account))



'''
db = client.test1


people = db.people

personDocument = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}

people.insert_one(personDocument)

print(people.find_one({ "name.last": "Turing" }))

'''