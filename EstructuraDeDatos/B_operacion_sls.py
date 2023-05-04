from A_node import Node

# * Creación de los nodos enlazados (linked list)
head=None
for i in range(1,6):
    head = Node(i, head) 


# * Recorrer e imprimir valores de la lista
def getValues(probe = head):
    print("Recorrido de la lista:")
    while probe.next != None:
        print(probe.data)
        probe = probe.next
    print(probe.data)



# * Busqueda de un elemento
def search(probe = head, target_item = 2):

    while probe != None and target_item != probe.data:
        probe = probe.next

    if probe != None:
        print(f'\nTarget item {target_item} has been found')
    else:
        print(f'\nTarget it {target_item} has not been found')



# * Remplazo de un elemento
def reepla(probe = head, target_item = 3, new_item = "Z"):

    while probe != None and target_item != probe.data:
        probe = probe.next

    if probe != None:
        probe.data = new_item
        print(f"\n{new_item} replace the old value in the node number {target_item}")
    else:
        print(f"\nThe target item {target_item} is not in the linked list")


# * Eliminar el ultimo Nodo
def deleteNode(head):
    if head.next is None:
        head = None
    else: 
        probe = head
        while probe.next.next != None:
            probe = probe.next
        remove_item = probe.next.data
        probe.next = None
        print(f"\nremove_item {remove_item}")


# * Agragar Valor
def addValueIndex(new_item, index=0):
    if head is None or index<1:
        head = Node(new_item, head)
    else: 
        probe = head
        while index>1 and probe.next!=None:
            probe = probe.next
            index -= 1 
        probe = Node(new_item, probe.next)


# * Eliminar por index
def deleteIndex(index=0):
    if index<=0 or head.next is None:
        remove_item = head.data
        head = head.next
    else: 
        probe = head
        while index>1 and probe.next.next !=None:
            probe = probe.next
            index -= 1
        remove_item = probe.data
        probe.next = probe.next.next
        print(remove_item)      

getValues()
