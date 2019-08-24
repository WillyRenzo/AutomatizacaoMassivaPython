#Cap7Completo.py - Capitulo 7 Completo do livro Automatização Massiva com Python
#Correspondencia de padroes com expressoes regulares


#Biblioteca para uso de expressões regulares.
import re


'''
phoneNumRegex = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone Number found:' +mo.group())

#-----------------------------Separando grupos com parenteses----------------------
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups())

#------------------------------Recebendo os valores em duas variaveis----------------------
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

#---------------------------------(\( \))---------------------------------------------------
#são caracteres de escape, ou seja, podemos utilizar para identificar o parenteses em padroes
phoneNumRegex = re.compile('(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415)-555-4242')
print('Phone Number found:' +mo.group())

#------------------------------------Utilizando | pipe-------------------------------

heroRegex = re.compile('Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

#------------------------------Colocando em evidencia com o pipe(mais de uma opção)---------------------

batRegex = re.compile('Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())

#---------------------------Colocando ()? para grupos opcionais-----------------------------------

batRegex2 = re.compile('Bat(wo)?man')
mo4 = batRegex2.search('The adventures of Batman')
mo5 = batRegex2.search('The adventures of Batwoman')
print(mo4.group())
print(mo5.group())

#---------------------------Colocando ()* para zero ou mais ocorrencias-------------------------

batRegex3 = re.compile('Bat(wo)*man')
mo6 = batRegex3.search('The adventures of Batwoman')
mo7 = batRegex3.search('The adventures of Batwowowowoman')
mo8 = batRegex3
.search('The adventures of Batman')
print(mo6.group())
print(mo7.group())
print(mo8.group())

#------------------------Colocando ()+ para uma ou mais ocorrencias-----------------------

batRegex4 = re.compile('Bat(wo)+man')
mo9 = batRegex4.search('The adventures of Batwoman')
mo10 = batRegex4.search('The adventures of Batwowowowoman')
mo11 = batRegex4.search('The adventures of Batman')
print(mo9.group())
print(mo10.group())
print(mo11.group())


#---------------------------Correspondendo a repetições especificas---------------------

haRegex = re.compile('(Ha){3}')
haRegex2 = re.compile('(Ha){3,5}') #intervalo de 3 a 5 repeticoes
haRegex3 = re.compile('(Ha){3,}') # 3 ou mais
haRegex4 = re.compile('(Ha){,5}') # 5 ou menos

mo1 = haRegex.search('HaHaHa')
mo2 = haRegex2.search('HaHaHaHa')
mo3 = haRegex3.search('HaHaHaHaHaHa')
mo4 = haRegex4.search('HaHa')

print(mo1.group())
print(mo2.group())
print(mo3.group())
print(mo4.group())
print(mo1.group())

#---------------------------Correspondencia greedy e nongreedy (){}?-------------------
#greedy é o default do python, logo o algoritmo procurara a maior string.

nongreedyHaRegex = re.compile('(Ha){3,5}?')
mo = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo.group())

#------------------------Metodo findall------------------------------------------.

phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000 Amor: 222-333-4444')
print(mo1)

#------------------------Classe de Caractere-----------------------------------
#\d - qualquer digito de 0 a 9
#\D - qualquer caractere que NÃO seja um digito de 0 a 9
#\w - qualquer letra,digito ou o caractere underscore(Palavra)
#\W - qualquer caractere que NÃO seja uma letra,digito ou o caractere underscore
#\s - qualquer espaço, tabulação ou caractere de quebra de linha
#\S - qualquer caractere que NÃO seja um espaço, tabulação ou caractere de quebra de linha

xmasRegex = re.compile('\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords'))


#Criando minha própria classe de caractere
#[] Colchete é utilizado para criar sua propria classe.

vowelRegex = re.compile('[aeiouAEIOU]') #Exemplo que captura todas as vogais minusculas ou maiusculas.
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))


#---------------------Acento circunflexo e sinal do dolar-------------------
#^ usado para indicar uma correspondencia no inicio de um texto
#$ usado para indicar uma correspondencia no final de um texto
# ^ e $ podem ser usados juntos para significar uma string inteira.

beginsWithHello = re.compile('^Hello') #Comeca com Hello
print(beginsWithHello.search('Hello World'))
endsWithNumber = re.compile('\d$')  #Finaliza com um digito
print(endsWithNumber.search('Your number is 42'))
wholeStringIsNum = re.compile('^\d+$')
print(wholeStringIsNum.search('1234')) #String inteira numero

#R:
#<re.Match object; span=(0, 5), match='Hello'>
#<re.Match object; span=(16, 17), match='2'>
#<re.Match object; span=(0, 4), match='1234'>

#-------------------Caractere curinga-----------------------------------------
# . corresponde a qqr caractere exceto uma  quebra de linha

atRegex = re.compile('.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

#R:
#['cat', 'hat', 'sat', 'lat', 'mat']


#------------------Correspondendo a tudo usando ponto-asterisc0------------------------
# Podemos usar (.*) para indicar q queremos qualquer caractere.

nameRegex = re.compile('First Name: (.*), Last Name: (.*)')
mo = nameRegex.search('First Name: Jefferson, Last Name: Aputaquetepariu')
print(mo.group(1))
print(mo.group(2))

#R:
#Jefferson
#Aputaquetepariu

#---------------Correspondendo a quebras de linhas com o caractere ponto---------------
# O (.*) correspondera a tudo incluindo quebras de linhas ao passar o segundo
#argumento re.DOTALL

newlineRegex = re.compile('.*',re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law'))
#R:
#<re.Match object; span=(0, 60), match='Serve the public trust.\nProtect the innocent.\nU>


#------------Correspondendo sem diferenciar letras maiusculas e minusculas-----------------
# Para fazer a correspondencia sem diferenciar letras maiusculas e minusculas passe o segundo
#argumento como re.IGNORECASE ou re.I

robocop = re.compile('robocop', re.I)
print(robocop.search('ROBOCOP is part man, part machine'))
print(robocop.search('robocop is part man, part machine'))

#R:
#<re.Match object; span=(0, 7), match='ROBOCOP'>
#<re.Match object; span=(0, 7), match='robocop'>


#-----------Substituindo strings com o metodo sub()-----------------------------------
# Para substituir os padroes por novos textos, utilizamos o metodo sub(), passando como
#primeiro argumento a string para substituição e segundo argumento é a string para a
#expressao regular.

namesRegex = re.compile('Agent \w+')
print(namesRegex.sub('Censored', 'Agent Alice gave the secret documents to Agent Willy'))

#R:
#Censored gave the secret documents to Censored

#--------Substituindo partes das string apenas---------------------------------------
# utilizamos \1,\2,\3 para fazer caracteres escaparem da substituição

agentNamesRegex = re.compile('Agent (\w)\w*')
print(agentNamesRegex.sub('\1***', 'Agent Alice told Agent Carol'))
'''

#---------Administrando regex complexas------------------------------------
#Para ignorar comentarios e espacos em brancos nas strings utilize o segundo argumento
#re.VERBOSE.

phoneRegex = re.compile('''((\d{3}|\(\d{3}\))? #Codigo de Area
                        (\s|-|\.)?         #Separador
                        \d{3}              #Primeiros 3 digitos
                        (\s|-|\.)           #Separador
                        \d{4}               #Ultimos 4 digitos
                        (\s*(ext|x|ext.)\s*\d{2,5})?    #Extensao
                        )''', re.VERBOSE)
