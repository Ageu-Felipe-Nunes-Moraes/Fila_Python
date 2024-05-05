
import time as t

class Queue:
    def __init__(self):
        self.list = []

    def empty(self):
        return len(self.list) == 0
    
    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if not self.empty():
            del(self.list[0])
        else:
            raise IndexError("A lista está vazia")
        
    def top(self):
        if not self.empty():
            return self.list[0]
        else:
            return None


queue = Queue()

for i in range(100+1):
    queue.push(i)
    print(f"Lista: {queue.list}\n")
    t.sleep(0.2)

print(f"Lista preenchida: {queue.list}\n")
print("Aguarde...\n")
t.sleep(3)

while not queue.empty():
    queue_first_item  = queue.top()
    queue.pop()
    print(f"Item removido da lista com sucesso: {queue_first_item}\n")
    print(f"Lista: {queue.list}\n")
    t.sleep(0.2)
