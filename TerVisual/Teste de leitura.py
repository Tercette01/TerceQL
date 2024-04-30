arquivo = open('C:\\Users\\mathe\\OneDrive\\Área de Trabalho\\Criações\\TerceQL\\TerVisual\\text.TV', 'r')

entidades = []
entidade_atual = {}

for linha in arquivo:
    # Se a linha é vazia, isso significa que estamos começando um novo parágrafo
    if linha.strip() == '':
        # Adiciona a entidade atual à lista de entidades e começa uma nova
        entidades.append(entidade_atual)
        entidade_atual = {}
    else:
        # Divide a linha em chave e valor
        chave, valor = linha.split(':', 1)
        # Remove espaços em branco extras
        chave = chave.strip()
        valor = valor.strip()
        # Adiciona a chave e o valor à entidade atual
        entidade_atual[chave] = valor

# Não se esqueça de adicionar a última entidade à lista
if entidade_atual:
    entidades.append(entidade_atual)

arquivo.close()

# Agora a variável 'entidades' é uma lista de dicionários, onde cada dicionário representa uma entidade do arquivo
print(entidades)
