import regex
import logging
from .tokenizer import Tokens, Tokenizer

logger = logging.getLogger(__name__)


class MecabTokenizer(Tokenizer):
    ALPHA_NUM = r'[\p{L}\p{N}\p{M}]+'
    NON_WS = r'[^\p{Z}\p{C}]'

    def __init__(self, **kwargs):
        """
        Args:
            annotators: None or empty set (only tokenizes).
        """
        self._regexp = regex.compile(
            '(%s)|(%s)' % (self.ALPHA_NUM, self.NON_WS),
            flags=regex.IGNORECASE + regex.UNICODE + regex.MULTILINE
        )
        if len(kwargs.get('annotators', {})) > 0:
            logger.warning('%s only tokenizes! Skipping annotators: %s' %
                           (type(self).__name__, kwargs.get('annotators')))
        self.annotators = set()

        from konlpy.tag import Mecab
        self.word_tokenizer = Mecab()

        #

    def tokenize(self, text):
        def is_whitespace(c):
            if c == " " or c == "\t" or c == "\r" or c == "\n" or ord(c) == 0x202F:
                return True
            return False

        tokens = self.word_tokenizer.morphs(text)

        data = []
        start_ws = 0
        for i in range(len(tokens)):
            # Get text
            token = tokens[i]

            end_ws = start_ws + len(token)

            span = (start_ws, end_ws)

            # # Add whitespace
            if i + 1 < len(tokens):
                # check next
                if is_whitespace(text[end_ws]):
                    end_ws = end_ws + 1

            # Format data
            data.append((
                token,
                text[start_ws: end_ws],
                span,
            ))

            # move starting point
            start_ws = end_ws

        return Tokens(data, self.annotators)
