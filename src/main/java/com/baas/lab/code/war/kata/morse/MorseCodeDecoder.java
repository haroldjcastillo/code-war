package com.baas.lab.code.war.kata.morse;

public class MorseCodeDecoder {

	public static final String WHITE_SPACE = " ";

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
