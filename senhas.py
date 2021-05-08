senha = input("Digite a senha a ser criptografada (por favor em maiusculo)")
letterA = 'A'
letterE = 'E'
letterI = 'I'
letterO = 'O'
letterU = 'U'
senhanova = senha
for letter in senha:
    if letter == letterA:
        senhanova = senha.replace('A', '@')
        print (senhanova)
    if letter == letterE:
        senhanova = senhanova.replace('E', '&')
        print (senhanova)

    if letter == letterI:
        senhanova = senhanova.replace('I', '%?')
        print (senhanova)
    
    if letter == letterO:
        senhanova = senhanova.replace('O', '<#*')
        print (senhanova)

    if letter == letterU:
        senhanova = senhanova.replace('U', '!%')
        print(senhanova)

print(senhanova)
