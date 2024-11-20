from example.utils import serde


def test_encode_decode():
    input_dict = {"key1": "value1", "key2": 2}
    encoded = serde.encode_to_url(input_dict)
    output_dict = serde.decode_from_url(encoded)
    assert output_dict == input_dict
