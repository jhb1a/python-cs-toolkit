class RomanNumerals:
    """
    Converts between integers and Roman numerals.

    Supports the standard Roman numeral range (1-3999) using symbols
    I, V, X, L, C, D, M with subtractive notation for 4, 9, 40, 90, 400, 900.

    Examples:
        >>> RomanNumerals.int_to_roman(1993)
        'MCMXCIII'

        >>> RomanNumerals.roman_to_int('XLII')
        42
    """

    # Value to symbol mappings in descending order
    # Includes subtractive pairs (CM, CD, XC, XL, IX, IV)
    MAPPINGS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    @staticmethod
    def int_to_roman(num: int) -> str:
        """
        Convert an integer to a Roman numeral string.

        Args:
            num: Integer between 1 and 3999 (inclusive)


        Returns:
            Roman numeral representation as a string

        Raises:
            TypeError: If num is not an integer
            ValueError: If num is outside the valid range (1-3999)

        Complexity:
            Time: O(1) - Fixed number of iterations (at most 13)
            Space: O(1) - Result string length bounded by constant (at most 15)

        Examples:
            >>> RomanNumerals.int_to_roman(49)
            'XLIX'
            >>> RomanNumerals.int_to_roman(3999)
            'MMMCMXCIX'
        """
        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        if num <= 0 or num >= 4000:
            raise ValueError("Number must be between 1 and 3999")

        result = ""
        for value, numeral in RomanNumerals.MAPPINGS:
            count = num // value
            result += numeral * count
            num -= value * count

        return result

    @staticmethod
    def roman_to_int(roman: str) -> int:
        """
        Convert a Roman numeral string to an integer.

        Args:
            roman: Roman numeral string (case-insensitive)

        Returns:
            Integer value of the Roman numeral

        Raises:
            TypeError: If roman is not a string

        Complexity:
            Time: O(n) - Where n is the length of the input string
            Space: O(1) - Only uses constant extra space

        Examples:
            >>> RomanNumerals.roman_to_int('MCMXCIV')
            1994
            >>> RomanNumerals.roman_to_int('xlix')
            49
        """
        if not isinstance(roman, str):
            raise TypeError("Input must be a string")

        result = 0
        i = 0
        roman = roman.upper()

        valid_chars = {"M", "D", "C", "L", "X", "V", "I"}
        for char in roman:
            if char not in valid_chars:
                raise ValueError(f"Invalid character '{char}' in Roman numeral")

        for value, numeral in RomanNumerals.MAPPINGS:
            while roman[i : i + len(numeral)] == numeral:
                result += value
                i += len(numeral)
                if i >= len(roman):
                    break

        return result
