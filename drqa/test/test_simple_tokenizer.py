from unittest import TestCase

import os
import sys
# add parent path (drqa) to path
sys.path.insert(0, os.path.realpath(os.path.pardir))
# print(sys.path)

# import tokenizers
from tokenizers import SimpleTokenizer as tok


class TestSimpleTokenizer(TestCase):
    def test_tokenize(self):
        tokens = tok().tokenize('This is a sample sentence.')
        print(tokens.words())
        self.assertEqual(len(tokens), 6)
