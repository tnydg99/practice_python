def romanToInt(s: str) -> int:
        roman_numerals = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        roman_total = 0
        previous_char = '-'
        for char in s:
            if previous_char + char in roman_numerals.keys():
                roman_total += roman_numerals[previous_char + char]
                roman_total -= roman_numerals[previous_char]
            else:
                roman_total += roman_numerals[char]
            previous_char = char
        return roman_total

if __name__ == "__main__":
    print(romanToInt('CXV'))