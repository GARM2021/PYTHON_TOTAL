mi_set = set((1,2,3,4,(1,2,3), 1,1,1,1,2,2)) #elimina los duplicados
print(2 in mi_set)

s1={1,2,3}
s2={3,4,5}
s3= s1.union(s2)
print(s3)

s1.add(4)

s1.remove(3)

s1.discard(6) # si no esta el 6 no marca error

s1.clear()

s1.add(4)

print(s1)
print(s2)
print(s3)




