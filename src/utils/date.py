from datetime import datetime


def get_current_time():
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return now_str
