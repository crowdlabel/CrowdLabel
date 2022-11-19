def encode_list(li):
    return li.join('|')


def decode_str(str):
    return str.split('|')