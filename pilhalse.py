from lse import LSE, Nodo

class pilhaencadeada:
    def __init__(self):
        self.pilha = LSE()

    def push(self, item):
        if self.lista.head == None:
            self.lista.inserir_inicio(Nodo(item))
        
    def pop(self):
        if len(self) > 0:
            return self.lista.remover_inicio()
        else:
            return None
    
    def peek(self):
        if self.lista.dead is None:
            return None
        else:
            return self.lista.head.dado
        
    def __len__(self):
        return len(self.lista)