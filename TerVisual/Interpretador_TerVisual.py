import flet as ft

def main(pagina):
    codigo_bruto = "escreva: 20; texto: 2, casa alfa, 20"
    codigo = codigo_bruto.split("; ")
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

            #organização das ordens de cor
            cor = subcomandos[2].split(".")

            #para identificar qual comando o segundo comando
            tipo = type(subcomandos[2])

            if int(subcomandos[0]) == 1:
                #forma padrão de escrever o texto
                texto = ft.Text(subcomandos[1])
                pagina.add(texto)

            elif int(subcomandos[0]) == 2:
                if tipo == int:
                    #forma com tamanho de escrever o texto
                    print(subcomandos)
                    texto = ft.Text(subcomandos[1], size=int(subcomandos[2]))
                    pagina.add(texto)
                        
                elif cor[0] == "cor":
                        #forma com cor de escrever o texto
                        texto = ft.Text(subcomandos[1], color = cor[1])
                        pagina.add(texto)

ft.app(main, view=ft.WEB_BROWSER)
        

    
        
