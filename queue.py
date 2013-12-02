from random import randint

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def printer_simulation(seconds, print_time):
    printer_queue = Queue()
    printing = None
    printer_busy = False
    timestamps = []
    for current_second in range(seconds):
        if randint(1,180) == 180:
            printer_queue.enqueue((current_second, randint(1,20)))
        if not printer_busy and not printer_queue.isEmpty():
            printing = printer_queue.dequeue()
            timestamps.append(current_second - printing[0])
            job_time = printing[1] * print_time
            printer_busy = True
        if printer_busy:
            job_time -= 1
            if job_time == 0:
                printer_busy = False

    return sum(timestamps)/len(timestamps)

print printer_simulation(3600, 12)
