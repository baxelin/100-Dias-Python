from datetime import date

class Pessoa:
    def __init__(self, id, nome, data_nascimento):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return (self.id == other.id and 
                    self.nome == other.nome and 
                    self.data_nascimento == other.data_nascimento)
        return False

    def __hash__(self):
        return hash((self.id, self.nome, self.data_nascimento))

    def __str__(self):
        return f"Pessoa{{nome='{self.nome}'}}"

def remover_item_usando_filtro_especifico(lista):
    lista[:] = [pessoa for pessoa in lista if pessoa.nome != "George Harrison"]

def remover_item_usando_equals(lista):
    lennon = Pessoa("1", "John Lennon", date(1940, 10, 9))
    lista[:] = [pessoa for pessoa in lista if pessoa != lennon]

# Criando a lista de objetos Pessoa
beatles = [
    Pessoa("1", "John Lennon", date(1940, 10, 9)),
    Pessoa("2", "Paul McCartney", date(1942, 6, 18)),
    Pessoa("3", "George Harrison", date(1943, 2, 25)),
    Pessoa("4", "Ringo Starr", date(1940, 7, 7))
]

# Removendo itens com métodos diferentes
remover_item_usando_equals(beatles)
remover_item_usando_filtro_especifico(beatles)

# Exibindo o resultado
print(beatles)
