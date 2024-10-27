import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Empty(Exception):
    pass

class LinkedStack:
    # --- Node class ---
    class _Node:
        __slots__ = '_element', '_next'  # faster memory access

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # --- Stack methods ---
    def __init__(self):  # empty stack
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


def timePush(stack_size, n=20):
    end = 0
    for i in range(n):
        stack = LinkedStack()
        start = time.time()
        for j in range(stack_size):
            stack.push(0)
        end += time.time() - start
    return end/n


def timePop(stack_size, n=20):
    end = 0
    for i in range(n):
        stack = LinkedStack()
        start = time.time()
        for j in range(stack_size):
            stack.push(0)
        for j in range(stack_size):
            stack.pop()
        end += time.time() - start
    return end / n


def timeTop(stack_size, n=20):
    end = 0
    for i in range(n):
        stack = LinkedStack()
        start = time.time()
        for j in range(stack_size):
            stack.push(i)
        for j in range(stack_size):
            stack.top()
        end += time.time() - start
    return end / n


sizes = [_*1000 for _ in range(1, 101)]  # Przykładowe rozmiary stosu do przetestowania
push_times = []
pop_times = []
top_times = []

for size in sizes:
    push_times.append(timePush(size))
    pop_times.append(timePop(size))
    top_times.append(timeTop(size))


plt.plot(sizes, push_times, label='Push')
plt.plot(sizes, pop_times, label='Pop')
plt.plot(sizes, top_times, label='Top')
plt.xlabel('Rozmiar stosu')
plt.ylabel('Czas (s)')
plt.legend()
plt.title('Wydajność operacji na stosie')
plt.show()
