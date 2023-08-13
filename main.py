class Professor:
    def __init__(self, nome): #construtor da classe professor
        self.nome = nome
    def ministrar_aula(self, assunto): #metodo para dizer qual assunto o professor esta ministrando aula
        print(f'O professor {self.nome} esta ministrando uma aula sobre {assunto}.')

class Aluno:
    def __init__(self, nome): #construtor da classe aluno
        self.nome = nome
    def presenca(self): #metodo para dar presenca ao aluno
        print(f'O aluno {self.nome} esta presente.')
class Aula:
    alunos = []
    def __init__(self,Professor, assunto):
        self.assunto = assunto
        self.Professor = Professor
        self.Aluno = Aluno
    def adicionar_aluno (self, Aluno):
        self.alunos.append(Aluno.nome)
    def listar_presenca (self):
        print(f'Presenca na aula sobre {self.assunto}, ministrada pelo professor {self.Professor.nome}: ')
        print (self.alunos)


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos",)
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())


