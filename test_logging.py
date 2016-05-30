# coding:utf8
import logging

# 测试logging打印异常
def main():
    1/0
    return

try:
    main()
except Exception as e:
    logging.exception(e)
