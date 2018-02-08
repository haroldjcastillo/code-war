package com.baas.lab.code.war.test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

import org.junit.Test;

import com.baas.lab.code.war.kata.morse.MorseCodeDecoder;

public class MorseCodeDecoderTest {

    @Test
    public void testExampleFromDescription() {
      assertThat(MorseCodeDecoder.decode2(".... . -.--   .--- ..- -.. ."), is("HEY JUDE"));
    }
}
