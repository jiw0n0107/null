# Java 코드 작성 순서도

Java 프로그램을 작성할 때의 일반적인 순서입니다.


```java
package oop;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
public class MyClass {
    // 클래스의 내용
}
public class MyClass {
    private int id;
    private String name;
}
public class MyClass {
    private int id;
    private String name;

    public MyClass(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
public class MyClass {
    private int id;
    private String name;

    public MyClass(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public void displayInfo() {
        System.out.println("ID: " + id + ", Name: " + name);
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static void main(String[] args) {
        MyClass obj = new MyClass(1, "Jiwon Shim");
        obj.displayInfo();
    }
}
