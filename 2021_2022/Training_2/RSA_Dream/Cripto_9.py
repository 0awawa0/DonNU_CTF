import random
def gcd(a,b): #расширенный
    x, lasty=0,0
    y, lastx=1,1
    n=a
    m=b
    while m!=0:
        q=n//m
        r=n%m
        n=m
        m=r
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y
    return n

def gcdost(a,b): #расширенный
    x, lasty=0,0
    y, lastx=1,1
    n=a
    m=b
    while m!=0:
        q=n//m
        r=n%m
        n=m
        m=r
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y
    return lastx

def pmnoj(a):
    p = []
    d = 2
    while d * d <= a:
        if a % d == 0:
            p.append(d)
            a //= d
        else:
            d += 1
    if a > 1:
        p.append(a)
    return p

def ferma(c):
    for i in range(1000):
        a=random.randint(2, c-2)
        b=a**(c-1)%c
        if b==1:
             return True
        else:
             return False

def rsa(st1, p,q):
    st2=[]
    res=[]
    res2=[]
    p1=ferma(p)
    q1=ferma(q)
    if not p1 or not q1:
        return "Error"
    for i in range(len(st1)):
        for j in range(len(alf)):
            if st1[i]==alf[j]:
                st2.append(zam[j])
    n=p*q
    fn=(p-1)*(q-1)
    i=2
    while i < fn:
        e=gcd(fn,i)
        if e==1:
            e=i
            break
        i+=1
    d=gcdost(e,fn)
    if d<0:
        d+=fn
    for i in st2:
        res.append((i**e)%n)
    for i in res:
        res2.append((i**d)%n)
    return res,res2


alf=["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я",".",",",":","?"]
zam=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
p=17
q=11
file=open('text.txt',encoding='utf-8')
st1=list(file.read())
file.close()
print(st1)
f,f2=rsa(st1,p,q)
s=sum(f)
print(s)
print(f,f2)

