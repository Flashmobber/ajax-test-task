import datetime

from parsing.parsing_bytes import (
    get_data_from_payload_1,
    get_data_from_payload_2,
)

if __name__ == "__main__":
    iterations = 1  # change this value to measure performance
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
