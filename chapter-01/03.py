import re

word: str = 'Now I need a drink, alcoholic of course, \
after the heavy lectures involving quantum mechanics.'

res = [len(re.sub(r'[.,]', '', x)) for x in word.split(' ')]
print(res)
