#sort
s=' '
A=[12,6,7,1,2,3,4,4]
B=[str(i) for i in A] 
print("A before sort: " + s.join(B))
A.sort()
B=[str(i) for i in A] 
print("A after sort: " + s.join(B))
#bisection search
import bisect 
#bisect_left(A,x) gives position before first x
#bisect_right(A,x) gives position after last x
print("4 is located in position " +str(bisect.bisect_left(A,4)+1)+" from the left.")
print("4 is located in position " +str(bisect.bisect_right(A,4))+" from the right.")

#bisection inset
bisect.insort_left(A,5)#bisect.insort_right(A,5) inserts after last five
B=[str(i) for i in A] 
print("A after insert: " + s.join(B))


   