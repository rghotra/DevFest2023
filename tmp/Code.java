
package tmp;
class Code {
public static void main(String[] args) {


class Test {
    int a;
    int b;
    
    Test (int a, int b) {
        this.a = a;
        this.b = b;
    }
    
    void swap() {
        this.a = this.a + this.b;
        this.b = this.a - this.b;
        this.a = this.a - this.b;
    }
}

Test p = new Test(4, 7);
System.out.println("a: " + p.a +", b: " + p.b);
p.swap();
System.out.println("a: " + p.a +", b: " + p.b);
}
}
