package com.baas.lab.code.war.kata.sum;

import java.util.Arrays;

public class Kata {

	public static int sum3(final int[] numbers) {

		int result = 0;
		
		if (numbers != null && numbers.length > 0) {
			Arrays.sort(numbers);
			for (int j = 1; j < numbers.length - 1; j++) {
				result += numbers[j];
			}
		}

		return result;
	}
	
	public static int sum(final int[] numbers) {

		int result = 0, max = 0, min = 0;

		if (numbers != null && numbers.length > 1) {
			max = numbers[0];
			min = numbers[0];

			for (int j = 0; j < numbers.length; j++) {

				if (numbers[j] <= min) {
					min = numbers[j];
				} else if (numbers[j] >= max) {
					max = numbers[j];
				}

				result += numbers[j];
			}
		}

		return result - min - max;
	}

	public static int sum2(final int[] numbers) {

		int result = 0, max = numbers[0], min = numbers[0];

		for (int j = 0; j < numbers.length; j++) {
			min = Math.min(min, numbers[j]);
			max = Math.max(max, numbers[j]);
			result += numbers[j];
		}

		return result - min - max;
	}

}
