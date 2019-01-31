f = open('vertices.txt','r')
f=f.read()
f=f.split('\n')
for i in range(len(f)):
    f[i]=f[i].split(',')

for i in range(40):
    for j in range(40):
        if f[i][j] != '-':
            f[i][j]=int(f[i][j])
        else:
            f[i][j]=10000

z=0            
for i in f:
    z=z+sum(i)

t=[0]
A=f
e=[0]
for i in range(40):
    A[i][0]=10000
while len(t)<40:
    smallest=10000
    for i in t:
        if min(A[i])<=smallest:
            smallest=min(A[i])
            ind=A[i].index(min(A[i]))
    for i in range(40):
        A[i][ind]=10000
    t.append(ind)
    e.append(smallest)
