
import time as t

class Fila:
    def __init__(self):
        self.lista = []

    def vazia(self):
        return len(self.lista) == 0
    
    def push(self, item):
        self.lista.append(item)
    
    def pop(self):
        if not self.vazia():
            del(self.lista[0])
        else:
            raise IndexError("A lista está vazia")
        
    def top(self):
        if not self.vazia():
            return self.lista[0]
        else:
            return None


fila = Fila()

for i in range(100+1):
    fila.push(i)
    print(f"Lista: {fila.lista}\n")
    t.sleep(0.2)

print(f"Lista preenchida: {fila.lista}\n")
print("Aguarde...\n")
t.sleep(3)

while not fila.vazia():
    primeiro_item_lista = fila.top()
    fila.pop()
    print(f"Item removido da lista com sucesso: {primeiro_item_lista}\n")
    print(f"Lista: {fila.lista}\n")
    t.sleep(0.2)
