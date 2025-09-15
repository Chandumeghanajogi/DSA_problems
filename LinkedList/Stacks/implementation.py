from collections import deque

stack=deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop()
stack.appendleft(400)
stack.popleft()
stack.extendleft([200,300])
stack.insert(1000,100000)


print(stack[-1])
print(list(stack))


s1=deque()
for i in range(100):
    s1.append(i)
s1.clear()
print(s1)

#to implement using the LifoQueue
from queue import LifoQueue

stack=LifoQueue(maxsize=3)

print(stack.qsize())
ans=stack[-1]
print(ans)

stack.put("chandu")
stack.put("meghana")
stack.put("jogi")

# print(stack.get())
print(stack.full())

print(stack.qsize())


