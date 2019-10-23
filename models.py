import mongoengine as mongo
import datetime

class AQvalues(mongo.Document):
    date = mongo.DateTimeField(datetime.datetime.now())
    pm25 = mongo.DecimalField()
    pm10 = mongo.DecimalField()