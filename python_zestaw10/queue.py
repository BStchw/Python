#Zadanie 10.4

import unittest

class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.n == self.head

    def put(self, data):
        if((self.tail + 1) % self.n == self.head):
            raise ValueError("Kolejka jest pelna")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if (self.head == self.tail):
            raise ValueError("Kolejka jest pusta")
        data = self.items[self.head]
        self.items[self.head] = None   # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q1 = Queue(5)
        self.q2 = Queue(2)
        self.q2.put(17)
        self.q2.put(12)

    def test_is_empty(self):
        self.assertTrue(self.q1.is_empty() == True)
        self.assertTrue(self.q2.is_empty() == False)

    def test_is_full(self):
        self.assertTrue(self.q1.is_full() == False)
        self.assertTrue(self.q2.is_full() == True)

    def test_put(self):
        self.q1.put(56)
        self.assertEqual(self.q1.head, 0)
        self.assertEqual(self.q1.tail, 1)
        self.assertEqual(self.q1.get(), 56)

    def test_get(self):
        self.assertEqual(self.q2.get(), 17)
        self.assertEqual(self.q2.head, 1)
        self.assertEqual(self.q2.tail, 2)