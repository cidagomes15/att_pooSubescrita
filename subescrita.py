
class Integrante_IFRN:
    def exibirMensagem(self):
        print("Seja bem vindo(a) ao IFRN!!!")

class Professor(Integrante_IFRN):
    def exibirMensagem(self):
        print("Meus alunos são os melhores!!!")


class Aluno(Integrante_IFRN):
    def exibirMensagem(self):
        print("Vou estudar pra tirar 100 em POO!!!")


if __name__ == "__main__":
    
    integrante = Integrante_IFRN()
    professor = Professor()
    aluno = Aluno()

    
    integrante.exibirMensagem() 
    professor.exibirMensagem()   
    aluno.exibirMensagem()   
