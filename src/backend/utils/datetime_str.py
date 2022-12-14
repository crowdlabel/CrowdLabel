import datetime

def datetime_now_str():
    return datetime.utcnow().strftime('%Y-%m-%d_%H.%M.%S.%f')[:-3]