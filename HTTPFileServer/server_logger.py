import logging


class Logger:
    def __init__(self, time_format='%Y-%m-%d %H:%M:%S'):
        # 创建 logger 实例
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # 默认日志级别为 DEBUG

        # 创建日志格式器，使用用户指定的时间格式
        formatter = logging.Formatter(
            fmt='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt=time_format
        )

        # 创建控制台处理器
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # 添加处理器到 logger
        self.logger.addHandler(handler)

    def log(self, message, level='info'):
        """
        记录日志
        :param message: 日志内容
        :param level: 日志级别（字符串或整数）
        """
        if isinstance(level, str):
            level = level.upper()
            if not hasattr(logging, level):
                raise ValueError(f"Invalid logging level: {level}")
            level = getattr(logging, level)

        self.logger.log(level, message)
