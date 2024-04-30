import flet as ft
     

def main(pagina):
         
    with open('C:\\Users\\mathe\\OneDrive\\Área de Trabalho\\Criações\\TerceQL\\TerVisual\\text.TV', 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        codigo = linha.split(";")
        for interpretacao in codigo:
            comando = interpretacao.split(": ")
            if comando[0] == "escreva":
                #caso a pessoa queira usar o terminal
                print(comando[1])

            elif comando[0] == "texto":
                #formas da pessoa colocar o texto

                #organização de subcomandos
                subcomandos = comando[1].split(", ")
                print(subcomandos)

                if int(subcomandos[0]) == 1:
                    #forma padrão de escrever o texto
                    texto = ft.Text(subcomandos[1])
                    pagina.add(texto)

                elif int(subcomandos[0]) == 2:
                    #organização das ordens de cor
                    cor = subcomandos[2].split(".")

                    #organização das ordens italicas
                    italico = subcomandos[2].split(".")

                    #organização das ordens grifar
                    grifar = subcomandos[2].split(".")

                    #organização das ordens fonte
                    familia_fonte = subcomandos[2].split(".")

                    print(subcomandos[2].isdigit())

                    #para identificar qual comando o segundo comando
                    if subcomandos[2].isdigit():
                        tipo = type(int(subcomandos[2]))
                    else:
                        tipo = type(subcomandos[2])

                    if tipo == int:
                        #forma com tamanho de escrever o texto
                        print(subcomandos)
                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]))
                        pagina.add(texto)
                            
                    elif cor[0] == "cor":
                            #forma com cor de escrever o texto
                            texto = ft.Text(subcomandos[1], color = cor[1])
                            pagina.add(texto)
                    
                    elif italico[0] == "italico":
                            if italico[1] == "verdadeiro":
                                #tranforma o texto em italico
                                texto = ft.Text(subcomandos[1], italic=True)
                                pagina.add(texto)

                            elif italico[2] == "falso":
                                 #não tranforma o texto em italico
                                 texto = ft.Text(subcomandos[1], italic=False)
                                 pagina.add(texto)
                    
                    elif grifar[0] == "grifar":
                        #forma com grifar de escrever o texto
                        cor_grifar = grifar[1].upper()
                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar)
                        pagina.add(texto)
                    
                    elif familia_fonte[0] == "familia_fonte":
                         pagina.theme = ft.Theme(font_family=familia_fonte[1])
                     
                

                            

ft.app(main, view=ft.WEB_BROWSER)
