flag='flag'
flag1=[]
for i in flag:
    flag1.append(ord(i))

print(flag1)


def xor(a):
    return a^23

def shift(b):
    return b+34

flagenc=[]



for i in flag1:
        if i%2==0:
             flagenc.append(xor(i))
        if i%2==1:
             flagenc.append(shift(i))


print(flagenc)
    
            
#flag output: [115, 145, 121, 121, 151, 101, 67, 81, 157, 153, 127, 135, 101, 135, 129, 139, 149, 129, 155, 145, 151, 101, 129, 113, 123, 131, 137, 159]
