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

                            elif italico[1] == "falso":
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

                            elif italico3[1] == "falso":
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

                                elif italico3[1] == "falso":
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

                            elif italico2[1] == "falso":
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

                            elif italico3[1] == "falso":
                                 #não tranforma o texto em italico
                                 texto = ft.Text(subcomandos[1], italic=False)
                                 pagina.add(texto)
                    
                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()
                            texto = ft.Text(subcomandos[1], bgcolor=cor_grifar)
                            pagina.add(texto)

                #Quando tem quatro comandos
                elif int(subcomandos[0]) == 4:
                    
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

                    #Organização dos subcomandos a partir do quatro
                    #organização das ordens de cor
                    cor4 = subcomandos[4].split(".")

                    #organização das ordens italicas
                    italico4 = subcomandos[4].split(".")

                    #organização das ordens grifar
                    grifar4 = subcomandos[4].split(".")

                    #organização das ordens fonte
                    familia_fonte4 = subcomandos[4].split(".")

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
                    
                    #para identificar qual comando o quarto comando
                    if subcomandos[4].isdigit():
                        tipo4 = type(int(subcomandos[4]))
                    else:
                        tipo4 = type(subcomandos[4])
                    
                    if tipo2 == int:
                        #forma com tamanho de escrever o texto

                        if cor3[0] == "cor":
                            #forma com cor de escrever o texto
                        
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], italic=False)
                                    pagina.add(texto)
                    
                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], bgcolor=cor_grifar)
                                pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1])
                                pagina.add(texto)
                                

                        elif italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor4[1])
                                    pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True)
                                    pagina.add(texto)

                            elif italico3[1] == "falso":
                                #não tranforma o texto em italico

                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False, color = cor4[1])
                                    pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False, bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte3[1])
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False)
                                    pagina.add(texto)
                    
                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()

                            if cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, color = cor4[1])
                                    pagina.add(texto)
                            
                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=False)
                                    pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar)
                                pagina.add(texto)
                    
                        elif familia_fonte3[0] == "familia_fonte":
                            #Fonte do texto
                            pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                            if cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor4[1])
                                    pagina.add(texto)
                            
                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False)
                                    pagina.add(texto)
                            
                            elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                    elif cor2[0] == "cor":
                        #forma com cor de escrever o texto

                        if tipo3 == int:
                            #forma com tamanho de escrever o texto

                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), italic=False)
                                    pagina.add(texto)

                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()
                                texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3], bgcolor=cor_grifar))
                                pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]))
                                pagina.add(texto)
                                
                        if italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, size=int(subcomandos[4]))
                                    pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=True)
                                    pagina.add(texto)

                            elif italico3[1] == "falso":
                                #não tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, size=int(subcomandos[4]))
                                    pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=False)
                                    pagina.add(texto)
                    
                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()

                            if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, size=int(subcomandos[4]))
                                    pagina.add(texto)
                            
                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=False)
                                    pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar)
                                pagina.add(texto)
                    
                        elif familia_fonte3[0] == "familia_fonte":
                            #Fonte do texto
                            pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                            if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[4]))
                                    pagina.add(texto)
                            
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=True)
                                    pagina.add(texto)

                                elif italico4[2] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor2[1], italic=False)
                                    pagina.add(texto)
                            
                            elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar)
                                    pagina.add(texto)

                    elif italico2[0] == "italico":
                            if italico2[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo3 == int:
                                    #forma com tamanho de escrever o texto

                                    if cor4[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), color = cor4[1])
                                        pagina.add(texto)
                                    
                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                        texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]))
                                        pagina.add(texto)
                                
                                elif cor3[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], size=int(subcomandos[4]))
                                        pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                        texto = ft.Text(subcomandos[1], italic=True, color = cor3[1])
                                        pagina.add(texto)
                    
                                elif grifar3[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar3[1].upper()

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, size=int(subcomandos[4]))
                                        pagina.add(texto)
                                    
                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, color = cor4[1])
                                        pagina.add(texto)
                                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                        texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                elif familia_fonte3[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[4]))
                                        pagina.add(texto)
                                    
                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=True, color = cor4[1])
                                        pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)

                            elif italico2[1] == "falso":
                                 #não tranforma o texto em italico

                                if tipo3 == int:
                                    #forma com tamanho de escrever o texto

                                    if cor4[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), color = cor4[1])
                                        pagina.add(texto)
                                    
                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                        texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]))
                                        pagina.add(texto)
                                
                                elif cor3[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], size=int(subcomandos[4]))
                                        pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                        texto = ft.Text(subcomandos[1], italic=False, color = cor3[1])
                                        pagina.add(texto)
                    
                                elif grifar3[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar3[1].upper()

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, size=int(subcomandos[4]))
                                        pagina.add(texto)
                                    
                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, color = cor4[1])
                                        pagina.add(texto)
                                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                        texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                elif familia_fonte3[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[4]))
                                        pagina.add(texto)
                                    
                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=False, color = cor4[1])
                                        pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)

                    elif grifar2[0] == "grifar":
                        #forma com grifar de escrever o texto
                        cor_grifar = grifar2[1].upper()

                        if tipo3 == int:
                            #forma com tamanho de escrever o texto

                            if cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[3]), color = cor4[1])
                                    pagina.add(texto)

                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[3]), italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[3]), italic=False)
                                    pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[3]))
                                pagina.add(texto)

                        if cor3[0] == "cor":
                            #forma com cor de escrever o texto

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto
                                print(subcomandos)
                                texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor3[1], size=int(subcomandos[4]))
                                pagina.add(texto)
                        
                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor3[1], italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor3[1], italic=False)
                                    pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor3[1])
                                pagina.add(texto)
                        
                        if italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=True, size=int(subcomandos[4]))
                                    pagina.add(texto)
                                
                                elif cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=True, color = cor4[1])
                                    pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=True)
                                    pagina.add(texto)

                            elif italico3[1] == "falso":
                                #não tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=False, size=int(subcomandos[4]))
                                    pagina.add(texto)
                    
                                elif cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=False, color = cor4[1])
                                    pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=False)
                                    pagina.add(texto)
                        
                        elif familia_fonte3[0] == "familia_fonte":
                            #Fonte do texto
                            pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[4]))
                                pagina.add(texto)
                                    
                            elif cor4[0] == "cor":
                                #forma com cor de escrever o texto
                                print(subcomandos)
                                texto = ft.Text(subcomandos[1], color = cor4[1])
                                pagina.add(texto)

                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], italic=False)
                                    pagina.add(texto)
                    
                    elif familia_fonte2[0] == "familia_fonte":
                        # Mudar fonte
                        pagina.theme = ft.Theme(font_family=familia_fonte2[1])

                        if tipo3 == int:
                            #forma com tamanho de escrever o texto

                            if cor4[0] == "cor":
                                #forma com cor de escrever o texto
                                print(subcomandos)
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), color = cor4[1])
                                pagina.add(texto)

                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), italic=False)
                                    pagina.add(texto)

                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[3], bgcolor=cor_grifar))
                                pagina.add(texto)
                        
                        if cor3[0] == "cor":
                            #forma com cor de escrever o texto

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto
                                print(subcomandos)
                                texto = ft.Text(subcomandos[1], color = cor3[1], size=int(subcomandos[4]))
                                pagina.add(texto)
                        
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor3[1], italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], color = cor3[1], italic=False)
                                    pagina.add(texto)
                    
                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()
                                texto = ft.Text(subcomandos[1], color = cor3[1], bgcolor=cor_grifar)
                                pagina.add(texto)
                        
                        if italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[4]))
                                    pagina.add(texto)
                                
                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], italic=True, color = cor4[1])
                                    pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar)
                                    pagina.add(texto)

                            elif italico3[1] == "falso":
                                #não tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[4]))
                                    pagina.add(texto)
                                
                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], italic=False, color = cor4[1])
                                    pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()
                                    texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar)
                                    pagina.add(texto)

                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto
                                texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[4]))
                                pagina.add(texto)
                                    
                            elif cor4[0] == "cor":
                                #forma com cor de escrever o texto
                                print(subcomandos)
                                texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor4[1])
                                pagina.add(texto)
                            
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=True)
                                    pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=False)
                                    pagina.add(texto)

                #Quando tem cinco comandos
                elif int(subcomandos[0]) == 5:
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

                    #Organização dos subcomandos a partir do quatro
                    #organização das ordens de cor
                    cor4 = subcomandos[4].split(".")

                    #organização das ordens italicas
                    italico4 = subcomandos[4].split(".")

                    #organização das ordens grifar
                    grifar4 = subcomandos[4].split(".")

                    #organização das ordens fonte
                    familia_fonte4 = subcomandos[4].split(".")

                    #Organização dos subcomandos a partir do cinco
                    #organização das ordens de cor
                    cor5 = subcomandos[5].split(".")

                    #organização das ordens italicas
                    italico5 = subcomandos[5].split(".")

                    #organização das ordens grifar
                    grifar5 = subcomandos[5].split(".")

                    #organização das ordens fonte
                    familia_fonte5 = subcomandos[5].split(".")

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
                    
                    #para identificar qual comando o quarto comando
                    if subcomandos[4].isdigit():
                        tipo4 = type(int(subcomandos[4]))
                    else:
                        tipo4 = type(subcomandos[4])
                    
                    #para identificar qual comando o quinto comando
                    if subcomandos[5].isdigit():
                        tipo5 = type(int(subcomandos[5]))
                    else:
                        tipo5 = type(subcomandos[5])
                    
                    if tipo2 == int:
                        #forma com tamanho de escrever o texto

                        if cor3[0] == "cor":
                            #forma com cor de escrever o texto
                        
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor3[1])
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False, color = cor3[1])
                                        pagina.add(texto)
                    
                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)

                                elif familia_fonte5[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], bgcolor=cor_grifar)
                                    pagina.add(texto)

                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], italic=False)
                                        pagina.add(texto)
                                
                                if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor3[1], bgcolor=cor_grifar)
                                        pagina.add(texto)
                                

                        elif italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor4[1], bgcolor=cor_grifar)
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor4[1])
                                        pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar, color = cor5[1])
                                        pagina.add(texto)

                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)
                                    
                                    elif cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor5[1])
                                        pagina.add(texto)


                            elif italico3[1] == "falso":
                                #não tranforma o texto em italico

                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor4[1], bgcolor=cor_grifar)
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor4[1])
                                        pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar, color = cor5[1])
                                        pagina.add(texto)

                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)
                                    
                                    elif cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor5[1])
                                        pagina.add(texto)
                    

                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()

                            if cor4[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if italico5[0] == "italico":
                                        if italico5[1] == "verdadeiro":
                                            #tranforma o texto em italico
                                            texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, color = cor4[1], italic=True)
                                            pagina.add(texto)

                                        elif italico5[1] == "falso":
                                            #não tranforma o texto em italico
                                            texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, color = cor4[1], italic=False)
                                            pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor4[1], bgcolor=cor_grifar)
                                        pagina.add(texto)

                            
                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=True, color = cor5[1])
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=False, color = cor5[1])
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])
                                texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar)
                                pagina.add(texto)

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)
                                
                                elif cor5[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, color = cor5[1])
                                    pagina.add(texto)

                    
                        elif familia_fonte3[0] == "familia_fonte":
                            #Fonte do texto
                            pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                            if cor4[0] == "cor":
                                #forma com cor de escrever o texto

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor4[1], italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor4[1], italic=False)
                                        pagina.add(texto)
                                    
                                elif grifar5[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar5[1].upper()
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), color = cor4[1], bgcolor=cor_grifar)
                                    pagina.add(texto)
                            
                            
                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, color = cor5[1])
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False, color = cor5[1])
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)
                            
                            elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, color = cor5[1])
                                        pagina.add(texto)
                                    
                                    if italico5[0] == "italico":
                                        if italico5[1] == "verdadeiro":
                                            #tranforma o texto em italico
                                            texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=True)
                                            pagina.add(texto)

                                        elif italico5[1] == "falso":
                                            #não tranforma o texto em italico
                                            texto = ft.Text(subcomandos[1], size=int(subcomandos[2]), bgcolor=cor_grifar, italic=False)
                                            pagina.add(texto)

                    elif cor2[0] == "cor":
                        #forma com cor de escrever o texto

                        if tipo3 == int:
                            #forma com tamanho de escrever o texto

                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3], italic=True, bgcolor=cor_grifar))
                                        pagina.add(texto)

                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), italic=True)
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3], italic=False, bgcolor=cor_grifar))
                                        pagina.add(texto)

                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), italic=False)
                                        pagina.add(texto)


                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)
                                
                                elif familia_fonte5[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                    texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), bgcolor=cor_grifar)
                                    pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3]), italic=False)
                                        pagina.add(texto)
                                
                                elif grifar5[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar5[1].upper()
                                    texto = ft.Text(subcomandos[1], color = cor2[1], size=int(subcomandos[3], bgcolor=cor_grifar))
                                    pagina.add(texto)
                                

                        if italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, size=int(subcomandos[4], bgcolor=cor_grifar))
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, size=int(subcomandos[4]))
                                        pagina.add(texto)   
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)  
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)

                            elif italico3[1] == "falso":
                                #não tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto

                                    if grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, size=int(subcomandos[4], bgcolor=cor_grifar))
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, size=int(subcomandos[4]))
                                        pagina.add(texto)   
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)  
                    
                                elif familia_fonte4[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, size=int(subcomandos[4]), italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, size=int(subcomandos[4]), italic=False)
                                        pagina.add(texto)

                                elif familia_fonte5[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, size=int(subcomandos[4]))
                                    pagina.add(texto)
                            
                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=True, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=False, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif familia_fonte5[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)
                    
                            elif familia_fonte4[0] == "familia_fonte":
                                #Fonte do texto
                                pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                if tipo5 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, size=int(subcomandos[5]))
                                    pagina.add(texto)

                                elif italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)
                    
                        elif familia_fonte3[0] == "familia_fonte":
                            #Fonte do texto
                            pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, size=int(subcomandos[4]))
                                        pagina.add(texto)

                                    elif italico5[2] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, size=int(subcomandos[4]))
                                        pagina.add(texto)
                            
                                elif grifar5[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar5[1].upper()
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, size=int(subcomandos[4]))
                                    pagina.add(texto)

                            
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)

                                elif italico4[2] == "falso":
                                    #não tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)
                            
                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()
                                texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar)
                                pagina.add(texto)

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)

                                    elif italico5[2] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor2[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)
                                
                                elif tipo5 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], color = cor2[1], bgcolor=cor_grifar, size=int(subcomandos[5]))
                                    pagina.add(texto)

                    elif italico2[0] == "italico":
                            if italico2[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo3 == int:
                                    #forma com tamanho de escrever o texto

                                    if cor4[0] == "cor":
                                        #forma com cor de escrever o texto

                                        if grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), color = cor4[1], bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), color = cor4[1])
                                            pagina.add(texto)
                                    
                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), bgcolor=cor_grifar, color = cor5[1])
                                            pagina.add(texto)

                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), color = cor5[1])
                                            pagina.add(texto)

                                        if grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[3]), bgcolor=cor_grifar)
                                            pagina.add(texto)
                                
                                elif cor3[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto

                                        if grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], size=int(subcomandos[4]), bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], size=int(subcomandos[4]))
                                            pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], bgcolor=cor_grifar, size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor3[1], bgcolor=cor_grifar)
                                            pagina.add(texto)

                                elif grifar3[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar3[1].upper()

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, size=int(subcomandos[4]), color = cor5[1])
                                            pagina.add(texto)
                                        
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, size=int(subcomandos[4]))
                                            pagina.add(texto)
                                    
                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, color = cor4[1], size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, color = cor4[1])
                                            pagina.add(texto)
                                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, color = cor5[1])
                                            pagina.add(texto)
                    
                                elif familia_fonte3[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[4]), color = cor5[1])
                                            pagina.add(texto)

                                        elif grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[4]), bgcolor=cor_grifar)
                                            pagina.add(texto)

                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor4[1], size=int(subcomandos[5]))
                                            pagina.add(texto)

                                        elif grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=True, color = cor4[1], bgcolor=cor_grifar)
                                            pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, color = cor5[1])
                                            pagina.add(texto)

                            elif italico2[1] == "falso":
                                 #não tranforma o texto em italico

                                if tipo3 == int:
                                    #forma com tamanho de escrever o texto

                                    if cor4[0] == "cor":
                                        #forma com cor de escrever o texto

                                        if grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), color = cor4[1], bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), color = cor4[1])
                                            pagina.add(texto)
                                    
                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), bgcolor=cor_grifar, color = cor5[1])
                                            pagina.add(texto)

                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), color = cor5[1])
                                            pagina.add(texto)

                                        if grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[3]), bgcolor=cor_grifar)
                                            pagina.add(texto)
                                
                                elif cor3[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto

                                        if grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], size=int(subcomandos[4]), bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], size=int(subcomandos[4]))
                                            pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], bgcolor=cor_grifar, size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], bgcolor=cor_grifar)
                                            pagina.add(texto)
                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor3[1], bgcolor=cor_grifar)
                                            pagina.add(texto)

                                elif grifar3[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar3[1].upper()

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, size=int(subcomandos[4]), color = cor5[1])
                                            pagina.add(texto)
                                        
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, size=int(subcomandos[4]))
                                            pagina.add(texto)
                                    
                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, color = cor4[1], size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif familia_fonte5[0] == "familia_fonte":
                                            #Fonte do texto
                                            pagina.theme = ft.Theme(font_family=familia_fonte5[1])
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, color = cor4[1])
                                            pagina.add(texto)
                                    
                                    elif familia_fonte4[0] == "familia_fonte":
                                        #Fonte do texto
                                        pagina.theme = ft.Theme(font_family=familia_fonte4[1])

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, color = cor5[1])
                                            pagina.add(texto)
                    
                                elif familia_fonte3[0] == "familia_fonte":
                                    #Fonte do texto
                                    pagina.theme = ft.Theme(font_family=familia_fonte3[1])

                                    if tipo4 == int:
                                        #forma com tamanho de escrever o texto

                                        if cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[4]), color = cor5[1])
                                            pagina.add(texto)

                                        elif grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[4]), bgcolor=cor_grifar)
                                            pagina.add(texto)

                                    elif cor4[0] == "cor":
                                        #forma com cor de escrever o texto

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor4[1], size=int(subcomandos[5]))
                                            pagina.add(texto)

                                        elif grifar5[0] == "grifar":
                                            #forma com grifar de escrever o texto
                                            cor_grifar = grifar5[1].upper()
                                            texto = ft.Text(subcomandos[1], italic=False, color = cor4[1], bgcolor=cor_grifar)
                                            pagina.add(texto)

                                    elif grifar4[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar4[1].upper()

                                        if tipo5 == int:
                                            #forma com tamanho de escrever o texto
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                            pagina.add(texto)
                                        
                                        elif cor5[0] == "cor":
                                            #forma com cor de escrever o texto
                                            print(subcomandos)
                                            texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, color = cor5[1])
                                            pagina.add(texto)

                    elif familia_fonte2[0] == "familia_fonte":
                        # Mudar fonte
                        pagina.theme = ft.Theme(font_family=familia_fonte2[1])

                        if tipo3 == int:
                            #forma com tamanho de escrever o texto

                            if cor4[0] == "cor":
                                #forma com cor de escrever o texto

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), color = cor4[1], italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), color = cor4[1], italic=False)
                                        pagina.add(texto)

                                elif grifar5[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar5[1].upper()
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), color = cor4[1], bgcolor=cor_grifar)
                                    pagina.add(texto)

                            elif italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), italic=True, color = cor5[1])
                                        pagina.add(texto)

                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), italic=False, color = cor5[1])
                                        pagina.add(texto)

                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)

                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()

                                if cor5[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), bgcolor=cor_grifar, color = cor5[1])
                                    pagina.add(texto)    
                                
                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], size=int(subcomandos[3]), bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)
                        
                        elif cor3[0] == "cor":
                            #forma com cor de escrever o texto

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto

                                if italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor3[1], size=int(subcomandos[4]), italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor3[1], size=int(subcomandos[4]), italic=False)
                                        pagina.add(texto)
                    
                                elif grifar5[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar5[1].upper()
                                    texto = ft.Text(subcomandos[1], color = cor3[1], size=int(subcomandos[4]), bgcolor=cor_grifar)
                                    pagina.add(texto)
                        
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor3[1], italic=True, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor3[1], italic=True, bgcolor=cor_grifar)
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], color = cor3[1], italic=False, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], color = cor3[1], italic=False, bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                            elif grifar4[0] == "grifar":
                                #forma com grifar de escrever o texto
                                cor_grifar = grifar4[1].upper()

                                if tipo5 == int:
                                    #forma com tamanho de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], color = cor3[1], bgcolor=cor_grifar, size=int(subcomandos[5]))
                                    pagina.add(texto)

                                elif italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor3[1], bgcolor=cor_grifar, italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], color = cor3[1], bgcolor=cor_grifar, italic=False)
                                        pagina.add(texto)
                        
                        elif italico3[0] == "italico":
                            if italico3[1] == "verdadeiro":
                                #tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[4]), color = cor5[1])
                                        pagina.add(texto)
                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=True, size=int(subcomandos[4]), bgcolor=cor_grifar)
                                        pagina.add(texto)
                                
                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=True, color = cor4[1], size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=True, color = cor4[1], bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                        pagina.add(texto)

                                    elif cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=True, bgcolor=cor_grifar, color = cor5[1])
                                        pagina.add(texto)

                            elif italico3[1] == "falso":
                                #não tranforma o texto em italico

                                if tipo4 == int:
                                    #forma com tamanho de escrever o texto

                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[4]), color = cor5[1])
                                        pagina.add(texto)
                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=False, size=int(subcomandos[4]), bgcolor=cor_grifar)
                                        pagina.add(texto)
                                
                                if cor4[0] == "cor":
                                    #forma com cor de escrever o texto

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=False, color = cor4[1], size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    elif grifar5[0] == "grifar":
                                        #forma com grifar de escrever o texto
                                        cor_grifar = grifar5[1].upper()
                                        texto = ft.Text(subcomandos[1], italic=False, color = cor4[1], bgcolor=cor_grifar)
                                        pagina.add(texto)
                    
                                elif grifar4[0] == "grifar":
                                    #forma com grifar de escrever o texto
                                    cor_grifar = grifar4[1].upper()

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, size=int(subcomandos[5]))
                                        pagina.add(texto)

                                    elif cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], italic=False, bgcolor=cor_grifar, color = cor5[1])
                                        pagina.add(texto)

                        elif grifar3[0] == "grifar":
                            #forma com grifar de escrever o texto
                            cor_grifar = grifar3[1].upper()

                            if tipo4 == int:
                                #forma com tamanho de escrever o texto

                                if cor5[0] == "cor":
                                    #forma com cor de escrever o texto
                                    print(subcomandos)
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[4]), color = cor5[1])
                                    pagina.add(texto)
                            
                                elif italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[4]), italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, size=int(subcomandos[4]), italic=False)
                                        pagina.add(texto)
                                    
                            elif cor4[0] == "cor":
                                #forma com cor de escrever o texto

                                if tipo5 == int:
                                    #forma com tamanho de escrever o texto
                                    texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor4[1], size=int(subcomandos[5]))
                                    pagina.add(texto)
                                
                                elif italico5[0] == "italico":
                                    if italico5[1] == "verdadeiro":
                                        #tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor4[1], italic=True)
                                        pagina.add(texto)

                                    elif italico5[1] == "falso":
                                        #não tranforma o texto em italico
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, color = cor4[1], italic=False)
                                        pagina.add(texto)
                            
                            if italico4[0] == "italico":
                                if italico4[1] == "verdadeiro":
                                    #tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=True, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=True, color = cor5[1])
                                        pagina.add(texto)

                                elif italico4[1] == "falso":
                                    #não tranforma o texto em italico

                                    if tipo5 == int:
                                        #forma com tamanho de escrever o texto
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=False, size=int(subcomandos[5]))
                                        pagina.add(texto)
                                    
                                    if cor5[0] == "cor":
                                        #forma com cor de escrever o texto
                                        print(subcomandos)
                                        texto = ft.Text(subcomandos[1], bgcolor=cor_grifar, italic=False, color = cor5[1])
                                        pagina.add(texto)


ft.app(main, view=ft.WEB_BROWSER)
