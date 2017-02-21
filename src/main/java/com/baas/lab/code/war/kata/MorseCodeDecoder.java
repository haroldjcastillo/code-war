package com.baas.lab.code.war.kata;

public class MorseCodeDecoder {

	public static final String WHITE_SPACE = " ";

	public static String decode(final String morseCode) {
		final char[] morseCodeArray = morseCode.toCharArray();
		final StringBuilder phrase = new StringBuilder();
		final StringBuilder word = new StringBuilder();

		char prevMorseCode = '\u0000';
		int indexOf = morseCodeArray.length - 1;

		for (int i = 0; i < morseCodeArray.length; i++) {

			if (morseCodeArray[i] == 32 || i == indexOf) {

				if (prevMorseCode == 32 && i != indexOf) {
					phrase.append(" ");
					prevMorseCode = '\u0000';
				} else {
					phrase.append(MorseCode.get(word.toString()));
					word.setLength(0);
				}

			} else {
				word.append(morseCodeArray[i]);
			}

			prevMorseCode = morseCodeArray[i];
		}

		return phrase.toString();
	}

	public static String decode3(final String morseCode) {

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
