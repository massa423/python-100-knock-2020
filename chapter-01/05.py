from typing import Sequence, List


def create_ngram(n: int, words: Sequence[str]):
    return list(zip(*[words[i:] for i in range(n)]))


word: str = 'I am an NLPer'
word_list: List[str] = ['I', 'am', 'an', 'NLPer']

print(create_ngram(2, word.split()))
print(create_ngram(2, word))
print(create_ngram(2, word_list))
