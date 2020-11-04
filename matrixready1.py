print("Программа для сложения и умножения двух матриц")
a=[]
b=[]
u=[]
z=[]
w=[]
k=0
q=0
i=0
j=0
o=0
p=0
print("Введите размер матриц по одной грани")
d=int(input())

print("Введите элементы первой матрицы")
while k<2:
    while i<d**2:
        while j<d**2:
            a.append(int(input()))
            j=j+1
        i=i+1
    k=k+1


print("Введите элементы второй матрицы")
while q<2:
    while o<d**2:
        while p<d**2:
            b.append(int(input()))
            p=p+1
        o=o+1
    q=q+1
print("Для сложения матриц введите 0, для умножения - 1")
u=int(input())
if u==0:
    if d==2:
        c=a[0]+b[0]
        d=a[1]+b[1]
        e=a[2]+b[2]
        f=a[3]+b[3]
        z.append(c)
        z.append(d)
        z.append(e)
        z.append(f)
        print(z)

    if d==3:
        g=a[0]+b[0]
        h=a[1]+b[1]
        l=a[2]+b[2]
        m=a[3]+b[3]
        n=a[4]+b[4]
        r=a[5]+b[5]
        s=a[6]+b[6]
        t=a[7]+b[7]
        v=a[8]+b[8]
        w.append(g)
        w.append(h)
        w.append(l)
        w.append(m)
        w.append(n)
        w.append(r)
        w.append(s)
        w.append(t)
        w.append(v)
        print(w)

if u==1:
    if d==2:
        c=a[0]*b[0]+a[1]*b[2]
        d=a[0]*b[1]+a[1]*b[3]
        e=a[2]*b[0]+a[3]*b[2]
        f=a[2]*b[1]+a[3]*b[3]
        z.append(c)
        z.append(d)
        z.append(e)
        z.append(f)
        print(z)

    if d==3:
        g=a[0]*b[0]+a[1]*b[3]+a[2]*b[6]
        h=a[0]*b[1]+a[1]*b[4]+a[2]*b[7]
        l=a[0]*b[2]+a[1]*b[5]+a[2]*b[8]
        m=a[3]*b[0]+a[4]*b[3]+a[5]*b[6]
        n=a[3]*b[1]+a[4]*b[4]+a[5]*b[7]
        r=a[3]*b[2]+a[4]*b[5]+a[5]*b[8]
        s=a[6]*b[0]+a[7]*b[3]+a[8]*b[6]
        t=a[6]*b[1]+a[7]*b[4]+a[8]*b[7]
        v=a[6]*b[2]+a[7]*b[5]+a[8]*b[8]
        w.append(g)
        w.append(h)
        w.append(l)
        w.append(m)
        w.append(n)
        w.append(r)
        w.append(s)
        w.append(t)
        w.append(v)
        print(w)
















