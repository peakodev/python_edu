from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()


for i in range(MAX_LEN + 2):
    push(i)
    print(lifo)

for i in range(MAX_LEN - 1):
    pop()
    print(lifo)
