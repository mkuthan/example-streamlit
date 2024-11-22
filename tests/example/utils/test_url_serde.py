from example.utils import url_serde


def test_encode_decode():
    input_dict = {"key1": "value1", "key2": 2}
    encoded = url_serde.encode(input_dict)
    output_dict = url_serde.decode(encoded)
    assert output_dict == input_dict
