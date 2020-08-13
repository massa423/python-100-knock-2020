patrolcar: str = 'パトカー'
taxi: str = 'タクシー'

res: str = ''

for i in range(len(patrolcar)):
    res += patrolcar[i]
    res += taxi[i]

print(res)
