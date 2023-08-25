import threading
import time
import queue
import random
import sys

class Producer(threading.Thread):
    def __init__(self, id, queue):
        super().__init__()
        self.id = id
        self.queue = queue

    def run(self):
        for i in range(5):
            item = f"Item-{random.randint(1, 10)}"
            print(f"Producer-{self.id} produced {item}")
            self.queue.put(item)
            time.sleep(random.random())

class Consumer(threading.Thread):
    def __init__(self, id, queue):
        super().__init__()
        self.id = id
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            print(f"Consumer-{self.id} consumed {item}")
            self.queue.task_done()
            time.sleep(random.random())

def main(num_producers, num_consumers):
    shared_queue = queue.Queue()

    producers = [Producer(i, shared_queue) for i in range(num_producers)]
    consumers = [Consumer(i, shared_queue) for i in range(num_consumers)]

    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    for producer in producers:
        producer.join()

    for _ in range(num_consumers):
        shared_queue.put(None)

    for consumer in consumers:
        consumer.join()

if __name__ == "__main__":
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))
    main(num_producers, num_consumers)
