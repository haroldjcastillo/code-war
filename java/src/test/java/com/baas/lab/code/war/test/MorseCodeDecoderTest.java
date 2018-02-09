package com.baas.lab.code.war.test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

import org.junit.Test;

import com.baas.lab.code.war.kata.morse.MorseCodeDecoder;

public class MorseCodeDecoderTest {

    @Test
    public void testExampleFromDescription() {
      assertThat(MorseCodeDecoder.decode(".... . -.--   .--- ..- -.. ."), is("HEY JUDE"));
    }
    
    @Test
    public void testExampleFromDescription3() {
      assertThat(MorseCodeDecoder.decode("-- ..- -.--  -... ..- . -.  -.. .. .-  ... ..  --- .-.-."), is("MUY BUEN DIA SI O"));
    }

}
