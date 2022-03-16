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
#============================================================================================

if __name__ == "__main__":
    #Validador de expressao
    p1 = Pilha()
    algoritimo = str(input('Digite a expresão matematica: '))
    exprAbrir = ['{','[','(']
    exprFechar= ['}',']',')']
    for i in algoritimo:
        if i in exprAbrir:
            p1.push(i)
        elif i in exprFechar:
            if p1.is_empty():
                print('Expressão inválida!')
                break
            if p1.peek() == exprAbrir[exprFechar.index(i)]:
                p1.pop()
            else:
                print('Expressão inválida!')
                break
    if p1.is_empty():
        print('Expressão válida!')
    else:
        print('Expressão inválida!')
