package com.baas.lab.code.war.kata;

public class MorseCodeDecoder {

    public static String decode(final String morseCode) {

        final char[] morseCodeArray = morseCode.toCharArray();
        String phrase = "";
        String code = "";
        char prevMorseCode = '\u0000';
        
        for (int i = 0; i < morseCodeArray.length; i++) {

            code += morseCodeArray[i];

            if (morseCodeArray[i] == 32) {
                phrase += MorseCode.get(code);

                code = "";
                if(prevMorseCode == 32) {
                    phrase += " ";
                }

            }
            
             prevMorseCode = morseCodeArray[i];
        }

        return phrase;
    }

}
