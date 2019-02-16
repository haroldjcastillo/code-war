package com.github.haroldjcastillo.codewar.test.morse;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

import org.junit.Test;

import com.github.haroldjcastillo.codewar.morse.MorseCodeDecoder;

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
