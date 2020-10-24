#include <stdio.h>

void d() {
    printf("I am function d, I have number 1");
}

void o() {
    printf("I am function o, I have numbers 2 and 16");
}

void n() {
    printf("I am function n, I have numbers 3, 4, 12 and 17");
}

void u() {
    printf("I am function u, I have numbers 5 and 11");
}

void C() {
    printf("I am function C, I have number 6");
}

void T() {
    printf("I am function T, I have number 7");
}

void F() {
    printf("I am function F, I have number 8");
}

void op() {
    printf("I am function {, I have number 9");
}

void f() {
    printf("I am function f, I have numbers 10 and 19");
}

void c() {
    printf("I am function c, I have number 13");
}

void t() {
    printf("I am function t, I have number 14");
}

void i() { 
    printf("I am function i, I have number 15");
}

void un() {
    printf("I am function _, I have number 18");
}

void l() {
    printf("I am function l, I have number 20");
}

void a() {
    printf("I am function a, I have number 21");
}

void g() {
    printf("I am function g, I have number 22");
}

void cp() {
    printf("I am function }, I have number 23");
}
// donnuCTF{function_flag} 

int main(int argc, char const * argv[]) {

    printf("No flags here\n");

    if (0) {
        d();
        o();
        n();
        u();
        C();
        T();
        F();
        op();
        f();
        c();
        t();
        i();
        un();
        l();
        a();
        g();
        cp();
    }
}