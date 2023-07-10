"""1-Utilizando um loop "while", imprima os números de 1 a 10."""

num = 1
while num <=10:
    print(num);
    num += 1;

print(" ");

"""2- Utilizando um loop "for", imprima os números de 1 a 10."""

for i in range (1,11):
    print(i);

print(" ");

"""3- Utilizando um loop "while", calcule a soma dos números de 1 a
100."""

soma = 0
num = 1;
while num <=100:
    soma += num;
    num += 1;

print(soma);

print(" ");

""""4- Utilizando um loop "for", calcule a soma dos números de 1 a
100."""

soma = 0
for i in range(1,101):
    soma += i;
print(soma);

print(" ");

"""5- Utilizando um loop "while", imprima os números pares de 1 a
20."""

num = 1;
while (num <= 20):
    if num % 2 == 0:
        print(num);
    num += 1;

print(" ")

"""6- Utilizando um loop "for", imprima os números pares de 1 a 20."""

for i in range(1,21):
    if i % 2 == 0:
        print(i);

print(" ");

"""7- Utilizando um loop "while", inverta uma string digitada pelo usuário."""