import hug
import json

from boxus import DB, Device

db = DB()

@hug.get('/')
def devices():
    ds = Device.all(db)
    return json.dumps(list(map(lambda d: d.to_dict(), ds)))

@hug.get('/{sid}')
def device(sid):
    d = Device.find(db, sid)
    return d.to_json()
