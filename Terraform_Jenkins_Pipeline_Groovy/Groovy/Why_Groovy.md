# Groovy Language

## Notes from: https://www.eficode.com/blog/jenkins-groovy-tutorial

## Objective:

+ Groovy is Java without types, so without defining the basic data types like int, float, String, etc. Basically it’s the same as Java: defining variable without specifying a type. Groovy will judge the type based on the value of the object.

```
def str = "Hello world"
def num =0
```

+ In Groovy, the ‘for’ loop becomes more concise and easier to read. Groovy loop statements support: while, for, for-in, break, continue, and the whole is consistent with Java.

For example:

0..5 indicates that the integers 0,1,2,3,4,5 are included

0..<5 means 0,1,2,3,5 and a..d means a,b,c,d:

```
for(x in 1..5){
  println x //0,1,2,3,4,5
}
```

+ Groovy also supports default parameter values:

```
def repeat(val, x=10){
  for(i in 0..<x){
    println val
  }
}
```

+ In Groovy, we can use scopes to define Collections or Arrays.

```
def arg = ["Groovy","Java","Python",”nodeJS”]
println arg.class
```


+ The search method in Groovy is also more flexible
```
println arg[1]
```


+ Groovy also allows you to add or remove collections from collections.
```
def no = [1,2,3,4]
def no2 = no +5 //=[1,2,3,4,5]
def no3 = no - [2,3] //=[1,4]
```

+ When adding elements to a collection, we can use the following methods

```
arg.add("Ruby")
arg << "Smalltalk"
arg[5] = "C++"
```


+ A further benefit to Groovy is its Operators:

Groovy arithmetic operators, logical operators, relational operators and bitwise operators are all consistent with languages like nodeJS. Groovy’s == is equivalent to the equals methods in Java .

```
String str1 = "123";
String str2 = new String("123");
if(str1 == str2){
  println(“equal")；
}else{
  println("Not equal")；
}
```

+ . List methods available in Groovy are another benefit.

Add( ) Append the new value to the end of this list.

Get( ) Returns the element at the specified position in this list.

Contains( ) Returns true if this list contains the specified value.

Minus( ) Create a new list of original elements that removes the specified element

Plus ( ) Create a new list of the original list elements and the specified elements.

Pop( ) Remove the last item from this list

Remove( ) Remove elements from the specified position in the list

Reverse() Create a new list that is the opposite of the original list's elements

Size( ) Get the number of elements in this list.

Sort( ) Returns a sorted copy of the original list.

```
def list = [];
list = [1, 2, 3, 4];
list.add(5); //add
list.pop(); //pop
```

+ In any other object-oriented language, there are concepts of objects and classes to represent the object-oriented nature of a programming language. Groovy implicitly creates getters, setter methods, and provides constructors with arguments.

```
class Person {
  String name;
  int ID;
}
class Test {
  static void main(String) {
    def emp = new emp(name: 'name’')
    println emp.getName();
    emp.setYR(2019);
    println emp.getYR(); // 2019
  }
}
```