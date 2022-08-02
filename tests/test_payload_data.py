import pytest

from parsing.parsing_bytes import get_data_from_payload_1, get_data_from_payload_2


parameters_for_tests = (
    [
        (
            "10FA0E00",
            {
                "field1": "Low",
                "field2": "00",
                "field3": "01",
                "field4": "00",
                "field5": "00",
                "field6": "01",
                "field7": "00",
                "field8": "Very High",
                "field9": "00",
                "field10": "00",
            },
        ),
        (
            "AFD50F00",
            {
                "field1": "High",
                "field2": "01",
                "field3": "00",
                "field4": "50",
                "field5": "01",
                "field6": "00",
                "field7": "01",
                "field8": "Low",
                "field9": "01",
                "field10": "00",
            },
        ),
        (
            "E0EB1E00",
            {
                "field1": "Low",
                "field2": "00",
                "field3": "00",
                "field4": "70",
                "field5": "01",
                "field6": "01",
                "field7": "00",
                "field8": "High",
                "field9": "00",
                "field10": "00",
            },
        ),
        (
            "E42D6500",
            {
                "field1": "Medium",
                "field2": "00",
                "field3": "00",
                "field4": "70",
                "field5": "01",
                "field6": "00",
                "field7": "01",
                "field8": "High",
                "field9": "01",
                "field10": "01",
            },
        ),
        (
            "CFE33E00",
            {
                "field1": "High",
                "field2": "01",
                "field3": "00",
                "field4": "60",
                "field5": "01",
                "field6": "01",
                "field7": "00",
                "field8": "Medium",
                "field9": "00",
                "field10": "01",
            },
        ),
    ],
)


@pytest.mark.parametrize("payload, data", *parameters_for_tests)
def test_get_data_from_payload_1(payload, data):
    assert get_data_from_payload_1(payload) == data


@pytest.mark.parametrize("payload, data", *parameters_for_tests)
def test_get_data_from_payload_2(payload, data):
    assert get_data_from_payload_2(payload) == data
