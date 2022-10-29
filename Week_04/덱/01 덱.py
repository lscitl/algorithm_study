# 문제
# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

class Deque:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def append(self, data):
        input_node  = Node(data)
        if self.head:
            input_node.prev = self.head.prev
            input_node.next = self.head
            self.head.prev.next = input_node
            self.head.prev = input_node
        else:
            self.head = input_node
        self.size += 1

    def appendleft(self, data):
        self.append(data)
        self.head = self.head.prev

    def pop(self):
        pop_node = self.head.prev
        pop_node.prev.next = pop_node.next
        pop_node.next.prev = pop_node.prev
        self.size -= 1
        if self.size == 0:
            self.head = None
        return pop_node.data

    def popleft(self):
        pop_node = self.head
        pop_node.prev.next = pop_node.next
        pop_node.next.prev = pop_node.prev
        self.size -= 1
        if self.size != 0:
            self.head = self.head.next
        else:
            self.head = None
        return pop_node.data
    
    def front(self):
        return self.head.data
    
    def back(self):
        return self.head.prev.data
	
def push_front(s, cmd):
    s.appendleft(int(cmd[-1]))

def push_back(s, cmd):
    s.append(int(cmd[-1]))

def pop_front(s, cmd):
    if len(s) == 0:
        print(-1)
    else:
        print(s.popleft())

def pop_back(s, cmd):
    if len(s) == 0:
        print(-1)
    else:
        print(s.pop())

def size(s, cmd):
    print(len(s))

def empty(s, cmd):
    if len(s) == 0:
        print(1)
    else:
        print(0)

def front(s, cmd):
    if len(s) == 0:
        print(-1)
    else:
        print(s.front())

def back(s, cmd):
    if len(s) == 0:
        print(-1)
    else:
        print(s.back())

if __name__ == "__main__":
    l = int(sys.stdin.readline())
    s = Deque()
    dic = {'push_front':push_front, 'push_back':push_back, 'pop_front':pop_front, 'pop_back':pop_back, 'size':size, 'empty':empty, 'front':front, 'back':back}
    for i in range(l):
        cmd = sys.stdin.readline().rstrip().split(" ")
        dic[cmd[0]](s, cmd)