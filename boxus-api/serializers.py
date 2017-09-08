import json

def collection_to_json(collection, fields=None):
    return json.dumps(list(map(lambda r: r.to_dict(fields), collection)))
