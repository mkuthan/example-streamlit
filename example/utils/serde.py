import base64
import pickle
import urllib


def encode_to_url(dict: dict) -> str:
    serialized = pickle.dumps(dict)
    encoded = base64.b64encode(serialized)
    return urllib.parse.quote(encoded)


def decode_from_url(str: str) -> dict:
    encoded = urllib.parse.unquote(str)
    serialized = base64.b64decode(encoded)
    return pickle.loads(serialized)
