__author__ = 'beatrizdsperes'

class Perfil:

    def __init__(self):
        self.Copiador = self.Inovador = self.Explorador = self.Planejador = self.Egocentrico = self.Impulsivo = self.Heuristica = 0

class Botao_Duvida:

    def __init__(self, e_botao, perfil):
        self.e_botao = e_botao
        e_botao.onclick = self.clicou
        self.perfil = perfil
        self.Contador = 0

    def clicou(self, ev):
        perfil = self.perfil
        self.Contador =self.Contador + 1
        if (self.Contador == 1):
            perfil.Copiador = perfil.Copiador + 1
            perfil.Inovador = perfil.Inovador + 1
            perfil.Explorador = perfil.Explorador + 1
            perfil.Planejador = perfil.Planejador + 1

        else:

            if (self.Contador == 2):
                perfil.Copiador = 0
                perfil.Planejador = 0
                perfil.Inovador = 0
                perfil.Explorador = 0
            perfil.Copiador = perfil.Copiador + 1
            perfil.Impulsivo = perfil.Impulsivo + 1
            perfil.Egocentrico = perfil.Egocentrico + 1

        print(perfil.Copiador, perfil.Inovador, perfil.Heuristica,perfil.Explorador, perfil.Impulsivo, perfil.Planejador, perfil.Egocentrico)

class Botao_Curtir:

    def __init__(self, e_botao, perfil):
        self.e_botao = e_botao
        e_botao.onclick = self.clicou
        self.perfil = perfil
        self.Contador = 0

    def clicou(self, ev):

        perfil = self.perfil
        self.Contador = self.Contador + 1
        if (self.Contador == 1):
            perfil.Explorador = perfil.Explorador + 1
            perfil.Planejador = perfil.Planejador + 1

        else:

            if (self.Contador == 2):
                perfil.Explorador = 0
                perfil.Planejador = 0
            perfil.Impulsivo = perfil.Impulsivo + 1
            perfil.Egocentrico = perfil.Egocentrico + 1

        print(perfil.Copiador, perfil.Inovador, perfil.Heuristica,perfil.Explorador, perfil.Impulsivo, perfil.Planejador, perfil.Egocentrico)

class Botao_Descurtir:

    def __init__(self, e_botao, perfil, c, t):
        self.e_botao = e_botao
        self.c = c
        self.t = t
        c.style.opacity = 1
        c.style.display = "block"
        c.ontransitionend = self.ficoubranco
        e_botao.onclick = self.clicou
        e_botao.onclick = self.ficoupreto

        self.perfil = perfil
        self.Contador = 0

    def ficoupreto (self, c):
        self.c.style.display = "block"
        self.c.style.opacity = 0

    def ficoubranco (self, c):
        self.c.style.opacity = 1
        #self.c.style.display = "none"
        print ("foi")


    def clicou(self, ev):

        perfil = self.perfil
        self.Contador = self.Contador + 1
        if (self.Contador == 1):
            perfil.Explorador = perfil.Explorador + 1
            perfil.Planejador = perfil.Planejador + 1

        else:

             if (self.Contador == 2):
                perfil.Explorador = 0
                perfil.Planejador = 0
             perfil.Impulsivo = perfil.Impulsivo + 1
             perfil.Egocentrico = perfil.Egocentrico + 1



        print(perfil.Copiador, perfil.Inovador, perfil.Heuristica,perfil.Explorador, perfil.Impulsivo, perfil.Planejador, perfil.Egocentrico)

class Botao_Som:

    def __init__(self, e_botao, perfil):
        self.e_botao = e_botao
        e_botao.onclick = self.clicou
        self.perfil = perfil
        self.Contador = 0

    def clicou(self, ev):

        perfil = self.perfil
        self.Contador = self.Contador + 1
        if (self.Contador == 1):
            perfil.Explorador = perfil.Explorador + 1
            perfil.Planejador = perfil.Planejador + 1

        else:

            if (self.Contador == 2):
                perfil.Explorador = 0
                perfil.Planejador = 0
            perfil.Copiador = perfil.Copiador + 1
            perfil.Inovador = perfil.Inovador + 1
            perfil.Explorador = perfil.Explorador + 1
            perfil.Planejador = perfil.Planejador + 1

        print(perfil.Copiador, perfil.Inovador, perfil.Heuristica,perfil.Explorador, perfil.Impulsivo, perfil.Planejador, perfil.Egocentrico)

        
def main(html, doc):
    tela = doc["main"]
    c = tela
    t = doc["tudo"]
    #c.ontransitionend= Botao_Descurtir.ficoupreto
    #c.ontransition = Botao_Descurtir.ficoubranco
    perfil = Perfil()
    splash = html.DIV("VOADORAS")
    tela <= splash
    botao1 = html.BUTTON("duvida")
    tela <= botao1
    bot = Botao_Duvida(botao1, perfil)
    botao2 = html.BUTTON("curtir")
    tela <= botao2
    bnt = Botao_Curtir(botao2, perfil)
    botao3 = html.BUTTON("descurtir")
    tela <= botao3
    bbt = Botao_Descurtir(botao3, perfil, c, t)
    botao4 = html.BUTTON("som")
    tela <= botao4
    boto = Botao_Som(botao4, perfil)
    print(perfil.Copiador, perfil.Inovador, perfil.Heuristica,perfil.Explorador, perfil.Impulsivo, perfil.Planejador, perfil.Egocentrico)

