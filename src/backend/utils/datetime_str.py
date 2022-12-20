from datetime import datetime

def datetime_now_str():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d_%H.%M.%S.%f')[:-3]