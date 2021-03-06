# coding=UTF-8

import unittest
import string
from StringIO import StringIO
from detector.language import Language
class TestLanguage(unittest.TestCase):
  def setUp(self):
    self.language_data = u"abcdefghijklmnopqrstuvwxyz.ABCDEFGHIJKLMNOPQRSTUVWXYZ.\u00A0.!~@#$\%^&*()_\+'?[]“”‘’—<>»«›‹–„/.ßäåæèéëïòóöøüąćęłńśźż."

    self.special_chars = set(list(self.language_data.split(".")[-2].strip()))
    self.alphabet = set(list(string.ascii_lowercase))

    self.language_io = StringIO(self.language_data)
    self.language = Language(self.language_io, 'English')

  def test_proper_keys(self):
    vectors = self.language.vectors

    self.assertEqual(set(vectors[0].keys()), self.alphabet) 
    self.assertEqual(set(vectors[1].keys()), self.alphabet)
    self.assertEqual(set(vectors[2].keys()), self.special_chars)

  def test_sums_to_1(self):
    for v in self.language.vectors:
      self.assertAlmostEqual(sum(v.values()), 1)

  def test_unique_set_of_characters(self):
    alphabet = self.alphabet.union(self.special_chars) 

    self.assertEqual(self.language.characters, alphabet)
