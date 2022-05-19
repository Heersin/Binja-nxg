def try_str2addr_or_neg_one(hex_or_int_str):
    result = -1
    try:
        if '0x' in hex_or_int_str:
            result = int(hex_or_int_str, base=16)
        else:
            result = int(hex_or_int_str)
    except:
        print("[BNG ERROR] Support hex or integer input")
    finally:
        return result