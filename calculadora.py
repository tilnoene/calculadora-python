import math

def verifica_numero(valor):
    try:
        float(valor)
    except ValueError:
        return False
    return True

def par_ou_impar(n):
    if n%2 == 0:
        return True
    else:
        return False

def identifica_print_fracao(a):
    if len(a) == 1:
        print("\n{}\n".format(a[0]))
    else:
        if a[1] > 0:
            print("\n{}/{} - aproximadamente {}\n".format(a[0], a[1], a[0]/a[1]))
        elif a[1] < 0:
            print("\n{}/{} - aproximadamente {}\n".format(a[0]*-1, a[1]*-1, a[0]/a[1]))
        else:
            print("\n{}/{} - aproximadamente {}\n".format(a[0], a[1], 'INDEFINIDO (DIVISÃO POR ZERO)'))

def distancia_dois_pontos(coord):
   return math.sqrt((coord[0]-coord[2])**2+(coord[1]-coord[3])**2)

def ponto_medio(x1, x2):
    ponto_medio = (x1+x2)/2
    print("O ponto médio de {} e {} é: {}".format(x1, x2, ponto_medio), end='')

def equacao_reduzida_da_reta():
    m = float(input("Digite o coeficiente angular: "))
    x = float(input("Digite um ponto X: "))
    y = float(input("Digite um ponto Y: "))

def fatorar(n):
    divisores = []
    fora_da_raiz = 1
    raiz = 1
    i = 2
    
    if n == 1:
        print("√", end='')
        print(n)
        return
        
    while i < (n+1):
        if n%i == 0:
            if divisores.count(i) == 1:
                fora_da_raiz = fora_da_raiz*i
                divisores.remove(i)
            else:
                divisores.append(i)
            n = n//i
        else:
            i += 1
            
    #formando o resultado
    for j in range(len(divisores)):
        raiz = raiz*divisores[j]
        
    
    if raiz == 1:
        print(fora_da_raiz)
        return
    elif fora_da_raiz == 1:
        print("√", end='')
        print(raiz)
        return
    else:
        print(fora_da_raiz, end='')
        print("√", end='')
        print(raiz)
        return

def simplifica_fracao(n, d):
    i = 2
    if n > d:
        limite = n
    else:
        limite = d

    while i < limite:
        if n%i == 0 and d%i == 0:
            n = n//i
            d = d//i
        i += 1

    if d != 0:
        if n%d == 0:
            return [n//d]
        
        return [n, d]
    
def multiplos(n):
    multiplos = []
    for i in range(1, n//2+1):
        if n%i == 0:
            multiplos.append(i)

    return multiplos

def primo(n):
    if len(multiplos(n)) == 1:
        return True
    else:
        return False

def formula_de_bhaskara(a, b, c):
    delta = b**2-4*a*c
    raizes = []
    
    if delta > 0:
        raizes.append((-b+math.sqrt(delta))/(2*a))
        raizes.append((-b-math.sqrt(delta))/(2*a))
    elif delta == 0:
        raizes.append((-b+math.sqrt(delta))/(2*a))
    
    return raizes

def equacao_reta_matriz(x1, y1, x2, y2):
    coef_x = y1-y2
    coef_y = x2-x1
    coef_linear = x1*y2-x2*y1
    equacao_da_reta = ""
    maior = coef_x

    if coef_y > maior:
        maior = coef_y
    if coef_linear > maior:
        maior = coef_linear

    for i in range(2,maior+1):
        if coef_x%i == 0:
            if coef_y%i == 0:
                if coef_linear%i == 0:
                    coef_x = coef_x//i
                    coef_y = coef_y//i
                    coef_linear = coef_linear//i
    
    if coef_x == 1:
        equacao_da_reta += str("x")
    elif coef_x == -1:
        equacao_da_reta += str("- x")
    elif coef_x > 1:
        equacao_da_reta += str("{}x".format(str(coef_x)))
    elif coef_x < -1:
        equacao_da_reta += str("- {}x".format(str(coef_x*-1)))
    
    if len(equacao_da_reta) != 0 and coef_y > 0 and (coef_y != 1 and coef_y != -1):
        equacao_da_reta += str(" + "+str(coef_y)+"y")
    elif len(equacao_da_reta) != 0 and coef_y < 0 and (coef_y != 1 and coef_y != -1):
        equacao_da_reta += str(" - "+str(coef_y*-1)+"y")
    elif len(equacao_da_reta) <= 1 and coef_y < 0 and (coef_y != 1 and coef_y != -1):
        equacao_da_reta += str("- "+str(coef_y*-1)+"y")
    elif len(equacao_da_reta) != 0 and coef_y == 1:
        equacao_da_reta += str(" + y")
    elif len(equacao_da_reta) != 0 and coef_y == -1:
        equacao_da_reta += str(" - y")
    elif len(equacao_da_reta) <= 1 and coef_y == -1:
        equacao_da_reta += str("- y")

    if coef_linear > 0:
        equacao_da_reta += str(" + "+str(coef_linear))
    elif coef_linear < 0:
        equacao_da_reta += str(" - "+str(coef_linear*-1))
        
    equacao_da_reta += " = 0"
    
    return equacao_da_reta

#por em vetor tlvz as variaveis
def area_triangulo_analitica(x1,y1,x2,y2,x3,y3):
    d = x1*y2+y1*x3+x2*y3-x3*y2-y3*x1-x2*y1
    if d < 0:
        d *= -1
    return simplifica_fracao(d,2)

def area_analitica(coord):
    d=0
    for i in range(len(coord[0])-1):
        d+=coord[0][i]*coord[1][i+1]
    d+=coord[0][-1]*coord[1][0]
    for i in range(len(coord[1])-1):
        d-=coord[1][i]*coord[0][i+1]
    d-=coord[1][-1]*coord[0][0]
    if d < 0:
        d*=-1
    return identifica_print_fracao(simplifica_fracao(d,2))

def pontos_alinhados(x1,y1,x2,y2,x3,y3):
    d = area_triangulo_analitica(x1,y1,x2,y2,x3,y3)
    if int(d[0]) == 0:
        return True
    else:
        return False

def coeficiente_angular(x1,y1,x2,y2):
    coef_y = y2-y1
    coef_x = x2-x1
    return simplifica_fracao(coef_y, coef_x)

def equacao_circunferencia(coord):
    if len(coord[1]) == 1:
        raio = coord[1][0]
    else:
        raio = distancia_dois_pontos(coord[0], coord[1])

    equacao_da_circunferencia = ''

    if coord[0][0] != 0:
        if coord[0][0] > 0:
            equacao_da_circunferencia += '(x-'+str(coord[0][0])
        else:
            equacao_da_circunferencia += '(x+'+str(coord[0][0]*-1)
        equacao_da_circunferencia+=')^2+'
    else:
        equacao_da_circunferencia += 'x^2+'

    if coord[0][1] != 0:
        if coord[0][1] > 0:
            equacao_da_circunferencia += '(y-'+str(coord[0][1])
        else:
            equacao_da_circunferencia += '(y+'+str(coord[0][1]*-1)
        equacao_da_circunferencia+=')^2='
    else:
        equacao_da_circunferencia += 'y^2='
        
    return equacao_da_circunferencia+str(raio**2)

def main():
    print("*** Bem vindo a calculadora mais útil do mundo! ***")
    print("")
    print("Funções:")
    print("")
    print("1 - Distância entre dois pontos")
    print("2 - Ponto médio de um segmento")
    print("3 - Fatorar a raiz de um número")
    print("4 - Simplificar uma fração")
    print("5 - Divisores de um número")
    print("6 - Se o número é ou não primo")
    print("7 - Fórmula de Bhaskara / Função Quadrática")
    print("8 - Calcular a equação da reta (por matriz)")
    print("9 - Área de um triângulo com as coordenadas de seus vértices")
    print("10 - Área de um polígono com as coordenadas de seus vértices")
    print("11 - Verificar se os pontos estão alinhados")
    print("12 - Calcular o coeficiente angular de uma reta")
    print("0 - Sair")
    print("")
    escolha = int(input("Opção: "))
    while escolha > 13 or escolha < 0:
        print("")
        print("Essa opção não existe! Tente novamente.")
        print("")
        escolha = int(input("Opção: "))
    print("")
    if escolha == 1:
        coord_distancia = []
        atual_distancia = float(input("Digite o valor de X1: "))
        coord_distancia.append(atual_distancia)
        atual_distancia = float(input("Digite o valor de Y1: "))
        coord_distancia.append(atual_distancia)
        atual_distancia = float(input("Digite o valor de X2: "))
        coord_distancia.append(atual_distancia)
        atual_distancia = float(input("Digite o valor de Y2: "))
        coord_distancia.append(atual_distancia)
        
        print("\n"+str(distancia_dois_pontos(coord_distancia)))
    elif escolha == 2:
        x1 = int(input("Digite um valor para X1/Y1: "))
        x2 = int(input("Digite um valor para X2/Y2: "))
        ponto_medio(x1, x2)
    elif escolha == 3:
        num_raiz = int(input("Digite o número que deseja fatorar: "))
        fatorar(num_raiz)
        print("")
    elif escolha == 4:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado_fracao = simplifica_fracao(numerador, denominador)
        identifica_print_fracao(resultado_fracao)
    elif escolha == 5:
        multiplos_n = int(input("Digite um valor para obter seus divisores: "))
        print(multiplos(multiplos_n))
        #criar um for bonitinho pra printar eles bonitinhos
        
    elif escolha == 6:
        numero_primo = int(input("Digite um número para saber se é ou não primo: "))
        if primo(numero_primo):
            print("\n{} é primo\n".format(numero_primo))
        else:
            print("\n{} não é primo\n".format(numero_primo))

    elif escolha == 7:
        bhaskara_a = int(input("Digite o valor de A: "))
        bhaskara_b = int(input("Digite o valor de B: "))
        bhaskara_c = int(input("Digite o valor de C: "))
        bhaskara_raizes = formula_de_bhaskara(bhaskara_a, bhaskara_b, bhaskara_c)

        if len(bhaskara_raizes) == 0:
            print("\nEsta equação não possui raízes reais.\n")
        elif len(bhaskara_raizes) == 1:
            print("\nEsta equação possui apenas uma raíz, que é {}\n".format(bhaskara_raizes[0]))
        else:
            print("\nA primeira raiz é: {}\nA segunda raiz é: {}\n".format(bhaskara_raizes[0], bhaskara_raizes[1]))
    elif escolha == 8:
        matriz_x1 = int(input("Digite o valor de X1: "))
        matriz_y1 = int(input("Digite o valor de Y1: "))
        matriz_x2 = int(input("Digite o valor de X2: "))
        matriz_y2 = int(input("Digite o valor de Y2: "))
        print("\n"+equacao_reta_matriz(matriz_x1,matriz_y1,matriz_x2,matriz_y2)+"\n")

    elif escolha == 9:
        print("*** ÁREA DO TRIÂNGULO COM AS COORDENADAS DOS VÉRTICES ***\n")
        triangulo_ponto1_x = float(input("Digite o valor de X1: "))
        triangulo_ponto1_y = float(input("Digite o valor de Y1: "))
        triangulo_ponto2_x = float(input("Digite o valor de X2: "))
        triangulo_ponto2_y = float(input("Digite o valor de Y2: "))
        triangulo_ponto3_x = float(input("Digite o valor de X3: "))
        triangulo_ponto3_y = float(input("Digite o valor de Y3: "))

        identifica_print_fracao(area_triangulo_analitica(triangulo_ponto1_x, triangulo_ponto1_y,
                                                  triangulo_ponto2_x, triangulo_ponto2_y,
                                                  triangulo_ponto3_x, triangulo_ponto3_y))
                
    elif escolha == 10:
        conta_lados = 1
        coordenadas_n_lados = [[],[]]
        coordenadas_n_lados_x = 0
        coordenadas_n_lados_y = 0

        while len(coordenadas_n_lados[0]) < 3:
            coordenadas_n_lados_x = input("Digite o valor de X{}: ".format(conta_lados))
            while verifica_numero(coordenadas_n_lados_x) == False:
                coordenadas_n_lados_x = input("ERRO! Digite o valor de X{}: ".format(conta_lados))
            coordenadas_n_lados[0].append(float(coordenadas_n_lados_x))

            coordenadas_n_lados_y = input("Digite o valor de Y{}: ".format(conta_lados))
            while verifica_numero(coordenadas_n_lados_y) == False:
                coordenadas_n_lados_y = input("ERRO! Digite o valor de Y{}: ".format(conta_lados))
            coordenadas_n_lados[1].append(float(coordenadas_n_lados_y))
            conta_lados += 1
            
        while verifica_numero(coordenadas_n_lados_x):
            coordenadas_n_lados_x = input("Digite o valor de X{}: ".format(conta_lados))
            if verifica_numero(coordenadas_n_lados_x):
                coordenadas_n_lados[0].append(float(coordenadas_n_lados_x))
                coordenadas_n_lados_y = input("Digite o valor de Y{}: ".format(conta_lados))
                while verifica_numero(coordenadas_n_lados_y) == False:
                    coordenadas_n_lados_y = input("ERRO! Digite o valor de Y{}: ".format(conta_lados))
                coordenadas_n_lados[1].append(float(coordenadas_n_lados_y))
            conta_lados += 1
        area_analitica(coordenadas_n_lados)
        print("polígono de {} lados".format(conta_lados-2))
        
    elif escolha == 11:
        alinhados_ponto1_x = int(input("Digite o valor de X1: "))
        alinhados_ponto1_y = int(input("Digite o valor de Y1: "))
        alinhados_ponto2_x = int(input("Digite o valor de X2: "))
        alinhados_ponto2_y = int(input("Digite o valor de Y2: "))
        alinhados_ponto3_x = int(input("Digite o valor de X3: "))
        alinhados_ponto3_y = int(input("Digite o valor de Y3: "))

        if pontos_alinhados(alinhados_ponto1_x,alinhados_ponto1_y,
                            alinhados_ponto2_x, alinhados_ponto2_y,
                            alinhados_ponto3_x, alinhados_ponto3_y):
            print("\nEstão alinhados\n")
        else:
            print("\nNão estão alinhados\n")
    elif escolha == 12:
        print("*** COEFICIENTE ANGULAR ***\n")
        coef_angular_x1 = int(input("Digite o valor de X1: "))
        coef_angular_y1 = int(input("Digite o valor de Y1: "))
        coef_angular_x2 = int(input("Digite o valor de X2: "))
        coef_angular_y2 = int(input("Digite o valor de X2: "))
        coef_angular_resultado = coeficiente_angular(coef_angular_x1,coef_angular_y1,coef_angular_x2,coef_angular_y2)
        identifica_print_fracao(coef_angular_resultado)
        
    elif escolha == 0:
        pass
    else:
        print("Essa opção não existe! Tente novamente.")

def iniciar():
    main();
    choice = int(input("\n\nDeseja utilizar a calculadora novamente?\n1 - Sim\n2 - Não\n\nEscolha: "))
    while choice == 1:
        main();
        choice = int(input("\n\nDeseja utilizar a calculadora novamente?\n1 - Sim\n2 - Não\n\nEscolha: "))
    print("\nEncerrando...\n")
    pass

iniciar()
