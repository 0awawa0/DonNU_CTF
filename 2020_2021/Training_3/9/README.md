# 9

## Task

```Python
from string import printable


class Shuffler:

    def __init__(self, d):
        self.d = d
        self.c = 0
    
    def do_switch(s, i, j):
        t = s[j]
        s[j] = s[i]
        s[i] = t
        return s

    def get_shuffled(self, deck):
        
        s = list(deck)
        l = (len(s) // 2 - self.d) % len(s)
        r = l + 1

        i = l
        j = 0
        while i > j:
            s = Shuffler.do_switch(s, i, j)
            i -= 1
            j += 1
            self.c += 1

        i = r
        j = len(s) - 1

        while i < j:
            s = Shuffler.do_switch(s, i, j)
            i += 1
            j -= 1
            self.c += 1

        return "".join(s)


class Encoder:

    def __init__(self, c):
        self.c = c
        self.d = {}
        for i in printable:
            self.d[i] = printable[(printable.find(i) + self.c) % len(printable)]

    def encode(self, deck):
        result = list(deck)
        for i in range(len(result)):
            result[i] = self.d[result[i]]
        return "".join(result)


if __name__ == "__main__":

    d = int(input("Enter shuffler initializer >> "))
    shuffler = Shuffler(d)

    s = input("Now gimme some deck >> ")
    deck = shuffler.get_shuffled(s)
    
    encoder = Encoder(shuffler.c)
    print(encoder.encode(deck).encode().hex())
    # 534b44444574384974487173346a436749346a4276764b7849346c4a754236562a
```

## Solution