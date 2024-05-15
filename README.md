# TerceQL
Uma linguagem onde uni a visualização do site e com o banco de dados a partir do python

## Coisas que precisam ser feitas
### Desenvolvendo o arquivo .TV ou TerVisual
- [X] Começar pela parte de criar um comando pro terminal
- [X] Criar o comando para texto
  - [X] Criar subcomandos para o texto, no caso cor
  - [x] Criar subcomandos para o texto, no caso tamanho
  - [x] (Não foi possível) Criar subcomandos para o texto, no caso negrito
  - [x] Criar subcomandos para o texto, no caso italico
  - [x] Criar subcomandos para o texto, no caso para grifar
  - [x] Misturar três subcomandos
  - [x] Misturar quatro subcomandos
  - [x] Misturar cinco subcomandos
  - [X] Misturar seis subcomandos

- [x] Criar um comando que mude de página da web para aplicativo
     
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
|-------|------|---------|
|escreva|Não exite uma regra para ele, porém sempre se usa os : e ;| serve para testar o terminal e ver se o código está rodando|
|texto|o seu primeiro subcomando sempre terá que ter um número, para dizer ao sistema quantos subcomandos existem, já o segundo subcomando vai ser obrigatoriamente o texto, para saber mais, de uma olhada em *regras do subcomando texto*|Serve para colocar o texto da página|




# Regras do comando **texto**
1. Sempre usar o número de subcomandos que você vai utlizar no começo (também conta a parte do texto), além de dar espaço quando for escrever o número depois dos dois pontos
2. Usar sempre virgula e espaço para separar os subcomandos
3. O ponto e vírgula sempre deve vir no final desse comando
4. Os sucomandos existentes são:
    |Nome do subcomando|Para que serve|Código|
    |----|-----|---------|
    |tamanho|Serve para dar o tamanho para a letra e é declarado somente com o número|```texto: 2, tamanho, 10;```|
   |cor|Serve para dar a cor ao texto e é declarado a partir de cor.(cor em inglês)|```texto: 2, cor, cor.yellow;```|
   |italico|Serve para tranformar um texto em italico e é declarado a partir de italico.verdedairo (para acionar) ou italico.falso (para não acionar)|```texto: 2, italico acionado, italico.verdadeiro;```|
   |grifar|Serve para grifar um texto e é declarado a partir de grifar.(cor em inglês)|```texto: 2, grifar, grifar.red;```|
   |font_family|Serve para dar a fonte para o texto e é declarado a partir de familia_font.(nome da fonte)|```texto: 2, font_family, familia_font."Kanit";```|
  
# Regras do comando **modelo**
1. Como os outros comandos, deve sempre usar dois pontos e colocar o subcomandos, além do ponto e virgula no final
2. Esse subcomando só vai ter dois comandos, o app e site, porém é de extrema importancia colocar espaço entre os dois pontos e o subcomando
3. Os sucomandos e suas habilidades são:
    |Nome do subcomando|Para que serve|Código|
    |----|-----|---------|
    |app|Serve para que o interpretador entenda que o código vai ser usado para criar um aplicativo|```modelo: app;```|
   |site|Serve para que o interpretador entenda que o código vai ser usado para criar um site|```modelo: site;```|
