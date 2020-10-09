# 11

## Task

```Kotlin
/**
 * You can edit, run, and share this code. 
 * play.kotlinlang.org 
 */
import java.security.MessageDigest
import kotlinx.coroutines.*

interface OnCheckCompleteListener {
    fun onCheckComplete(result: Boolean)
}

class Part1Checker(private val part: String) {
    
    private var completeListener: OnCheckCompleteListener? = null
    
    fun setOnCheckCompleteListener(listener: OnCheckCompleteListener) {
        this.completeListener = listener
    }
    
    fun doCheck() {
       	val result = this.part.reversed() == "}{FTCunnod"
        this.completeListener?.onCheckComplete(result)
    }
}

class Part2Checker(private val part: String) {
    
    private var completeListener: OnCheckCompleteListener? = null
    
    fun setOnCheckCompleteListener(listener: OnCheckCompleteListener) {
        this.completeListener = listener
    }
    
    fun doCheck() {
        val l = this.part.split('_').map { it -> it.toInt() }
        
        if (l.size != 3) {
            this.completeListener?.onCheckComplete(false)
            return
        }
        
        val a0 = l[0]
        val a1 = l[1]
        val a2 = l[2]
        
        var result = true
       	result = result and (107 * a0 - a1 + 15 * a2 == 89177)
        result = result and (a1 - a0 == 63423 + a2)
        result = result and (a2 - a0 == a1 - 66097)
        
        this.completeListener?.onCheckComplete(result)
    }
}

class Part3Checker(private val part: String) {
    
    private var completeListener: OnCheckCompleteListener? = null
    
    fun setOnCheckCompleteListener(listener: OnCheckCompleteListener) {
        this.completeListener = listener
    }
    
    fun doCheck() {
        
        val digest = MessageDigest.getInstance("SHA-256").digest(this.part.toByteArray()).joinToString(separator="") { String.format("%02x", it) }
        val check = "a941a4c4fd0c01cddef61b8be963bf4c1e2b0811c037ce3f1835fddf6ef6c223"
        this.completeListener?.onCheckComplete(digest == check)
    }
}

fun main() {
    
    val flag = "***REDACTED***"
    val part1 = flag.substring(0..8) + flag.last()
    val part2 = flag.substring(9..22)
    val part3 = flag.substring(24..31)
    
    GlobalScope.launch {
        val part1Checker = Part1Checker(part1)
    	part1Checker.setOnCheckCompleteListener(object: OnCheckCompleteListener {
        	override fun onCheckComplete(result: Boolean) {
                if (result) {
                    println("Part 1 check is true")
                } else {
                    println("Part 1 check is false")
                }
        	}
    	})
        part1Checker.doCheck()
    }
    
    GlobalScope.launch {
        val part2Checker = Part2Checker(part2)
    	part2Checker.setOnCheckCompleteListener(object: OnCheckCompleteListener {
        	override fun onCheckComplete(result: Boolean) {
                if (result) {
                    println("Part 2 check is true")
                } else {
                    println("Part 2 check is false")
                }
        	}
    	})
        part2Checker.doCheck()
    }
    
    GlobalScope.launch {
        val part3Checker = Part3Checker(part3)
    	part3Checker.setOnCheckCompleteListener(object: OnCheckCompleteListener {
        	override fun onCheckComplete(result: Boolean) {
                if (result) {
                    println("Part 3 check is true")
                } else {
                    println("Part 3 check is false")
                }
        	}
    	})
        part3Checker.doCheck()
    }
}
```

## Solution