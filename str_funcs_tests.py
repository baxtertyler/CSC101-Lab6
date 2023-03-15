# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

import unittest
from str_funcs import *


class TestMap(unittest.TestCase):

    def test_vowel_extractor(self):
        self.assertEqual(vowel_extractor("one two three"), "oeoee")  # lowercase
        self.assertEqual(vowel_extractor("FOUR FIVE SIX"), "OUIEI")  # uppercase
        self.assertEqual(vowel_extractor("ta te ti to tu"), "aeiou")  # all vowel

    def test_str_capitalize(self):
        self.assertEqual(str_capitalize("hello my name is tYler"), "Hello My Name Is Tyler")
        self.assertEqual(str_capitalize("a a a a a a a a a"), "A A A A A A A A A")
        self.assertEqual(str_capitalize("this is a Test"), "This Is A Test")

    def test_str_rotate(self):
        self.assertEqual(str_rotate("abcde"), "nopqr")  # lowercase
        self.assertEqual(str_rotate("nopqr"), "abcde")  # l reverse
        self.assertEqual(str_rotate("ABCDE"), "NOPQR")  # uppercase
        self.assertEqual(str_rotate("NOPQR"), "ABCDE")  # u reverse
        self.assertEqual(str_rotate("NOPQR!?@%"), "ABCDE!?@%")  # special char

    def test_make_substring(self):
        self.assertEqual(make_substring("Test for substring function", 3, 10, 2), "tfrs")
        self.assertEqual(make_substring("Every third letter is printed", 0, 29, 3), "Ertrlt  ie")
        self.assertEqual(make_substring("0123456789", 0, 10, 2), "02468")

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("racecar"), True)  # odd num char
        self.assertEqual(is_palindrome("anna"), True)  # even num char
        self.assertEqual(is_palindrome("hello"), False)  # not a palindrome

    def test_count_characters(self):
        self.assertEqual(count_characters("count characters", "c"), 3)  # appears
        self.assertEqual(count_characters("count characters", "w"), -1)  # does not appear
        self.assertEqual(count_characters("tyler", "t"), 1)
