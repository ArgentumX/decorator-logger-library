from functools import wraps
from loguru import logger

from decorator_logging.decorator_logging.log_level import LogLevel
from decorator_logging.decorator_logging.log_timing import LogTiming


class SyncLoggable:
    def __init__(self, log_level: LogLevel = LogLevel.INFO, log_timing: str = LogTiming.BOTH):
        self.log_level = log_level
        self.log_timing = log_timing
        if log_level == LogLevel.DEBUG:
            self.log_func = logger.debug
        elif log_level == LogLevel.INFO:
            self.log_func = logger.info
        elif log_level == LogLevel.WARNING:
            self.log_func = logger.warning
        elif log_level == LogLevel.ERROR:
            self.log_func = logger.error
        elif log_level == LogLevel.CRITICAL:
            self.log_func = logger.critical

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.log_timing in (LogTiming.BEFORE, LogTiming.BOTH):
                self.log_func(f"Executing {func.__name__} with args: {list(map(str, args))}")
            result = func(*args, **kwargs)
            if self.log_timing in (LogTiming.AFTER, LogTiming.BOTH):
                self.log_func(f"Success {func.__name__} returned: {result}")

            return result

        return wrapper

class AsyncLoggable:
    def __init__(self, log_level: LogLevel = LogLevel.INFO, log_timing: str = LogTiming.BOTH):
        self.log_level = log_level
        self.log_timing = log_timing
        if log_level == LogLevel.DEBUG:
            self.log_func = logger.debug
        elif log_level == LogLevel.INFO:
            self.log_func = logger.info
        elif log_level == LogLevel.WARNING:
            self.log_func = logger.warning
        elif log_level == LogLevel.ERROR:
            self.log_func = logger.error
        elif log_level == LogLevel.CRITICAL:
            self.log_func = logger.critical

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if self.log_timing in (LogTiming.BEFORE, LogTiming.BOTH):
                self.log_func(f"Executing {func.__name__} with args: {list(map(str, args))}")
            result = await func(*args, **kwargs)
            if self.log_timing in (LogTiming.AFTER, LogTiming.BOTH):
                self.log_func(f"Success {func.__name__} returned: {result}")

            return result

        return wrapper