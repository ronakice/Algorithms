#sort
s=' '
A=[12,6,7,1,2,3,4,4]
B=[str(i) for i in A] 
print("A before sort: " + s.join(B))
A.sort()
B=[str(i) for i in A] 
print("A after sort: " + s.join(B))


   