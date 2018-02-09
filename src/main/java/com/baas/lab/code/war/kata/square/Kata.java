package com.baas.lab.code.war.kata.square;

public class Kata {

	public static int[] squareOrSquareRoot(final int[] array) {

		if (array != null && array.length > 0) {
			for (int i = 0; i < array.length; i++) {
				int square = array[i] * array[i];
				double sqrt = Math.sqrt(Double.valueOf(array[i]));
				if (sqrt == array[i]) {
					array[i] = square;
				} else {
					array[i] = (int) sqrt;
				}
			}
		}

		return array;
	}

}
