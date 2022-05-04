def getMsg():
    a=input("Insira algo:")
    return a

def stringToList(a):
    lista=list(a.strip(""))
    return lista

def listToString(a):
    msgfinal=("")
    msgfinal= msgfinal.join(a)
    return msgfinal

def trocaLetras(lista):
    for x in range(len(lista)):
        if (lista[x].isnumeric()== False):
            if (x % 2 ==0):
                lista[x]=lista[x].lower()
            else:
                lista[x]=lista[x].upper()
        if (lista[x].isnumeric()== False):
            if (lista[x] == "a"):
                lista[x]="4"
            if (lista[x] == "A"):
                lista[x]="4"
            if (lista[x] == "e"):
                lista[x]="3"
            if (lista[x] == "E"):
                lista[x]="3"            
            if (lista[x] == "i"):
                lista[x]="1"
            if (lista[x] == "I"):
                lista[x]="1"
            if (lista[x] == "o"):
                lista[x]="0"
            if (lista[x] == "O"):
                lista[x]="0"
            

msg=getMsg()
lista=stringToList(msg)  
novalista=trocaLetras(lista)
resultado=("")
resultado=resultado.join(lista)
print(resultado)
            





