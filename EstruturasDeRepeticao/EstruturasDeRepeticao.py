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

print("A soma dos números de 1 a 100 com loop WHILE é: ", soma);

print(" ");

""""4- Utilizando um loop "for", calcule a soma dos números de 1 a
100."""

soma = 0
for i in range(1,101):
    soma += i;
print("A soma dos números de 1 a 100 com loop FOR é: ", soma);

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

for i in range(2,21, 2):
        print(i);

print(" ");

"""7- Utilizando um loop "while", inverta uma string digitada pelo usuário."""

string = (input("Digite uma string: "));

indice = len(string) - 1;
string_invertida = ""

while indice >= 0:
    string_invertida += string[indice]
    indice -= 1

print("A string invertida é: ", string_invertida);

print(" ");

"""8- Utilizando um loop "for", verifique se uma palavra digitada pelo
usuário é um palíndromo (lê-se da mesma forma de trás para frente)."""

palavra = input("Digite uma palavra: ");

palavra_invertida = "";

for letra in palavra:
    palavra_invertida = letra + palavra_invertida;
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.");
else:
    print("A palavra não é um palíndromo.");

print(" ");

"""9- Utilizando um loop "while", encontre o menor número inteiro cujo
quadrado seja maior do que 1000."""

numero = 1;

while numero ** 2 <= 1000:
    numero += 1;

print("O menor número inteiro cujo quadrado é maior que 1.000 é: ", numero);

print(" ");

"""10- Utilizando um loop "for", imprima os elementos de uma lista em
ordem inversa."""

lista = ["a", "b", "c", "d", "e"];

for indice in range(len(lista)-1, -1, -1):
    print(lista[indice]);

