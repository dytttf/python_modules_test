# coding:utf-8
# import memory_profiler
# import sys
# sys.setrecursionlimit(100000)
@profile
def falone(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>=3:
        return falone(n-1)+falone(n-2)

# 命令行运行
# python -m memory_profiler test_memory_profiler.py


if __name__ == "__main__":
    falone(10)
