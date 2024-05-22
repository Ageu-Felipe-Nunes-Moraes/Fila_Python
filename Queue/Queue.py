
import time as t # Time Method

# Class for queue operations
class Queue:
    # Initial function
    def __init__(self):
        self.list = []

    # Function that checks if it is empty
    def empty(self):
        return len(self.list) == 0
    
    # Puts item in the final list
    def push(self, item):
        self.list.append(item)
    
    # Removes the first item from the list
    def pop(self):
        # Only delete the item from the list if it is not empty
        if not self.empty():
            del(self.list[0])
        else:
            raise IndexError("A lista está vazia")
    
    #  Stores the first item in the list in a variable
    def top(self):
        # Return a value only if the list is different from empty
        if not self.empty():
            return self.list[0]
        else:
            return None

# Declare of the class
queue = Queue()

# Fills the list with 100 numbers
for i in range(100+1):
    queue.push(i)
    print(f"Lista: {queue.list}\n")
    t.sleep(0.2)

print(f"Lista preenchida: {queue.list}\n")
print("Aguarde...\n")
t.sleep(3)

# Emptying the entire list
while not queue.empty():
    queue_first_item  = queue.top()
    queue.pop()
    print(f"Item removido da lista com sucesso: {queue_first_item}\n")
    print(f"Lista: {queue.list}\n")
    t.sleep(0.2)
