import pymorphy2
import pprint
import morphy

class TestPyMorphy:
    def setUp(self):
        self.morph = pymorphy2.MorphAnalyzer()

    def test_pymorphy2(self):
        morph = self.morph

        rc = morph.parse('стали')
        pprint.pprint(rc)


class TestTokenizer:
    def setUp(self):
        self.tokens = morphy.tokenizer(morphy.SENT)
        # pprint.pprint(tokens)

    def test_make_normal(self):
        normal=morphy.normalize(self.tokens)
        assert normal[0]=="морфологический"
        print(" ".join(normal))

    def test_normalize_t(self):
        normal=morphy.normalize_t(self.tokens)
        assert normal[0][0]=="морфологический"


class TestKwExtractor:
    def setUp(self):
        self.kw=set()
        tokens = morphy.tokenizer(morphy.SENT)
        normal=morphy.normalize_t(tokens)
        morphy.keywords(normal, self.kw)


    def test_kw(self):
        pprint.pprint(self.kw)
