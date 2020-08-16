from typing import List, Dict

word: str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New NAtions Might Also Sign Peace Security Clause. Arthur King Can.'

word_list: List[str] = word.split()
target_index: List[int] = [1, 5, 6, 7, 8, 9, 15, 16, 19]
res: Dict = {}

for i, w in enumerate(word_list):
    if i + 1 in target_index:
        res[w[:1]] = i + 1
    else:
        res[w[:2]] = i + 1

print(res)
