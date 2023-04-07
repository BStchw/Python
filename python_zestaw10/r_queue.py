#Zadanie 10.8

from collections import deque
import random


class RandomQueue:

    def __init__(self):
        self.data = deque()

    def insert(self, item: int):
        self.data.append(item)
        self.data.rotate(random.randint(-5, 5))

    def remove(self)->int:
        self.data.rotate(random.randint(-5, 5))
        return self.data.pop()

    def is_empty(self)->bool:
        return len(self.data) == 0

    def is_full(self):
        return False

rand_q = RandomQueue()

rand_q.insert(14)
rand_q.insert(28)
rand_q.insert(19)
rand_q.insert(7)

print(rand_q.is_empty())

print(rand_q.remove())