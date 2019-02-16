package com.github.haroldjcastillo.codewar.sum;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class SolutionTest {

	//@Test
	public void sum() {
		long start = System.nanoTime();
		int result = Kata.sum(new int[] { 6, 2, 1, 8, 5, 10 });
		System.out.println("Suma 1 " + (System.nanoTime() - start));
		assertEquals(21, result);
	}

	//@Test
	public void SumNullArray() {
		long start = System.nanoTime();
		int result = Kata.sum(null);
		System.out.println("SumNullArray " + (System.nanoTime() - start));
		assertEquals(21, result);
	}
	
	@Test
	public void SumEmptyArray () {
		long start = System.nanoTime();
		int result = Kata.sum(new int[] { -6 });
		System.out.println("SumNullArray " + (System.nanoTime() - start));
		assertEquals(21, result);
	}

	//@Test
	public void SumOnlyOneElement() {
		long start = System.nanoTime();
		int result = Kata.sum(new int[] {});
		System.out.println("SumOnlyOneElement " + (System.nanoTime() - start));
		assertEquals(0, result);
	}
}