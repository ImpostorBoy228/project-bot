import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class fack {
    static int can_break(int n) {
        List<Integer> factors = new ArrayList<>();
        for (int i=2;;i++) {
            var nn = true;
            while (nn) {
                if (n%i==0) {
                    String j = String.valueOf(i);
                    if (!(j.contains("1") || j.contains("3"))) {
                        return 0;
                    }
                    factors.add(i);
                    n/=i;
                    if (!(n%i==0)) {
                        nn=false;
                    }
                }
                if (factors.size() >= 2) {return 0;}
            }
            if (i>=n) {
                for (int o=2;o*o<factors.get(0);o++) {
                    if (factors.get(0)%o==0) {return 0;}
                }

                for (int o=2;o*o<factors.get(1);o++) {
                    if (factors.get(1)%o==0) {return 0;}
                }
                int max = Collections.max(factors);
                return max;
            }
        }
        
    }

    public static void main(String[] args) {
        for(int i=3000000;;i++) {
            int u = can_break(i);
            if (u!=0) {
                System.out.printf("%d %d %n",i, u);
            }
        }
    }
}
