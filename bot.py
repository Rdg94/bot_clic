# Passo 1: Instalar o Python
# Se você ainda não tem o Python instalado, siga os passos abaixo:

# Baixar o Python: Acesse python.org e faça o download da versão mais recente para o seu sistema operacional.
# Instalar o Python:
# Durante a instalação, marque a opção "Add Python to PATH" (muito importante!).
# Siga os passos de instalação padrão.

# Instalar as bibliotecas: Execute o seguinte comando para instalar o pyautogui: pip install pyautogui



#Importar as duas bibliotecas
import pyautogui 
import time

# Como o código precisava ser simples, deixei o login manual. Então faça login e e vá até a página de  aulas antes de rodar o código.

time.sleep(2)#Tempo de espera para abrir a página

pyautogui.click(x=-1164, y=338) #Indicação de onde o mouse deve clicar o arquivo auxilir serve para encontrar a posição corrata. Substitua x e y pela localização da sua tela. A posição varia de acordo com o tamanho e resolução da tela, por isso não coloquei uma posição fixa.


time.sleep(2)#Tempo de espera para a página carregar entre um clique e outro

#Para parar a automação, deixe o mouse parado no canto superior esquerdo da tela.