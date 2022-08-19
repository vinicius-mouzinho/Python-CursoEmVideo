
'''

frase = 'curso_em_video_python'

O primeiro digito, que seria o ''c'', é o digito 0

quando usamos print((frase[9:21]) vamos printar com o início no caracter 9 e o fim no caracter 20 (o 21 não será usado)

print((frase[9::3])) = voph => o dois pontos vazio após o 9 significa que vai do 9 até o final, o dois pontos após significa
que vai pegar o digito 9 e depois o terceiro, sexto, nono etc digitos na sequência

ANÁLISE DA STRING

len(frase) = mostrar o comprimento da frase, que seria 21 caracteres

frase.count('o') = mostrar quantas vezes aparece a letra "o" minúscula

frase.count('o', 0, 13) = mostrar quantas vezes aparece a letra "o" minúscula
até o digito 12

frase.find('deo') = mostra vai indicar onde se encontra o início dessa sequência de digitos
na sua frase

frase.find('Android') = vai retornar o valor -1 nesse exemplo, pois essa sequência de digitos
não é encontrada

'Curso' in frase = aparecerá True ou False para vc saber se existe essa palavra na frase

TRANSFORMAÇÃO DA STRING

frase.replace('Python', 'Android') = vai substituir Python por Android.

frase.upper() = colocar frase em maiúsculo
frase.lower() = coloca a frase em minúsculo
frase.capitalize() = joga todos os caracteres para minúsculos e só o primeiro letra da FRASE fica em maiúsculo.
frase.title() = joga todos os caracteres para minúsculo e apenas a primeira letra de cada PALAVRA fica em maiúsculo.

frase.strip() = remove todos os espaços inúteis, presentes antes e depois da frase.
''   Aprenda Python  ''se transforma em ''Aprenda Python''.

frase.rstrip() = remove os espaços inúteis apenas do lado direito da frase.
''   Aprenda Python  '' se transforma em ''   Aprenda Python''.

frase.lstrip() = remove os espaços inúteis apenas do lado esquerdo da frase.
''   Aprenda Python  '' se transforma em ''Aprenda Python  ''

FUNCIONALIDADES DE DIVISÃO

frase.split() = no caso de "Curso em Video Python'', ele criaria frases diferentes que seriam
''Curso'', ''em'', ''Video'' e ''Python''. Ou seja, cada palavra recebe uma indexação nova.
Ou seja, essa função cria uma lista com todas as palavras de uma cadeia de caracteres.

'-'.join(frase) = junta todos os elementos da frase com um separador específico. Nesse caso, seria:
Curso-em-Video-Python


'''