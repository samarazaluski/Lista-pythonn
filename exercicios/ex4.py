lista_palavras_ing = []
lista_palavras_pt = []

resp = 1

while(resp != 0):
    lista_palavras_ing.append(input("Digite uma palavra em inglês:"))
    lista_palavras_pt.append(input("Digite uma palavra em português:"))

    resp= int(input("Deseja continuar(1-sim/ 0 não"))
    palavra= input("Digite a palavra em inglês a ser traduzida:")

if(palavra in lista_palavras_ing):
    pos_palavra = lista_palavras_ing.index(palavra)
    print(f"A palavra em portugues é:{lista_palavras_pt[pos_palavra]}")

