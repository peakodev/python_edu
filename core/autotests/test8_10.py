from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():
    return fifo.popleft()


for i in range(MAX_LEN + 2):
    push(i)
    print(fifo)

for i in range(MAX_LEN - 1):
    pop()
    print(fifo)
