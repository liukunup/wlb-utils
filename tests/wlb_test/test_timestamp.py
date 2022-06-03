import unittest
import time
from src.wlb import timestamp


class TimestampTestCase(unittest.TestCase):

    def test_ts(self):
        # 获取当前时间
        t = time.time()
        print("当前测试时间值", t)
        # 测试 ts() 函数的不同分支
        # 取 原始 时间戳
        print("原始", timestamp.ts("原始"))
        self.assertGreaterEqual(timestamp.ts("原始"), t, "函数ts()的分支'原始'情况测试失败!")
        # 取 秒级 时间戳
        print("秒级", timestamp.ts("秒级"))
        self.assertGreaterEqual(timestamp.ts("秒级"), int(t), "函数ts()的分支'秒级'情况测试失败!")
        # 取 毫秒级 时间戳
        print("毫秒级", timestamp.ts("毫秒级"))
        self.assertGreaterEqual(timestamp.ts("毫秒级"), int(round(t * 1000)), "函数ts()的分支'毫秒级'情况测试失败!")
        # 取 微秒级 时间戳
        print("微秒级", timestamp.ts("微秒级"))
        self.assertGreaterEqual(timestamp.ts("微秒级"), int(round(t * 1000000)), "函数ts()的分支'微秒级'情况测试失败!")
        # 取 日期时间型 时间戳
        print("日期时间型", timestamp.ts("日期时间型"))
        self.assertEqual(type(timestamp.ts("日期时间型")), str, "函数ts()的分支'日期时间型'情况返回类型测试失败!")
        self.assertEqual(len(timestamp.ts("日期时间型")), 26, "函数ts()的分支'日期时间型'情况返回值长度测试失败!")


if __name__ == '__main__':
    unittest.main()
