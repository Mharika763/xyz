from Queue import Priority Queue
p=PriorityQueue()
p.put((1,"Naman"))
p.put((3,"Deepika"))
p.put((4,"Sikha"))
next=p.get()
print(next)
print(p.empty())
print(p.full())
p.put((2,"Aditya"))
print(p.get())
while not (p.empty()):
    print(p.get())
print(p.empty())
