class Gato:
    def __init__(self, raca:str, cor:str, tipo_pelo:str, idade:int, nome:str):
        """
        Docstring for __init__
        
        :param self: Comando que faz os atributos e metos olharem para a classe 
        :param raca: Digite a raça do seu gato
        :type raca: str
        :param cor: Digite a cor do gato 
        :type cor: str
        :param tipo_pelo: Digite o tipo do pelo(Sem pelo, Pelo long, Sem pelo, Pelo curto)
        :type tipo_pelo: str
        :param idade: Digite a idade do gato com numero inteiro
        :type idade: int
        :param nome: Digite o nome do gato
        :type nome: str
        """
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor = cor
        self.tipo_pelo = tipo_pelo

    def miar(self):
        print(f"O {self.nome} miou")


meu_gato = Gato("Angora", "Preto" , "Pelo longo",7,"Salvador" )
meu_gato.miar()


