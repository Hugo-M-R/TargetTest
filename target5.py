# Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;
# Solicita a entrada do usuário
string_original = input("Digite uma string: ")
string_invertida = ""

for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]
print("A string invertida é:", string_invertida)