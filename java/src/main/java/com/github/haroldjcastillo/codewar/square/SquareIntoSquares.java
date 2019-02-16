/*
 * https://www.codewars.com/kata/54eb33e5bc1a25440d000891
 */
package com.github.haroldjcastillo.codewar.square;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author harold.castillo
 */
public class SquareIntoSquares {

    public static String solution(long number) {

        final double nsqrt = Math.pow(number, 2);
        double acu = 0;

        for (int i = 1; i < number && acu != nsqrt; i++) {

            long ci = number - (i + 1);
            long np = number - i;
            acu = 0;

            while (acu != nsqrt && ci > 0) {
                final List<Long> result = new ArrayList<>();
                result.add(np);
                acu = Math.pow(np, 2);
                for (long n = ci; n >= 1; n--) {
                    final double tmp = Math.pow(n, 2);
                    final double cv = tmp + acu;
                    if (cv <= nsqrt) {
                        acu = cv;
                        result.add(n);
                    }
                }
                if (acu == nsqrt) {
                    return toString(result);
                }
                ci = result.get(1) - 1;
            }
        }

        return null;
    }

    private static String toString(final List<Long> list) {
        final StringBuilder builder = new StringBuilder();
        final long[] array = list.stream().sorted().mapToLong(i -> i).toArray();
        
        for (long i : array) {
            builder.append(i).append(" ");
        }
        
        return builder.toString().trim();
    }

}
