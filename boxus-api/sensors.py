import hug

from marshmallow import fields
from boxus import DB, Sensor

from .serializers import *

db = DB()

@hug.get('/')
def sensors():
    sensors = Sensor.all(db)
    return collection_to_json(sensors)

@hug.get('/{sid}')
def sensor(sid):
    sensor = Sensor.find(db, sid)
    return sensor.to_json()

@hug.get('/{sid}/readings', examples='period=2-weeks&limit=100')
def sensor_readings(sid,
                    limit:int=None,
                    period:hug.types.text=None,
                    since:fields.DateTime()=None,
                    order:hug.types.text=None):
    if order:
        assert(order.lower() in ['asc', 'desc'])

    sensor = Sensor.find(db, sid)

    options = {}

    if limit:
        options['limit'] = limit
    if order:
        if order.lower() == 'asc':
            options['descending'] = False
        elif order.lower() == 'desc':
            options['descending'] = True

    if since:
        return collection_to_json(sensor.readings_since(since, options), ['created_at', 'values'])
    elif period:
        pars = period.split('-')
        return collection_to_json(sensor.readings_for(int(pars[0]), pars[1], options), ['created_at', 'values'])
    else:
        return collection_to_json(sensor.readings(options), ['created_at', 'values'])
