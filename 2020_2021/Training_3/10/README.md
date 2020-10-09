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