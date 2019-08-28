#Cap8Completo - Capitulo 8 do livro de Automatização Massiva com Python
#Lendo e escrevendo em arquivos.

import os
print(os.path.join('usr', 'bin', 'spam'))

#R:
#usr\bin\spam

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filenames in myFiles:
    print(os.path.join('C:\\Users', filenames))

#R:
#C:\Users\accounts.txt
#C:\Users\details.csv
#C:\Users\invite.docx

#----------------------Diretorio de Trabalho Atual---------------------
# Para obter o diretorio de trabalho atual utilize o comando os.getcwd()
# e para muda-lo utilize os.chdir()

print(os.getcwd())
os.chdir('C:\\Users\\Usuário\\Desktop\AMP\\')
print(os.getcwd())

#R:
#C:\Users\Usuário\Desktop\AMP\Lendo e escrevendo em arquivos
#C:\Users\Usuário\Desktop\AMP

#--------------------Criando novas pastas------------------------
# Para criar novas pastas utiize o comando os.makedirs()

#os.makedirs('C:\\delicious\\walnut\\waffles')

#---------------------Lidando com paths absolutos e relativos--------------------
# Chamar os.path.abspath(path) é uma maneira facil de converter um path relativo em um
#path abosluto
# Chamar os.path.isabs(path) retornará True se o argumento for um path absoluto e False
#se for um path relativo
# Chamar os.path.relpath(path, inicio) retornara uma string contendo um path relativo
# ao path inicio para path. Se inicio nao for especificado, o diretorio de trabalho atual
# sera usado como path de inicio
print()
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

#R:
#C:\Users\Usuário\Desktop\AMP
#C:\Users\Usuário\Desktop\AMP\Scripts
#False
#True

print(os.path.relpath('C:\\Windows', 'C:\\'))

path ='C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

#R:
#calc.exe
#C:\Windows\System32

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))

#R:
#('C:\\Windows\\System32', 'calc.exe')

print(calcFilePath.split(os.path.sep))

#R:
#['C:', 'Windows', 'System32', 'calc.exe']

#--------------------Obtendo os tamanhos dos arquivos e o conteudo das pastas------------------
# Chamar os.path.getsize(path) retornará o tamanho em bytes do arquivo no argumento path
# Chamar os.listdir(path) retornará uma lista de strings com nomes de arquivo para cada arquivo
#no argumento path.

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print(os.listdir('C:\\Windows\\System32'))

#R:
#26112
#Squeezed text 691 lines

#Se quiser descobrir o tamanho total de todos os arquivos nesse diretorio, poderei usar
#os.path.getsize() e os.listdir() juntos.

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

#R:
#1333183020
