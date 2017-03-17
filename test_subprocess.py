#coding:utf8
"""
subprocess模块用于替代旧模块的一些方法
例如:
    os.system
    os.popen
    ...
"""
import subprocess


stdout_file = open("test_stdout.txt", "w")

# Popen 类
#__init__(self, args, bufsize=0, executable=None, stdin=None,
#   stdout=None, stderr=None, preexec_fn=None, close_fds=False,
#   shell=False, cwd=None, env=None, universal_newlines=False,
#   startupinfo=None, creationflags=0)

"""
参数:
args: 执行的命令 类型为 str list tuple
    例如 ls   不能是ls -l
        ["ls", "-l"]
        
bufsize: 指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲(全缓冲)

preexec_fn: 只在Unix平台下有效，用于指定一个可执行对象（callable object）
        它将在子进程运行之前被调用。

close_fds:在windows平台下，如果close_fds被设置为True，
    则新创建的子进程将不会继承父进程的输入、输出、错误管道。
    我们不能将close_fds设置为True同时重定向子进程的标准输入、输
    出与错误(stdin, stdout, stderr)

shell:

cwd: 设置子进程当前目录

env: 是字典类型，用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。

universal_newlines: 设为True 则换行符统一按照linux标准
"""

# 创建一个子进程用于执行指定命令 非阻塞模式运行
child_process = subprocess.Popen("dir", stdout=stdout_file, shell=True)

# 等待直到子进程结束 阻塞模式 返回returncode
#returncode = child_process.wait()
# 检查子进程状态 非阻塞 returncode
returncode = child_process.poll()

#
(stdoutdata, stderrdata) = child_process.communicate()

child_process.kill()

#child_process.send_signal()

