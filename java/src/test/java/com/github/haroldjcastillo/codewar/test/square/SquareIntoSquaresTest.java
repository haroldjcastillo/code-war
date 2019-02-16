package com.github.haroldjcastillo.codewar.test.square;

import com.github.haroldjcastillo.codewar.square.SquareIntoSquares;
import org.junit.Assert;
import org.junit.Test;

/**
 *
 * @author harold.castillo
 */
public class SquareIntoSquaresTest {
    
    @Test
    public void test11() {
        Assert.assertEquals("1 2 4 10", SquareIntoSquares.solution(11));
    }
    
    @Test
    public void test50() {
        Assert.assertEquals("1 3 5 8 49", SquareIntoSquares.solution(50));
    }
    
    @Test
    public void test12() {
        Assert.assertEquals("1 2 3 7 9", SquareIntoSquares.solution(12));
    }
    
    @Test
    public void test4() {
        Assert.assertNull(SquareIntoSquares.solution(4));
    }
    
    @Test
    public void test21() {
        System.out.println(SquareIntoSquares.solution(21));
    }
}
