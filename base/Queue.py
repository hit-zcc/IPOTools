import time
import threading
import queue
import random

q = queue.Queue


class Queue:
    @classmethod
    def putMessage(self, index, value):
        q.put((index, index))

    @classmethod
    def getMessage(self):
        while True:
            if not q.empty():
                print(q.get())
            else:
                time.sleep(random.random())

    @classmethod
    def status(self):
        print("size:%s" % q.qsize())  # 查看队列长度
        print("full:%s" % q.full())  # 查看队列是否为满的状态
        print("empty:%s" % q.empty()) # 查看队列是否为空的状态
