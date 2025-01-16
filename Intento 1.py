MAX=100
def pedir_num():
    num=int(input("Ingrese el numero a convertir"))
    while num<0:
        num=int(input("Ingrese Un numero positivo"))
    return num
def creacion():
    v=[1 for position in range(0,MAX)]
    return(v)
def decimal_a_binario(num):
    vBinario=creacion()
    pos=0
    while num != 1:
        vBinario[pos]=num%2
        num=num//2
        pos=pos+1
    pos=pos+1
    return(vBinario,pos)
def mostrar_vector(vbinario,pos):
    for position in range(pos-1,-1,-1):
        print(vbinario[position],end="")

def main():
    num=pedir_num()
    [vBinario,pos]=decimal_a_binario(num)
    mostrar_vector(vBinario,pos)
main()