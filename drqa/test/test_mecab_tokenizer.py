from unittest import TestCase

import os
import sys
# add parent path (drqa) to path
sys.path.insert(0, os.path.realpath(os.path.pardir))
# print(sys.path)

# import tokenizers
from tokenizers import MecabTokenizer as tok


class TestMecabTokenizer(TestCase):
    def test_tokenize(self):
        tokens = tok().tokenize('이것은 샘플 문장입니다.')
        print(tokens.words())
        self.assertEqual(len(tokens), 6)

    def test_span(self):
        text = '이것은 샘플 문장입니다.'
        tokens = tok().tokenize(text)
        print(tokens.words())
        span = tokens.offsets()
        print(span)
        tokens_by_span = [text[s[0]:s[1]] for s in span]
        print(tokens_by_span)

        self.assertListEqual(tokens_by_span, tokens.words())

    def test_untokenize(self):
        text = '이것은 샘플 문장입니다.'
        untokenized = tok().tokenize(text).untokenize()
        print(text)
        print(untokenized)
        self.assertEqual(text, untokenized)