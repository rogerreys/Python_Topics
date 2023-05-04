from A_node import Node

class SinglyLinkedList():
    def __init__(self) -> None:
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next

            current.next = node
        
        self.size += 1

    def size(self):
        return self.size
    
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def __str__(self) -> str:
        if self.tail == None:
            print("Sin datos")
            return
        
        current = self.tail
        res = ""
        while current.next:
            res += current.data + " "
            current = current.next
        res += current.data
        print(res)
    
    def delete(self, data):
        current = self.tail 
        previus = self.tail 
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previus.next = current.next
                    self.size -= 1
                    return current.data

            # Pasa al siguiente nodo
            previus = current
            current = current.next

    def search(self, data):
        current = self.tail
        founded = False
        for _ in range(self.size):
            if current.data == data:
                founded = True 
            current = current.next
        res = f"El dato {data} existe!!!" if founded else f"El dato {data} no existe"
        print(res)

    def clear(self):
        self.tail = None
        self.size = 0
        self.head = None


sll = SinglyLinkedList()
sll.append("Vale")
sll.append("Lucas")
sll.append("Maria")
sll.append("Ana")
sll.__str__()

sll.search("Pepe")

sll.clear()
sll.__str__()
