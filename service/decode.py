import struct

def decode_hex_packet(hexa, byte):
    res = bytes.fromhex(hexa)[byte:byte+4]
    return round(struct.unpack("!f", res)[0], 2)

def recreate_response(device, timestamp, hexa):
    return {
        "device": device,
        "timestamp": timestamp,
        "temperature": decode_hex_packet(hexa, 0)
    }
