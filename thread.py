import threading
import time
import queue
import random

class Producer(threading.Thread):
    def __init__(self, id, queue):
        super().__init__()
        self.id = id
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            item = f"Item-{random.randint(1, 5)}"
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

    threads = []

    for i in range(num_producers):
        threads.append(Producer(i, shared_queue))

    for i in range(num_consumers):
        threads.append(Consumer(i, shared_queue))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))
    main(num_producers, num_consumers)
