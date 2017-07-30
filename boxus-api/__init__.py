import hug

from . import sensors
from . import devices
from . import readings


@hug.extend_api('/sensors')
def sensors_api():
    return [sensors]

@hug.extend_api('/devices')
def devices_api():
    return [devices]
