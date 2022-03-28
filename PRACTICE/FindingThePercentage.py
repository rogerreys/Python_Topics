#Sample Input 1
#   2
#   Harsh 25 26.5 28
#   Anurag 26 28 30
#   Harsh
#
#Sample Output 1
#   26.50
#

#Another Input
#   3
#   Krishna 67 68 69
#   Arjun 70 98 63
#   Malika 52 56 60
#   Malika
#OUTPUT
#   56.00


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
    
if str(query_name) in student_marks:
    note = student_marks[query_name]
    res=0.0E-10
    res = sum(note)
    #for x in range(3):
    #    res+=float(note[x])

    print("%.2f"%(res/len(note)))
