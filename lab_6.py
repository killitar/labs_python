elements = [2,1,4,0,-1,-2]
 
print(sum(element for i, element in enumerate(elements) if not i & 1))

s1 = s2 = 0
for s1, a in enumerate(elements):
    if a > 0:
        break  # определить индекс первого положительного элемента
for s2, a in enumerate(reversed(elements)):
    if a > 0:
        break  # определить индекс последнего положительного элемента
s = sum(elements[s1+1: -s2-1])  # взять сумму между индексами
print(s)

elements.sort(key=lambda x: x < 0)

print(elements)


