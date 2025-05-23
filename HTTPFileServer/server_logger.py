# 简单的日志类
from datetime import datetime


class Logger:
    def __init__(self, time_format='%Y-%m-%d %H:%M:%S'):
        self.time_format = time_format

    def log(self, message):
        current_time = datetime.now().strftime(self.time_format)
        print(f'[{current_time}] {message}')
