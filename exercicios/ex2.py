lista_idades = []


soma_idades = 0
qtd_menor18 = 0

idade = int(input("Digite a idade do usuario:"))

while(idade>0):
    lista_idades.append(idade)
    idade= int(input("Digite a idade do usuario"))

for i in range(len(lista_idades)):
    soma_idades+=lista_idades[i]
    if(lista_idades[i] <18):
        qtd_menor18+=1
media_idades = soma_idades / len(lista_idades)

print(f"Media das idaes:{media_idades:.2f}")
print(f"Quantidade de menores de 18 anos>{qtd_menor18} ")