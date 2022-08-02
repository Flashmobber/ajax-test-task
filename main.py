import datetime

from parsing.parsing_bytes import (
    get_data_from_payload_1,
    get_data_from_payload_2,
    set_data_into_payload,
)

if __name__ == "__main__":
    iterations = 1000
    payload = "10FA0E00"
    start = datetime.datetime.now()
    for _ in range(iterations):
        get_data_from_payload_1(payload)
    print(payload, get_data_from_payload_1(payload))
    print(datetime.datetime.now() - start)

    start = datetime.datetime.now()
    for _ in range(iterations):
        get_data_from_payload_2(payload)
    print(payload, get_data_from_payload_2(payload))
    print(datetime.datetime.now() - start)

    set_data_into_payload(
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
        }
    )
