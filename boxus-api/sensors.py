import hug
import json

from marshmallow import fields

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

@hug.get('/{sid}/readings', examples='period=2-weeks&limit=100')
def sensor_readings(sid,
                    limit:int=None,
                    period:hug.types.text=None,
                    since:fields.DateTime()=None):
    sensor = Sensor.find(db, sid)

    options = {}

    if limit:
        options['limit'] = limit

    if since:
        return json.dumps(list(map(lambda r: r.to_dict(['created_at', 'values']), sensor.readings_since(since, options))))
    elif period:
        pars = period.split('-')
        return json.dumps(list(map(lambda r: r.to_dict(['created_at', 'values']), sensor.readings_for(int(pars[0]), pars[1], options))))
    else:
        return json.dumps(list(map(lambda r: r.to_dict(['created_at', 'values']), sensor.readings(options))))
