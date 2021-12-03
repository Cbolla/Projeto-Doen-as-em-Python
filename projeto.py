import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import doenças

# fazendo um web scraping
# carregando o site
resposta = requests.get("https://super.abril.com.br/saude/as-grandes-epidemias-ao-longo-da-historia/")


# adicionando conteudo a uma variavel
conteudo = resposta.content

# lendo o site como html
site = BeautifulSoup(conteudo, 'html.parser')
# pesquisando informação por div e classes

titulo1 = site.find("div", {'class': 'post-header'})
#transformando o codigo  html em conteudo text
titulo1text = site.find("h1", {'class': 'title'})

# apresentando o projeto

print(f"Bem vindo ao nosso projeto \n Hoje vamos falar sobre.\n")

print("     " ,titulo1text.text ,"     \n\n")

# mostrando os topicos
print("Alguns topicos do nosso trabalho")
print("1 - PESTE NEGRA \n 2 - CÓLERA \n 3 - TUBERCULOSE \n 4 - VARÍOLA \n 5 - GRIPE ESPANHOLA  \n 6 - FEBRE AMARELA \n 7 - SARAMPO \n 8 - AIDS \n 9 - COVID-19 \n\n\n")

# criando funçao para selecao de topico

def selecao(n):
    if n == 1:
        print(doenças.pestenegra)
        file.write("Peste Negra\n")
    if n == 2:
        print(doenças.colera)
        file.write("Colera\n")
    if n == 3:
        print(doenças.tuberculose)
        file.write("Tuberculo\n")
    if n == 4:
        print(doenças.variola)
        file.write("Variola\n")
    if n == 5:
        print(doenças.espanhola)
        file.write("Gripe Espanhola\n")
    if n == 6:
        print(doenças.febreamarela)
        file.write("Febre Amarela\n")
    if n == 7:
        print(doenças.sarampo)
        file.write("Sarampo\n")
    if n == 8:
        print(doenças.aids)
        file.write("Aids\n")
    if n == 9:
        print(doenças.covid)
        file.write("Covid-19\n")

        
res = str(input("Deseja continuar?  S/N  : "))
while res.upper() == "S":
    pergunta = str(input("Deseja pesquisar por topico ou ver os graficos: "))
    if pergunta.upper() == "TOPICO":
        file = open("topicos-pesquisados.txt","a")
        topico = int(input("Digite o numero do topico que deseja saber sobre:"))
        selecao(topico)
        file.close()
        res = str(input("Deseja continuar? S/N : "))
        if res.upper() == "N":
            print("Fim")
    if pergunta.upper() == "GRAFICOS":
        pgraf = str(input("Qual grafico quer ver: mortes/tempo: "))
        if pgraf.upper() == "MORTES":
            x = "Peste Negra","Colera","tuberculose","Variola","Gripe Espanhola","Febre Amarela","Sarampo","Aids","Covid-19"
            y = 50000000,100000,10**9,300000000,20000000,30000,6000000,22000000,5220000
            plt.title("Numero de mortes por doenças.")
            plt.ylabel("Número de mortes por doença (em bilhões )")
            plt.xlabel("Nome das doenças")
            plt.bar(x,y)
            plt.show()
            res = str(input("Deseja continuar? S/N : "))
            if res.upper() == "N":
                    print("Fim")
        if pgraf.upper() == "TEMPO":
            x = "Peste Negra","Colera","tuberculose","Variola","Gripe Espanhola","Febre Amarela","Sarampo","Aids","Covid-19"
            y = 1351,1824,1950,1980,1919,1962,1963,1981,2021
            plt.bar(x,y)
            plt.title("Ano de todas as Doenças.")
            plt.ylabel("Anos")
            plt.xlabel("Nome das doenças")
            plt.show()
file.close()
    



