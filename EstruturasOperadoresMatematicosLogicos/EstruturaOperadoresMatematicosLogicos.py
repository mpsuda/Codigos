"""1-Escreva um programa que solicite ao usuário dois números
inteiros e exiba a soma, subtração, multiplicação e divisão entre
esses números."""

#Solicitando ao usuário para incluir 2 números
num1 = int(input("Favor inserir um numero inteiro: "));
num2 = int(input("Favor inserir outro numero inteiro: "));

#Operações matemáticas
soma          = num1 + num2;
subtracao     = num1 - num2;
multiplicacao = num1 * num2;
divisao       = num1 / num2;

#Impressão dos resultados
print("A soma dos 2 números é: ", soma);
print("A subtração dos 2 números é: ", subtracao);
print("A multiplicação dos 2 números é: ", multiplicacao);
print("A divisão dos 2 números é: ", divisao);

print(" ");

"""2- Escreva um programa que solicite ao usuário uma temperatura
em graus Celsius e verifique se ela está acima do ponto de
ebulição da água (100°C). Caso positivo, exiba a mensagem "A
água está fervendo!"."""

temperatura = int(input("Qual a temperatura em graus Celsius da água? "));

if temperatura > 100:
    print("A água está fervendo!");
else: 
    print("Esquente mais a água!!!");

print(" ");

"""3- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é par ou ímpar."""

parImpar = int(input(" Favor inserir um número inteiro: "));

if parImpar % 2 == 0:
    print(" O número informado é PAR!");
else:
    print("O número informado é IMPAR!");

print(" ");

"""4- Escreva um programa que solicite uma senha ao usuário e
verifique se a senha está correta. Considere a senha correta como
"123456"."""

senha = int(input("Digite uma senha com 6 digitos: "));

senhaCorreta = 123456;

if senha == senhaCorreta:
    print("Senha Correta!");
else:
    print("Cuidado! Senha Errada!");

print(" ");

"""5- Escreva um programa que solicite ao usuário uma idade e
verifique se ela está entre 18 e 30 anos (inclusive)."""

idade = int(input("Favor informar sua idade: "));

if (idade > 18) and (idade <= 30):
    print("Você possui mais de 18 anos, e tem até 30 anos.");
else:
    print("Infelizmente sua idade não está entre as que buscamos.");

print(" ");

"""6- Escreva um programa que solicite ao usuário três números
inteiros e verifique se pelo menos um deles é positivo."""

num1 = int(input("Favor informar um número inteiro: "));

num2 = int(input("Favor informar outro número inteiro: "));

num3 = int(input("Favor informar mais um número inteiro: "));

if (num1 > 0) or (num2 > 0) or (num3 > 0):
    print("Pelo menos um dos números informados é positivo!");
else:
    print("Todos os números informados são negativos ou zero.");

print(" ");

"""7- Escreva um programa que solicite ao usuário uma letra e
verifique se ela é uma vogal (a, e, i, o, u)."""

letra = input("Favor informar uma única letra minúscula: ");

if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
    print("A letra informada é uma VOGAL!");
else:
    print("A letra informada é uma CONSOANTE!");

print(" ");

"""8- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é positivo, negativo ou zero."""

num1 = int(input("Favor informar um número inteiro: "));

if num1 == 0:
    print("O número informado é igual a ZERO!");
elif num1 > 0:
    print("O número informado é POSITIVO!");
else:
    print("O número informado é NEGATIVO!");

print(" ");

"""9- Escreva um programa que solicite ao usuário três números e
verifique se eles estão em ordem crescente."""

num1 = int(input("Favor informar um número inteiro: "));

num2 = int(input("Favor informar outro número inteiro: "));

num3 = int(input("Favor informar mais um número inteiro: "));

if (num1 < num2) and (num2 < num3):
    print("Os 3 números são CRESCENTES!");
elif (num1 > num2) and (num2 > num3):
    print("Os 3 números são DECRESCENTES!");
else:
    print("Os 3 números NÃO estão em sequência crescente ou decrescente.");

print(" ");

"""10- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo."""

num1 = int(input("Por favor, digite um número: "));

if (num1 % 3 == 0) and (num1 % 5 == 0):
    print("O número informado é um múltiplo de 3 e 5 ao mesmo tempo!");
else:
    print("O número informado NÃO é um múltiplo de 3 e 5 ao mesmo tempo!");

print(" ");