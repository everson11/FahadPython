class Pilha:
    def __init__(self):
        self._vet = [] # lista interna

    def peek(self): # retorna qual item esta no topo
        return self._vet[-1]
       
    def push(self, item): # metodo de inserir item
        self._vet.append(item)
        
    def pop(self): # remover o topo e retornar item para usuario
        # tratar caso de underflow
        if self.is_empty():
            print("Lista Vazia!")
            return None
        return self._vet.pop()
                
    def is_empty(self): # teste se é vazia
        if len(self._vet) > 0:
            return False
        return True
        
    def __len__(self): # retorna o total de itens
        return len(self._vet)

    def __str__(self): # representacao da pilha como string
        return str(self._vet)

import os
print('-='*35)
print('           Conversor de decimal para binario               ')
print('-='*35)
#converter decimal para binario
if __name__ == "__main__":
    p1 = Pilha()
    numero = int(input('Digite um numero decimal: '))
    while numero > 0:
        p1.push(numero % 2)
        numero = numero // 2
    print('O numero binario é: ', end='')
    while not p1.is_empty():
        print(p1.pop(), end='')
    print()
    os.system('pause')


print('-='* 20)
#### Forma mais simples de resolver:
if __name__ == "__main__":
    p1 = Pilha()
    num = int(input('(Forma mais simplificada) -Digite um numerro : '))
    if num > 0 :
        p1.push(bin(num)[2:])# removendo os 2 primeiro algarismo da lista usando slicing
        print('A conversão é :',p1)