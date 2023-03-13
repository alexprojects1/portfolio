# Groovy Language

## Objective:
+ Work with Jenkins and Groovy
+ Datatypes "def" or explicit data types
+ Control structures

Further Testing
```
def x = 5

x += 5

println x
assert x == 10

# define x = 5 and add 5 which will result in 10 

```

```
def x = 5

x += 5

println x
assert x == 10: "value wasn't 11"

#added message at the end
```


```
String name = " Alex working on groovy"
int courseCount = 14
float salary = 99999999.99999
Boolean isProgrammer = true

println name + " has created"  + courseCount + " courses."
println name + " is a programmer?" + isProgrammer.toString().capitalize()
println name + " wishes his salary was" + salary



###OUTPUT
Alex working on groovy has created14 courses.
 Alex working on groovy is a programmer?True
 Alex working on groovy wishes his salary was1.0E8

String name = " Alex working on groovy"
int courseCount = 14
float salary = 99999999.99999
Boolean isProgrammer = true

println name + " has created"  + courseCount + " courses."
println name + " is a programmer?" + isProgrammer.toString().capitalize()
println name + " wishes his salary was \$" + String.format("%.2f", salary)

###OUTPUT (rounded up
Alex working on groovy has created14 courses.
 Alex working on groovy is a programmer?True
 Alex working on groovy wishes his salary was $100000000.00


String name = " Alex working on groovy"
int courseCount = 14
float salary = 99999999.99999
Boolean isProgrammer = true

println name + " has created"  + courseCount + " courses."
println name + " is a programmer?" + isProgrammer.toString().capitalize()
println name + " wishes his salary was \$" + salary

###OUTPUT
Alex working on groovy has created14 courses.
 Alex working on groovy is a programmer?True
 Alex working on groovy wishes his salary was $1.0E8


```


```
# Control structures
# If/Else, For loop, For-in loop, Each loops


int courseCount = 14;
Boolean isProgrammer = true;
String[] singers = [ "Alex", "Chin", "Jeff", "Ed"]

if (isProgrammer) {
    println "He's a programmer, alright"
}
else{
    println "Not a programmer, though"
}


###OUTPUT
He's a programmer, alright

```


```
int courseCount = 14;
Boolean isProgrammer = true;
String[] singers = [ "Alex", "Chin", "Jeff", "Ed"]

/*if (isProgrammer) {
    println "He's a programmer, alright"
}
else{
    println "Not a programmer, though"
}*/

for (int i = 0;i < courseCount; i++){
    println "chris made course  " + (i+1) + "!!!"
}

###OUTPUT
chris made course  1!!!
chris made course  2!!!
chris made course  3!!!
chris made course  4!!!
chris made course  5!!!
chris made course  6!!!
chris made course  7!!!
chris made course  8!!!
chris made course  9!!!
chris made course  10!!!
chris made course  11!!!
chris made course  12!!!
chris made course  13!!!
chris made course  14!!!


Alex
Chin
Jeff
Ed



```

```
int courseCount = 14;
Boolean isProgrammer = true;
String[] singers = [ "Alex", "Chin", "Jeff", "Ed"]

/*if (isProgrammer) {
    println "He's a programmer, alright"
}
else{
    println "Not a programmer, though"
}*/

//for (int i = 0;i < courseCount; i++){
    println "chris made course  " + (i+1) + "!!!"
//}

for(String singer: singers) {
    println singer
}

```

```
int courseCount = 14;
Boolean isProgrammer = true;
String[] singers = ["Alex", "Chin", "Jeff", "Ed"]

*if (isProgrammer) {
    println "He's a programmer, alright"
}
else{
    println "Not a programmer, though"
}

for (int i = 0;i < courseCount; i++){
    println "chris made course  " + (i+1) + "!!!"
}

for(String singer: singers) {
   println singer
}

singers.each{x -> println{x}}
singers.each{println(it)}

```


## Subroutines
```
Functions - return value (void return type)

Methods - do not return a value.  a fucntion to create crednetiasl from a name

# create our username function
# properly asser that the value returned is correct
# create a simple output function


String getUserName(String firstName, String lastName) {
    return firstName.substring(0,1).toLowerCase() + lastName.toLowerCase();
}

assert getUserName("Chris", "Behrens") == "cbehrens" : "getUserName isn't working"

print(getUserName("Chris","Behrens"))
 
cbehrens


### OUTPUT

cbehrens
```


