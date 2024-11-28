---
author: Mindusting
corrected: false
tags:
  - Programming/Java/Class
title: Clases en Java
---

# CLASES Y OBJETOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## PROPIEDAD STATIC

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## CONSTRUCTORES

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## FINALIZA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

```java
public class Complex {

    private double real      = 0;
    private double imaginary = 0;

    public Complex(Complex complex) {
        this.real      = complejo.getReal();
        this.imaginary = complejo.getImaginary();
    }

    public Complex(double r, double i) {
        this.real      = r;
        this.imaginary = i;
    }

    public double getReal() {
        return this.real;
    }

    public double getImaginary() {
        return this.imaginary;
    }

    public void finalize() {
        System.out.println("A complex has been destroyed.");
    }

    public static void main(String[] args) {

        Complex complex = new Complex(3, 2);
    }
}
```
