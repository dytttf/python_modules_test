# coding:utf-8
import cProfile
import pstats


def foo():
    result = 0
    for i in range(100):
        result += i
    return result

# cProfile.run('foo()', 'prof.txt')
p = pstats.Stats('prof.txt')
# p.sort_stats('time').print_stats()
p.sort_stats('time').print_stats(10)
p.sort_stats('time').print_stats('.1', 'foo:')

if __name__ == "__main__":
    pass
