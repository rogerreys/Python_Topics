from A_node import Node

index = 1
new_item = 'ham'
head = Node(None,Node)

head.next = head
probe = head
# print(probe.data, probe.next)

while index>0 and probe.next != head:
    probe = probe.next    
    index -= 1

# probe.next = Node(new_item, probe.next)
# print(probe.next.data, probe.next, probe)

for i in range(5):
    probe.next = Node(i, probe.next)

i = 20
while i>0:
    print(f"DATA:{probe.data}, NEXT:{probe.next}, ID:{probe}")
    probe = probe.next
    i-=1
