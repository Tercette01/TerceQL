# TerceQL
Uma linguagem onde uni a visualização do site e com o banco de dados a partir do python

## Coisas que precisam ser feitas
### Desenvolvendo o arquivo .TV ou TerVisual
- [X] Começar pela parte de criar um comando pro terminal
- [X] Criar o comando para texto
  - [X] Criar subcomandos para o texto, no caso cor
  - [x] Criar subcomandos para o texto, no caso tamanho
  - [ ] Criar subcomandos para o texto, no caso negrito
  - [ ] Criar subcomandos para o texto, no caso italico
  - [ ] Criar subcomandos para o texto, no caso cor para italico
- [ ] Criar o comando para inserir texto
  - [ ] Criar subcomandos para o texto, no caso desabilitado
  - [ ] Criar subcomandos para o texto, no caso somente leitura
  - [ ] Criar subcomandos para o texto, no caso com dica
  - [ ] Criar subcomandos para o texto, no caso realce
  - [ ] Criar subcomandos para o texto, no caso cor
  - [ ] Criar subcomandos para o texto, no caso tamanho

### Regras de sintaxe e comandos do TerVisual:
- é obrigatorio usar o ponto e virgula no final de cada comando, além disso, quando você for colocar um subcomando com o comando, coloque dois pontos, por exemplo:
```
escreva: 20;
```
- para cada subcomando, usamos a virgula, por exemplo:

```
texto: 2, o texto está amarelo, cor.yellow
```

- Lista de comandos e suas regras

|Comando|Regras|Para que serve|
|escreva|Não exite uma regra para ele, porém sempre se usa os : e ;| serve para testar o terminal e ver se o código está rodando|
|texto|o seu primeiro subcomando sempre terá que ter um número, para dizer ao sistema quantos subcomandos existem, já o segundo subcomando vai ser obrigatoriamente o texto, sendo os seus comandos até o momento, cor.(palavra cor em inglês) e tamanho (ainda não aceita unidade e somente número)|Serve para colocar o texto da página|
