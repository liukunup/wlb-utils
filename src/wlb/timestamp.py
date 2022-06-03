from typing import AnyStr
import time
import datetime
import pytz


def ts(req: AnyStr, fmt: AnyStr = "%Y-%m-%d %H:%M:%S.%f", tz: AnyStr = "Asia/Shanghai"):
    """
    返回时间戳(按照指定的要求)
    原始/秒级/毫秒级/微秒级/日期时间型
    raw/s/ms/us/datetime
    :param req: 需求
    :param fmt: 返回格式(仅在 日期时间型 情况下有效)
    :param tz:  时区(仅在 日期时间型 情况下有效)
    :return: 时间戳的值或字符串
    """
    # 获取浮点数的秒(1970-01-01 00:00:00 UTC)
    t = time.time()
    # 处理成各种时间戳以备使用
    ts_dict = {
        # 中文键名
        "原始": t,
        "秒级": int(t),
        "毫秒级": int(round(t * 1000)),
        "微秒级": int(round(t * 1000000)),
        "日期时间型": datetime.datetime.now(pytz.timezone(tz)).strftime(fmt),
        # 英文键名
        "raw": t,
        "s": int(t),
        "ms": int(round(t * 1000)),
        "us": int(round(t * 1000000)),
        "datetime": datetime.datetime.now(pytz.timezone(tz)).strftime(fmt),
    }
    # 当填写的需求不正确时将返回None
    return ts_dict.get(req)
