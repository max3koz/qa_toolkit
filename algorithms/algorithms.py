import re


def is_palindrome(text: str) -> bool:
    """Checks if the text is a palindrome"""
    checked_text = re.sub(r"[^a-zA-Z0-9а-яА-ЯіїєІЇЄ]", "", text).lower()
    return checked_text == checked_text[::-1]


def count_vowels(text: str) -> int:
    """Counts the number of each vowel in the text"""
    vowels_count = 0
    vowel_string = "aeiouy"
    for letter in text.lower():
        if letter in vowel_string:
            vowels_count += 1
    return vowels_count


def count_each_vowels(text: str) -> dict:
    """Counts the number of each vowel in the text"""
    vowels_dict = {}
    vowel_string = "aeiouy"
    for letter in text.lower():
        if letter in vowel_string:
            vowels_dict[letter] = vowels_dict.get(letter, 0) + 1
    return vowels_dict


def find_max(num_list: list) -> int | None:
    """Finds the largest number in the number list"""
    if len(num_list) > 0:
        max_num = num_list[0]
        for num in num_list:
            if max_num < num:
                max_num = num
        return max_num
    else:
        return None


def find_min(num_list: list) -> int | None:
    """Finds the smallest number in the number list"""
    if not num_list:
        return None

    min_num = num_list[0]
    for num in num_list:
        if min_num > num:
            min_num = num
    return min_num


def revers_list(num_list: list) -> list | ValueError:
    """Revers number in the number list"""
    if not num_list:
        raise ValueError("The number list is empty!")

    temp_list = num_list[:]
    new_list: list = []
    for _ in range(len(num_list)):
        update_num = temp_list.pop()
        new_list.append(update_num)
    return new_list


def numbers_sum(num_list: list) -> int | float:
    """Sum the numbers in the number list"""
    if not num_list:
        return 0

    num_sum: int | float = 0
    for num in num_list:
        num_sum += num
    return num_sum


def count_even(num_list: list) -> int:
    """Counts the even number in the number list"""
    if not num_list:
        return 0

    count = 0
    for num in num_list:
        if isinstance(num, int) and num % 2 == 0:
            count += 1
    return count
