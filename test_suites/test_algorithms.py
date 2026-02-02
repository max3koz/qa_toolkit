import pytest
from assertpy import assert_that

from algorithms.algorithms import is_palindrome, count_vowels, count_each_vowels, find_max


@pytest.mark.skip
@pytest.mark.parametrize("test_text, expected_result",
                         [(" Hello, hello! ", False),
                          (" ALLa, alla! ", True),
                          ("", True),
                          (" ", True),
                          ("єЄ є і і Її І і є єє", True),
                          (" AL, alla! ", False),
                          ("Level", True),
                          ("A man, a plan, a canal: Panama", True),
                          ("2 34   3 2", True),
                          ("234532", False),
                          ])
def test_is_palindrome(test_text, expected_result):
    assert_that(is_palindrome(test_text)).is_equal_to(expected_result)


@pytest.mark.skip
@pytest.mark.parametrize("text, expected_result", [
    ("Automation", 6),
    ("fhtrndbr", 0),
    ("", 0),
    (" ", 0),
    ("Automation Automation", 12),
    ("Automation_Automation", 12)
])
def test_count_vowels(text, expected_result):
    assert_that(count_vowels(text)).is_equal_to(expected_result)


@pytest.mark.skip
@pytest.mark.parametrize("text, expected_result", [
    ("Automation", {'a': 2, 'i': 1, 'o': 2, 'u': 1}),
    ("fhtrndbr", {}),
    ("", {}),
    (" ", {}),
    ("Automation Automation", {'a': 4, 'i': 2, 'o': 4, 'u': 2}),
    ("Automation_Automation", {'a': 4, 'i': 2, 'o': 4, 'u': 2})
])
def test_count_each_vowels(text, expected_result):
    assert_that(count_each_vowels(text)).is_equal_to(expected_result)

@pytest.mark.parametrize("test_num_list, expected_result",[
    ([-10, -3, -50], -3),
    ([1, 5, 3], 5),
    ([], None),
    ([1], 1),
    ([-10, -3, -50, -10, -3, -50], -3),
])
def test_max_number(test_num_list, expected_result):
    assert_that(find_max(test_num_list)).is_equal_to(expected_result)
