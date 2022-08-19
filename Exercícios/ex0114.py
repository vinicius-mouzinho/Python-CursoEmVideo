import urllib.request
try:
    page = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print('\033[31mERRO! O site está inacessível.\033[m')
else:
    print("Consegui acessar o site com sucesso.")
