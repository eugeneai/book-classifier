import pymorphy2
from pymorphy2.tokenizers import simple_word_tokenize
from stop_words import get_stop_words


SENT="Морфологический анализ - это определение характеристик слова на основе того, как это слово пишется. При морфологическом анализе не используется информация о соседних словах."

tokenizer = simple_word_tokenize
morph = pymorphy2.MorphAnalyzer()

stop_words = get_stop_words('ru')

print(stop_words)

def normalize_token(token):
    p = morph.parse(token)[0]
    return (p.normal_form, p.tag)

def normalize(tokens):
    return [normalize_token(t)[0] for t in tokens]

def normalize_t(tokens):
    return [normalize_token(t) for t in tokens]

def is_stop_word(token):
    """Determines that token is a
    stop word.
    """

def get_kw(tokens):
    kw=[]

    state="aggr"

    for n,t in tokens:
        if state=="aggr":
            if "VERB" in t:
                state="tear"
            elif n in stop_words:
                state="tear"
        elif state=="tear":
            if ("VERB" in t) or (n in stop_words):
                state="tear"
            else:
                state="aggr"

        if state=="tear":
            if kw:
                yield kw
                kw=[]
        elif state=="aggr":
            kw.append(n)


def keywords(tokens, d):
    for kw in get_kw(tokens):
        d.add(tuple(kw))
