package com.github.haroldjcastillo.codewar.perimeter;

import java.math.BigInteger;

public class SumFct {

	public static BigInteger perimeter(BigInteger n) {
		BigInteger t1 = BigInteger.valueOf(0);
		BigInteger t2 = BigInteger.valueOf(1);
		BigInteger s = BigInteger.valueOf(1);

		for (int i = 0; i < n.intValue(); i++) {
			final BigInteger temp = t1.add(t2);
			t1 = t2;
			t2 = temp;
			s = s.add(t2);
		}
		return s.multiply(BigInteger.valueOf(4));
	}
}
