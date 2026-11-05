public class woe {

    static int f(int c, int e) {
        if (c==e) {return 1;}
        if (c<e || c==8) {
            return 0;
        }
        return f(c-1,e)+f(c-4,e)+f(c/2,e);
    }
    public static void main(String[] args) {
        System.out.println(f(30, 12)*f(12,4));
    }
}
