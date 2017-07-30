import hug
import json

from boxus import DB, Sensor

db = DB()

@hug.get('/')
def sensors():
    sensors = Sensor.all(db)
    return json.dumps(list(map(lambda s: s.to_dict(), sensors)))

@hug.get('/{sid}')
def sensor(sid):
    sensor = Sensor.find(db, sid)
    return sensor.to_json()
