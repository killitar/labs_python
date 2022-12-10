elements = [2,1,-4,0,-1,-t6FpLlGv st104649@ruc.su
print(sum(element for i, element in enumerate(elements) if not i & 1))

s1 = s2 = 0
for s1, a in enumerate(elements):
    if a > 0:
        break  # индекс первого положительного элемента
for s2, a in enumerate(reversed(elements)):
    if a > 0:
        break  # оиндекс последнего положительного элемента
s = sum(elements[s1+1: -s2-1])  # сумму между индексами
print(s)
t6FpLlGv st104649@ruc.su


res = sorted(elements, key = lambda i: 0 if i == 0 else -1 / i)
# elements.sort(key=lambda x: x < 0)

print(res)


