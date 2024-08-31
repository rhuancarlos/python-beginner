num1 = [5,2,3,1,14,15,2,18,23,11,25,29,30,15,5,3,15]
num_rep = 15
num_pos = 0

for x in num1:
  rest = x % 2
  if (rest != 0):
    print(f"{x} impar")
  else:
    print(f"{x} par")

print(f"Número de repetições de um elemento: {num_rep}")
print(num1.count(num_rep))

print("Número de elementos no array:")
print(len(num1))

print(f"Elemento na posicao {num_pos} no array:")
print(num1[num_pos])