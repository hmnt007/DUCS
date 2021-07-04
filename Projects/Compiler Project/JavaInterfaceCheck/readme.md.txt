			Java - Interfaces


Defination: An interface is a reference type in Java. It is similar to class. It is a collection of abstract methods.
 Abstract method: A method without body (no implementation) is known as abstract method.
		example: public abstract int myMethod(int n1, int n2);

Features:

 1. Along with abstract methods, an interface may also contain constants, default methods, static methods, and nested types. 
 2. Method bodies exist only for default methods and static methods.
 3. An interface can contain any number of methods.
 4. An interface is written in a file with a ".java" extension, with the name of the interface matching the name of the file.
 5. The byte code of an interface appears in a ".class" file.
 6. Interfaces appear in packages, and their corresponding bytecode file must be in a directory structure that matches the package name.
 7. We cannot instantiate an interface.
 8. An interface does not contain any constructors.

Declaring Interfaces:

The interface keyword is used to declare an interface. Here is a simple example to declare an interface −

* File name : NameOfInterface.java */
import java.lang.*;
// Any number of import statements

public interface NameOfInterface {
   // Any number of final, static fields
   // Any number of abstract method declarations\
}

Properties of Interface:
 1. An interface is implicitly abstract. We do not need to use the abstract keyword while declaring an interface.
 2. Each method in an interface is also implicitly abstract, so the abstract keyword is not needed.
 3. Methods in an interface are implicitly public.


Jave Interface Implemantation 

Syntax:
public interface NameOfInterface {
   // Any number of final, static fields
   // Any number of abstract method declarations\
}



Example
// Filename: Sports.java
public interface Sports {
   public void setHomeTeam(String name);
   public void setVisitingTeam(String name);
}

Page Link: https://www.tutorialspoint.com/java/java_interfaces.htm


Things to check:
 1. opening and closing braces to be balanced
 2. syntax appropiately written
Limitations:
 1. You can only use char, String, int and float values to declare any function

erros not handled:
 1. functions with parameters (, int a) will also be accepted.
 2. required import staements are handled or not
 3. 


https://beginnersbook.com/2014/01/abstract-method-with-examples-in-java/
