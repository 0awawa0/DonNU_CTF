# 10

## Task

```Lisp
(setf a (make-array '(44)
    :initial-contents '(117 300 128 333 127 330 127 330 134 351 84 201 101 252 87 210 140 369 117 300 65 144 112 285 132 345 65 144 126 327 68 153 112 285 116 297 114 291 125 324 116 297 142 375)))

(defun check1(flag)
    (setq i 0)
    (setq j 0)
    
    (loop
        (if (/= (aref a j) (+ 17 (char-code (char flag i))))
            (return-from check1 nil)
            (list (setq j (+ j 2)) (setq i (+ i 1))))
            
        (if (>= j 44)
            (return)
        )
    )
    
    (return-from check1 T)
)

(defun check2(flag)
    (setq i 0)
    (setq j 1)
    
    (loop
        (if (/= (aref a j) (* 3 (char-code (char flag i))))
            (return-from check2 nil)
            (list (setq j (+ j 2)) (setq i (+ i 1))))
        
        (if (>= j 44)
            (return)
        )
    )
    
    (return-from check2 T)
)

(defun check3(flag)
    (= 22 (length flag))
)

(princ "Enter the flag >> ")
(setq s (read-line))
(write-line "")

(if (check3 s)
    (if (check2 s)
        (if (check1 s)
            (write-line "Flag is correct!")
            (write-line "Wrong!")
        )
        (write-line "Wrong!")
    )
    (write-line "Wrong!")
)
```

## Solution

This one is actually pretty easy. The only difficulty of the task is that it is written in Common Lisp. This programming language has a fancy syntax so it could be hard to read it. But once you get used to it, it is really easy task.

So we have an array `a` with some numbers in it. We input string `s`. After that we put it through 3 check functions to check if the string is a flag. Well, `check3` is just checks the length of the input, we know it should be `22`. Alright.

Now, `check2` and `check1` look pretty similar. And they are! We can notice, that both functions checks if ASCII code of `i-th` input character satisfies the equation. But `check2` goes over odd indices of `a` and `check1` over even indices.

So actually we have only one variable to determine and two equations. But do we really need both? No, we don't! We can use any of these functions to calculate back our flag. Let's use `check1`.

`check1` checks if `ord(s[i]) + 17 = a[j]; i = range(0, len(s), 1), j = range(0, len(a), 2)`. So the flag is:

```Python
>>> a = [117, 300, 128, 333, 127, 330, 127, 330, 134, 351, 84, 201, 101, 252, 87, 210, 140, 369, 117, 300, 65, 144, 112, 285, 132, 345, 65, 144, 126, 327, 68, 153, 112, 285, 116, 297, 114, 291, 125, 324, 116, 297, 142, 375]
>>> "".join(chr(a[i] - 17) for i in range(0, len(a), 2))
'donnuCTF{d0_s0m3_calc}'
```