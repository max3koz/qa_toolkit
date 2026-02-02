import re

def is_palindrome(text: str) -> bool:
    checked_text = re.sub(r"[^a-zA-Z0-9а-яА-ЯіїєІЇЄ]", "", text).lower()
    return checked_text == checked_text[::-1]

def count_vowels(text: str) -> int:
    vowels_count = 0
    vowel_string = "aeiouy"
    for letter in text.lower():
        if letter in vowel_string:
            vowels_count += 1
    return vowels_count

def count_each_vowels(text: str) -> dict:
    vowels_dict = {}
    vowel_string = "aeiouy"
    for letter in text.lower():
        if letter in vowel_string:
            vowels_dict[letter] = vowels_dict.get(letter, 0) + 1
    return vowels_dict

def find_max(num_list: list) -> int|None:
    if len(num_list) > 0:
        max_num = num_list[0]
        for num in num_list[1:]:
            if max_num < num:
                max_num = num
        return max_num
    else:
        return None
