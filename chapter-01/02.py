police_car: str = 'パトカー'
taxi: str = 'タクシー'

res: str = ''.join([p + t for p, t in zip(police_car, taxi)])

print(res)
