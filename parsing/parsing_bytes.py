test_data = [
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
]

# Format settings - array [sett_byte1 as dict {bit: [size, 'field_name']}, sett_byte2, sett_byte3, sett_byte4]
device_settings = [
    {0: [3, "field1"], 3: [1, "field2"], 4: [1, "field3"], 5: [3, "field4"]},
    {
        0: [1, "field5"],
        1: [1, "field6"],
        2: [1, "field7"],
        3: [3, "field8"],
    },
    {0: [1, "field9"], 5: [1, "field10"]},
    {},
]

field1 = {
    "0": "Low",
    "1": "reserved",
    "2": "reserved",
    "3": "reserved",
    "4": "Medium",
    "5": "reserved",
    "6": "reserved",
    "7": "High",
}
field4 = {
    "0": "00",
    "1": "10",
    "2": "20",
    "3": "30",
    "4": "40",
    "5": "50",
    "6": "60",
    "7": "70",
}
field8 = {
    "0": "Very Low",
    "1": "reserved",
    "2": "Low",
    "3": "reserved",
    "4": "Medium",
    "5": "High",
    "6": "reserved",
    "7": "Very High",
}


def get_bits(from_int, start, end):
    """Returns the sequence of bits the number 'from_int'
    starting from 'start' to 'end' bit"""
    mask = 2 ** (end - start) - 1
    return (from_int & (mask << start)) >> start


def get_data_from_payload_1(payload):
    """The first version of the solution is based on obtaining
    the desired bit using a bitwise shift."""
    int_payload = [payload[byte: byte + 2] for byte in range(0, len(payload), 2)]
    parsed_data, byte_index = {}, 0
    while byte_index < 4:
        for bit, params in device_settings[byte_index].items():
            if params[0] > 1:
                parsed_data[params[1]] = globals()[params[1]][
                    str(
                        get_bits(int(int_payload[byte_index], 16), bit, bit + params[0])
                    )
                ]
            else:
                parsed_data[params[1]] = str(
                    get_bits(int(int_payload[byte_index], 16), bit, bit + params[0])
                ).zfill(2)
        byte_index += 1
    return parsed_data


def get_data_from_payload_2(payload):
    """The second version of the solution is based on the
    conversion of a number into a bit string."""
    int_payload = int(payload, 16)
    binary_payload = bin(int_payload).removeprefix("0b").zfill(32)
    parsed_data, bit_index = {}, 8
    for byte in device_settings:
        for bit, param in byte.items():
            if param[1] in globals():
                parsed_data[param[1]] = globals()[param[1]][
                    str(
                        int(
                            binary_payload[
                                -len(binary_payload)
                                + bit_index
                                - bit
                                - param[0]: -len(binary_payload)
                                + bit_index
                                - bit
                            ],
                            2,
                        )
                    )
                ]
            else:
                parsed_data[param[1]] = str(
                    binary_payload[
                        -len(binary_payload)
                        + bit_index
                        - bit
                        - param[0]: -len(binary_payload)
                        + bit_index
                        - bit
                    ]
                ).zfill(2)
        bit_index += 8
    return parsed_data


def set_data_into_payload(data) -> str:
    """This is an approximate possible variant of encoding the structure into
    a bit sequence. I don't know the possible values of bits 6 and 7 in the
    second byte, and bits 1, 2, 3, 4, 6, and 7 in the third byte.
    Therefore, I do not claim the absolute correctness of this function.
    I leave it only as an example."""
    binary_string = ""
    for byte in device_settings:
        current_byte = ""
        for bit, param in byte.items():
            if param[1] in globals():
                for key, value in globals()[param[1]].items():
                    if value == data[param[1]]:
                        current_byte = (
                            bin(int(key)).removeprefix("0b").zfill(3) + current_byte
                        )
                        break
            elif param[1] == "field9":
                current_byte = "111" + str(int(data[param[1]], 2)) + current_byte
            else:
                current_byte = str(int(data[param[1]], 2)) + current_byte
        if byte != {} and len(byte) > 2:
            filler = "1"
        else:
            filler = "0"
        while len(current_byte) < 8:
            current_byte = filler + current_byte
        binary_string += current_byte.zfill(8)
    payload = str(hex(int(binary_string, 2))).removeprefix("0x").upper()
    print(payload, data)
    return payload
