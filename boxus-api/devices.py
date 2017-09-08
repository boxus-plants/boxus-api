import hug

from boxus import DB, Device

from .serializers import *

db = DB()

@hug.get('/')
def devices():
    devices = Device.all(db)
    return collection_to_json(devices)

@hug.get('/{did}')
def device(did):
    d = Device.find(db, did)
    return d.to_json()

@hug.get('/{did}/on')
def device(did):
    d = Device.find(db, did)
    d.on()
    return True

@hug.get('/{did}/off')
def device(did):
    d = Device.find(db, did)
    d.off()
    return True

@hug.get('/{did}/on_for', examples='period=2-seconds')
def device(did, period:hug.types.text):
    d = Device.find(db, did)

    pars = period.split('-')
    d.on_for(int(pars[0]), pars[1])
    return True
