import base64
import pickle
import urllib


def encode_to_url(value: dict) -> str:
    serialized = pickle.dumps(value)
    encoded = base64.b64encode(serialized)
    return urllib.parse.quote(encoded)


def decode_from_url(value: str) -> dict:
    encoded = urllib.parse.unquote(value)
    serialized = base64.b64decode(encoded)
    return pickle.loads(serialized)
