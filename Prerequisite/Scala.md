# Scala

| |Index|
|---|---|
|0|[Hello World](#hello)|
|1|[String](#string)|
|2|[Loop](#loop)|
|3|[Condition(Pattern Matching)](#condition)|
|4|[Array(ArrayBuffer, iterate, sort, foleLeft, filter, map, collect, slice, take, drop)](#array)|
|5|[Collection(Map, Set, List)](#collection)|
|6|[Case Class](#bean)|
|7|[Tuple](#tuple)|
|8|[IO](#io)|
|9|[Actor](#actor)|
|10|[continue, break](#break)|
|11|[Option, Some, None](#option)|
|12|[Exception(try, catch, finally)](#exception)|
|13|[Functional](#functional)|
|14|[Word Count(Map, Reduce)](#count)|

## 0 <a id='hello'></a>Hello World
main function
```
object HelloWorld {
    def main(args : Array[String]) : Unit = {
        val name = args(0)
        println("Hello World : " + name)
    }
}

object HelloWorld extends App {
    println("Hello World")
}
```

## 1 <a id='string'></a>String
### 1.1 interpolation
s-Strings, f-Strings
```
var str = "hello"
val i = 123
str += i.toString

# The s Interpolator
println(s"$str $i world")

# The f Interpolator: format
println(f"$str%s $i%4d world")
printf("%s %d word", str, i)
```

### 1.2 lower, upper, capitalize, empty
```
# is alphanumeric
println(str.matches("^[a-zA-Z0-9]+$"))

# lower, upper, capitalize
println(str.toLowerCase)
println(str.toUpperCase)
println(str.capitalize)

# is empty
println(str.isEmpty)
println("".equals(str))
println(str.length == 0)
println(str.nonEmpty)
println(!"".equals(str))
println(str.length > 0)
```

### 1.3 substring, startsWith
```
"hello".substring(1, 3)
"hello".startsWith("he")
```

### 1.4 indexOf
```
println("hello".indexOf("ll"))
```

### 1.5 split
```
val str = "abc def"
for (word <- str.split(" ")) println(word)
```

### 1.6 iterate chars
```
for (i <- 0 until str.length) println(str.charAt(i))

Array.range(0, str.length).foreach(i => println(str.charAt(i)))

for (c <- str) println(c)
```

### 1.7 date
date format
```
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
val currentDateTime: LocalDateTime = LocalDateTime.now()
val formatter: DateTimeFormatter = DateTimeFormatter.ofPattern("yyyyMMdd")
println(currentDateTime.format(formatter))
```

## 2 <a id='loop'></a>Loop

### 2.1 for
```
for (i <- 0 to 10 if i % 2 == 0) println(i)

# include
for (i <- 0 to 5) println(i * 2)

# exclude
for (i <- 0 until 6) println(i * 2)

Array.range(0, 10, 2).foreach(println)

for (i <- 'a' to 'z') println(i)
```

### 2.2 foreach
```
val list = Array(2, 4, 1, 3, 5)
# 1
list.foreach(println)
# 2
for (i <- list.indices) println(list(i))
```

## 3 <a id='condition'></a>Condition

### 3.1 if, else
```
val str = if (i % 2 == 0) 'even' else 'odd'
```

### 3.2 Pattern Matching
```
import scala.util.Random
val x: Int = Random.nextInt(10)
x match {
  case 0 => "zero"
  case 1 => "one"
  case _ => "other"
}
```

## 4 <a id='array'></a>Array

### 4.1 Array, ArrayBuffer
- Array: immutable
- ArrayBuffer: mutable, append & remove
```
import scala.collection.mutable.ArrayBuffer

val arr1 = Array(1, 2)
val arr2 = ArrayBuffer(1, 3)
arr2 += (4)
arr2.append(5)
arr2.appendAll(Array(7, 8))
arr2.insert(0, 0)
# remove one
arr2.remove(0)
val arr3 = arr1 ++ arr2
println(arr3.mkString(","))

# length
println(arr3.length())
# get the first one
println(arr3.head)
println(arr3(0))
println(arr3.apply(0))
# get the last one
println(arr3.last)

# is empty
println(arr3.isEmpty)
println(arr3.length > 0)
```

### 4.2 Iterate
```
for(v <- arr3) println(v)

for(i <- arr.indices) println(arr(i))

for (i <- 0 until arr.length) println(arr.apply(i))
```

### 4.3 Sort
sorted, sortWith
```
val arr = Array(2, 4, 1, 3, 5)

# sort
println(arr.sorted.mkString(","))

# reverse sort
println(arr.sorted.reverse.mkString(","))

# sortWith
println(arr.sortWith((v1 : Int, v2 : Int) => v2 < v1).mkString(","))
```

### 4.4 min, max, sum
```
val arr = Array(2, 4, 1, 3, 5)
println(arr.min + ", " + arr.max + ", " + arr.sum.toDouble / arr.length)
```

### 4.5 foldLeft
```
val arr = Array(2, 4, 1, 3, 5)
println(arr.foldLeft(0)((result, item) => result + (if (item % 2 != 0) item else 0)))
```

### 4.6 filter, map
```
val arr = Array(2, 4, 1, 3, 5)
arr.filter(_ < 3).map(_ * 3).foreach(println)
```

### 4.7 filter, map, collect
```
val arr = Array(2, 4, 1, 3, 5)
arr.collect({case item : Int if item < 3 => item * 3}).foreach(println)
```

### 4.8 slice, take, drop
sub-array
```
val arr = Array(2, 4, 1, 3, 5)
arr.slice(1, 3).foreach(println)
arr.take(3).foreach(println)
arr.drop(2).foreach(println)
```

## 5 <a id='collection'></a>Collections
### 5.1 Map
Immutable and mutable
```
import scala.collection.mutable.Map

var map1 = Map("a" -> 1, "b" -> 2)
map1 += ("c" -> 3)
map1.foreach(println)

val map2 = Map("d" -> 1)
val map3 = map1 ++ map2

map3.keys.foreach(key => println(s"$key " + map1(key)))

for ((k, v) <- map3) println(s"$k, $v")

map3.foreach{case(k, v) => println(s"$k, $v")}

arr = map3.toArray
```

### 5.2 Set, BitSet
```
import scala.collection.immutable.Set

val s = Set(1, 2, 3, 4)
println(s(1))

import scala.collection.immutable.BitSet 

val bs = BitSet(1, 2, 3, 4)
println(bs(2))
val bs1 = bs + 10 + 11 - 2
println(bs1(2))
```

### 5.3 List
LinkedList
```
import scala.collection.immutable.List

val list1 = 1 :: (2 :: (3 :: (4 :: Nil)))
var list2 = List(1, 2, 3, 4)
list = list :+ 5
val list3 = list1 ::: list2
val list4 = List.concat(list1, list2, list3)
list4.foreach(println)

println(list4.head)
println(list4.apply(0))
println(list4.tail)
```

## 6 <a id='bean'></a>Case Class
Java bean
```
# auto generated methods: getter, setter, hashcode, equals, toString
case class Dummy(val name : String, val age : Int)
```

### 6.1 Sort
```
val arr1 = Array(new Dummy("a", 1), new Dummy("b", 3), new Dummy("a", 2), new Dummy("b", 1))

# sortBy name
println(arr1.sortBy(_.name).mkString("-"))

# sortBy age
println(arr1.sortBy(_.age).mkString("-"))

# sortWith
println(arr1.sortWith((item1, item2) => if (item1.name.equals(item2.name)) item1.age < item2.age else item1.name.compareTo(item2.name) < 0).mkString("-"))
```

### 6.2 Case Class with Pattern Matching

## 7 <a id='tuple'></a>Tuple
```
def statistics(arr : Array[Int]) : (Int, Int, Double) = (arr.min, arr.max, arr.sum.toDouble / arr.length)
val arr = Array(2, 4, 1, 3, 5)
val s = statistics(arr)
println(s._1 + ", " + s._2 + ", " + s._3)
```

### 7.1 Sort
```
val arr = Array(("a", 1), ("b", 3), ("a", 2), ("b", 1))
println(arr.sortBy(_._1).mkString("-"))
println(arr.sortBy(_._2).mkString("-"))
println(arr.sortWith((item1, item2) => if (item1._1.equals(item2._1)) item1._2 < item2._2 else item1._1.compareTo(item2._1) < 0).mkString("-"))
```

## 8 <a id='io'></a>IO
read and write
```
import scala.io.Source
# read
Source.fromFile("test.log").getLines().foreach(println)

# write
var writer : PrintWriter = null
try {
    writer = new PrintWriter("test.log")
    writer.write("test")
    writer.flush()
} catch {case e : Exception => e.printStackTrace}
finally {try {if (writer != null) writer.close()} catch {case e : Exception => e.printStackTrace}}
```

## 9 <a id='actor'></a>Actor
multithread
```
import java.util.concurrent.{ExecutorService, Executors, TimeUnit}
import akka.actor.{Actor, ActorSystem, Props}
import akka.util.Timeout
import scala.concurrent.{Await, ExecutionContext}
import scala.concurrent.duration.Duration
import java.util.Random

class TestActor extends Actor {
    def receive = {
        case arg => {
            val random = new Random()
            val sleepTime = random.nextInt(10)
            Thread.sleep(sleepTime)
            val result = s"hello : $sleepTime " + arg
            println(result)
            result
        }
    }
}
val system = ActorSystem("ActorSystem")
val actor = system.actorOf(Props(new TestActor), "TestActor")

# sync
actor ! "world async"

# async
implicit val timeout = Timeout(5, TimeUnit.SECONDS)
import akka.pattern._
# 1
val feature = actor ? "world async with feature"
while (!feature.isCompleted) Thread.sleep(100)
if (feature.isCompleted) {println(feature.value.get.isSuccess + ", " + feature.value.get.get);}
# 2
println(Await.result(feature, Duration.create(1, TimeUnit.SECONDS)))
```

### 9.1 Schedule
```
val system = ActorSystem("ActorSystem")
import system.dispatcher
system.scheduler.schedule(Duration.create(1000, TimeUnit. MILLISECONDS), Duration.create(1000, TimeUnit. MILLISECONDS))(
    println("hello")
)
```

### 9.2 concurrent
```
val ec = ExecutionContext.fromExecutorService(Executors.newFixedThreadPool(100))
val system = ActorSystem("ActorSystem", None, None, Option(ec))
```

## 10 <a id='break'></a>continue, break
```
import scala.util.control.Breaks._

breakable {
  ...
  break
}
```

## 11 <a id='option'></a>Option, Some, None
replace Java null
```
def toInt(in: String): Option[Int] = {
    try {
        Some(Integer.parseInt(in.trim))
    } catch {
        case e: NumberFormatException => None
    }
}

val intOpt = toInt(someString)
intOpt match {
    case Some(i) => println(i)
    case None => println("That didn't work.")
}

print(if (intOpt == None) "That didn't work." else intOpt.get)
```

## 12 <a id='exception'></a>Exception
```
try {
    throw new Exception("hello")
} catch {
    case e: Exception => e.printStackTrace
    case e: ...
} finally {
    //clean up
}
```

## 13 <a id='functional'></a>Functional
### higher-order function, anonymous function
```
def wrapper(str : String, f : ((String) => String)): Unit = {
    println("wrapper start")
    println(f(str))
    println("wrapper end")
}
# 1
def say(str : String) : String = "hello " + str
wrapper("test", say)
# 2
wrapper("test", (str => "hello " + str))
```

### Tail Recursion
@tailrec, can be optimized by compiler.

## 14 <a id='count'></a>Word Count
### 14.1 Map
```
# flatMap
val arr = Array("1,2,3", "1,4,5")
arr.flatMap(_.split(",")).distinct.foreach(println)
```

### 14.2 Reduce
```
# groupBy, reduce
val map1 = Map("a" -> 1, "b" -> 2)
val map2 = Map("a" -> 1, "c" -> 3)
Array.concat(map1.toArray, map2.toArray).groupBy(_._1).map(item => (item._1, item._2.map(_._2).reduce(_ + _))).foreach(println)
```
