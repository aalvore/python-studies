palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    vogais = ''
    for letra in palavra:
        if letra in 'aeiou':
            vogais += letra

    print(f'Na palavra {palavra.upper()} contem as vogais {vogais.upper()}')
    