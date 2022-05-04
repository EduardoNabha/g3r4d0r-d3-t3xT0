msg=input("Insira a mensagem para ser mudada:\n")
frase=list(msg.strip(""))
tamanho=len(frase)
resultado=("")
for x in range(len(frase)):
    if (x % 2 == 0):
        frase[x]=frase[x].lower()
    else:
        frase[x]=frase[x].upper()

resultado=resultado.join(frase)

print(resultado)


