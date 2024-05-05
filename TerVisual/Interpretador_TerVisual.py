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

                #quando não tem nenhum comando
                if int(subcomandos[0]) == 1:
                    #forma padrão de escrever o texto
                    texto = ft.Text(subcomandos[1])
                    pagina.add(texto)

                #quando tem dois comandos
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
                        texto = ft.Text(subcomandos[1])
                        pagina.add(texto)

                #Quando tem três comandos
                elif int(subcomandos[0]) == 3:

                    #Organização dos subcomandos a partir do dois
                    #organização das ordens de cor
                    cor2 = subcomandos[2].split(".")

                    #organização das ordens italicas
                    italico2 = subcomandos[2].split(".")

                    #organização das ordens grifar
                    grifar2 = subcomandos[2].split(".")

                    #organização das ordens fonte
                    familia_fonte2 = subcomandos[2].split(".")

                    #Organização dos subcomandos a partir do três
                    #organização das ordens de cor
                    cor3 = subcomandos[3].split(".")

                    #organização das ordens italicas
                    italico3 = subcomandos[3].split(".")

                    #organização das ordens grifar
                    grifar3 = subcomandos[3].split(".")

                    #organização das ordens fonte
                    familia_fonte3 = subcomandos[3].split(".")

                    #para identificar qual comando o segundo comando
                    if subcomandos[2].isdigit():
                        tipo2 = type(int(subcomandos[2]))
                    else:
                        tipo2 = type(subcomandos[2])
                    
                    #para identificar qual comando o terceiro comando
                    if subcomandos[3].isdigit():
                        tipo3 = type(int(subcomandos[3]))
                    else:
                        tipo3 = type(subcomandos[3])


                    if tipo2 == int:
                        #forma com tamanho de escrever o texto

                        if cor3[0] == "cor":
                            #forma com cor de escrever o texto
                            print(subcomandos)
                            texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1])
                            pagina.add(texto)

                        elif italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True)
                                pagina.add(texto)

                            elif italico3[2] == "falso":
                                 #não tranforma o texto em italico
                                 texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False)
                                 pagina.add(texto)
                    
                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()
                            texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar)
                            pagina.add(texto)
                    
                        elif familia_fonte3[0] == "familia_fonte":
                            #Fonte do texto
                            pagina.theme = ft.Theme(font_family=familia_fonte3[1])
                            texto = ft.Text(subcomandos[1], size=int(subcomandos[2]))
                            pagina.add(texto)
                            
                    elif cor2[0] == "cor":
                            #forma com cor de escrever o texto

                            if tipo3 == int:
                                #forma com tamanho de escrever o texto
                                texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]))
                                pagina.add(texto)
                            
                            if italico3[0] == "italico":
                                if italico3[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=True)
                                    pagina.add(texto)

                                elif italico3[2] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=False)
                                    pagina.add(texto)
                    
                            elif grifar3[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar3[1].upper()
                                texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar)
                                pagina.add(texto)
                    
                            elif familia_fonte3[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte3[1])
                                texto = ft.Text(subcomandos[1], color = cor2[1])
                                pagina.add(texto)
                    
                    elif italico2[0] == "italico":
                            if italico2[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo3 == int:
                                    #forma com tamanho de escrever o texto
                                    texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]))
                                    pagina.add(texto)
                                
                                elif cor3[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], italic=True, color = cor3[1])
                                    pagina.add(texto)
                    
                                elif grifar3[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar3[1].upper()
                                    texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                                elif familia_fonte3[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte3[1])
                                    texto = ft.Text(subcomandos[1], italic=True)
                                    pagina.add(texto)

                            elif italico2[2] == "falso":
                                 #não tranforma o texto em italico

                                if tipo3 == int:
                                    #forma com tamanho de escrever o texto
                                    texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]))
                                    pagina.add(texto)
                                
                                elif cor3[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], italic=False, color = cor3[1])
                                    pagina.add(texto)
                    
                                elif grifar3[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar3[1].upper()
                                    texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                                elif familia_fonte3[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte3[1])
                                    texto = ft.Text(subcomandos[1], italic=False)
                                    pagina.add(texto)
                    
                    elif grifar2[0] == "grifar":
                        #forma com grifar de escrever o texto
                        cor_grifar = grifar2[1].upper()

                        if tipo3 == int:
                            #forma com tamanho de escrever o texto
                            texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[3]))
                            pagina.add(texto)
                        
                        elif cor3[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor3[1])
                                    pagina.add(texto)
                           
                        elif italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico
                                texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=True)
                                pagina.add(texto)

                            elif italico3[2] == "falso":
                                #não tranforma o texto em italico
                                texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=False)
                                pagina.add(texto)
                    
                        elif familia_fonte3[0] == "familia_fonte":
                            #Fonte do texto
                            pagina.theme = ft.Theme(font_family=familia_fonte3[1])
                            texto = ft.Text(subcomandos[1], bgcolor=cor_grifar)
                            pagina.add(texto)
                    
                    elif familia_fonte2[0] == "familia_fonte":
                        # Mudar fonte
                        pagina.theme = ft.Theme(font_family=familia_fonte2[1])

                        if tipo3 == int:
                            #forma com tamanho de escrever o texto
                            print(subcomandos)
                            texto = ft.Text(subcomandos[1], size=int(subcomandos[3]))
                            pagina.add(texto)
                            
                        elif cor3[0] == "cor":
                            #forma com cor de escrever o texto
                            texto = ft.Text(subcomandos[1], color = cor3[1])
                            pagina.add(texto)
                    
                        elif italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico
                                texto = ft.Text(subcomandos[1], italic=True)
                                pagina.add(texto)

                            elif italico3[2] == "falso":
                                 #não tranforma o texto em italico
                                 texto = ft.Text(subcomandos[1], italic=False)
                                 pagina.add(texto)
                    
                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()
                            texto = ft.Text(subcomandos[1], bgcolor=cor_grifar)
                            pagina.add(texto)
                     
                

                            

ft.app(main, view=ft.WEB_BROWSER)
