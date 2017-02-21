package com.baas.lab.code.war.kata;

import java.util.HashMap;
import java.util.Map;

public final class MorseCode {

    public static final MorseCode morseCode = new MorseCode();

    private static Map<String, String> morseCodeMap;

    private MorseCode() {
    	morseCodeMap = new HashMap<>();
        morseCodeMap.put(".-", "A");
        morseCodeMap.put("-...", "B");
        morseCodeMap.put("-.-.", "C");
        morseCodeMap.put("-..", "D");
        morseCodeMap.put(".", "E");
        morseCodeMap.put("..-.", "F");
        morseCodeMap.put("--.", "G");
        morseCodeMap.put("....", "H");
        morseCodeMap.put("..", "I");
        morseCodeMap.put(".---", "J");
        morseCodeMap.put("-.-", "K");
        morseCodeMap.put(".-..", "L");
        morseCodeMap.put("--", "M");
        morseCodeMap.put("-.", "N");
        morseCodeMap.put("---", "O");
        morseCodeMap.put(".--.", "P");
        morseCodeMap.put("--.-", "Q");
        morseCodeMap.put(".-.", "R");
        morseCodeMap.put("...", "S");
        morseCodeMap.put("-", "T");
        morseCodeMap.put("..-", "U");
        morseCodeMap.put("...-", "V");
        morseCodeMap.put(".--", "W");
        morseCodeMap.put("-..-", "X");
        morseCodeMap.put("-.--", "Y");
        morseCodeMap.put("--..", "Z");
    }

    public static String get(final String code) {
        return morseCodeMap.get(code);
    }
}
