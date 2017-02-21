package com.baas.lab.code.war.kata;

public class MorseCodeDecoder {
	
	public static final String WHITE_SPACE = " ";

	public static String decode2(final String morseCode) {

		final char[] morseCodeArray = morseCode.toCharArray();
		final StringBuilder phrase = new StringBuilder();
		final StringBuilder code = new StringBuilder();
		char prevMorseCode = '\u0000';

		for (int i = 0; i < morseCodeArray.length; i++) {

			if (morseCodeArray[i] == 32) {

				if (!code.toString().trim().isEmpty()) {
					phrase.append(MorseCode.get(code.toString().trim()));
				} else {
					phrase.append(WHITE_SPACE);
				}

				code.setLength(0);
			}

			code.append(morseCodeArray[i]);
			prevMorseCode = morseCodeArray[i];
		}

		return phrase.toString();
	}
	
	public static String decode(final String morseCode) {

		final StringBuilder phrase = new StringBuilder();
		final String[] morseCodeParts = morseCode.split(WHITE_SPACE);
		boolean ignoreSpace = false;

		for (String code : morseCodeParts) {
			code = code.trim();
			if (!code.isEmpty()) {
				final String rCode = MorseCode.get(code);
				if (rCode != null) {
					phrase.append(rCode);
				}
				ignoreSpace = false;
			} else {
				if (!ignoreSpace) {
					phrase.append(WHITE_SPACE);
					ignoreSpace = true;
				}
			}
		}

		return phrase.toString().trim();
	}

}
