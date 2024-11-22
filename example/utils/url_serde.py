import base64
import pickle
import urllib


def encode(value: dict) -> str:
    serialized = pickle.dumps(value)
    encoded = base64.b64encode(serialized)
    return urllib.parse.quote(encoded)


def decode(value: str) -> dict:
    encoded = urllib.parse.unquote(value)
    serialized = base64.b64decode(encoded)
    return pickle.loads(serialized)
