import queue

q=queue.Queue()

print(q.empty())
q.put('item-1')
q.put('item-2')
print(q.empty())
print(q.get())
print(q.get())
#print(q.get(block=False))
print(q.get_nowait)
print(q.empty())

q2=queue.Queue(maxsize=2)
q2.put('item-111')
q2.put('item-222')
q2.put_nowait('item-333')
#q2.put('item-333', block=False)
print(q2.full)




