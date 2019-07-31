import matplotlib.pyplot as plt
import os.path
import csv
from matplotlib import style
style.use('bmh')


def busca_1(ano,mod,gen):#--------------------------BUSCA 1 ------------------------------------------------------    
    arq = open('vgsales.csv', 'r')
    lista=[]                                                     
    L=[]                                                         
    media=[0,0,0,0,0,0,0,0,0,0,0,0]                               
    genero = [0,0,0,0,0,0,0,0,0,0,0,0]
    nomes=['Action','Role-Playing', 'Shooter', 'Platform', 'Sports','Simulation',
           'Fighting','Misc', 'Adventure','Racing', 'Puzzle','Strategy']
    for linha in arq:
        linha=linha.replace('\n', '')
        lista.append(linha.split(','))
    arq.close()
    from decimal import Decimal as d
    for i in range (1,len(lista)):
        L=lista[i]
        d(L[10])
        L[10]==float(L[10])
        if L[4]=='Action'and L[3]== ano:  
            genero[0] +=d(L[10])        
            media[0] += 1
            
        if L[4]=='Role-Playing'and L[3]== ano:
            genero[1] +=d(L[10])  
            media[1] += 1
        if L[4]=='Shooter'and L[3]== ano:
            genero[2] +=d(L[10]) 
            media[2] += 1
        if L[4]=='Platform'and L[3]== ano:
            genero[3] +=d(L[10]) 
            media[3] += 1
        if L[4]=='Sports'and L[3]== ano:
            genero[4] +=d(L[10])  
            media[4] += 1
        if L[4]=='Simulation'and L[3]== ano:
            genero[5] +=d(L[10])  
            media[5] += 1
        if L[4]=='Fighting'and L[3]== ano:
            genero[6] +=d(L[10])  
            media[6] += 1
        if L[4]=='Misc'and L[3]== ano:
            genero[7] +=d(L[10])  
            media[7] += 1
        if L[4]=='Adventure'and L[3]== ano:
            genero[8] +=d(L[10])  
            media[8] += 1
        if L[4]=='Racing'and L[3]== ano:
            genero[9] +=d(L[10])  
            media[9] += 1
        if L[4]=='Puzzle'and L[3]== ano:
            genero[10] +=d(L[10]) 
            media[10] += 1
        if L[4]=='Strategy'and L[3]== ano:
            genero[11] +=d(L[10])  
            media[11] += 1

    for i in range(12):
        if genero[i]!=0:
            genero[i]= genero[i]/media[i]

    if mod == "1":
        for i in range(12):
            if nomes[i]==gen:
                return(genero[i])
            
    #-------gera hitorico----
    x=''
    y=''
    for i in range(len(nomes)):
        if i != 0:
            x +=','
            y +=','   
        x += str(nomes[i])
        y += str(genero[i])
        
    h='busca_1,'+'Ano:'+ano+'|'+x+'|'+y+'|'+'\n'
    escrever(h)

    #-------------------
    return(graphics(nomes,genero,ano))

def graphics(nomes,lista,ano):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    x = nomes
    y = lista
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation (45)
    plt.bar(x,y)
    plt.xlabel('Genero')
    plt.ylabel('Média Global')
    plt.title('Média X Gênero ano: {0}'.format(ano))
    plt.show()

#----------------------------------------BUSCA 2 ---------------------------------------------------------
def busca_2(ano,gen):
    arq = open('vgsales.csv', 'r')
    dic={'':0,' ':0,'  ':0,'    ':0,'     ':0,'      ':0,
         '       ':0,'        ':0,'         ':0,'          ':0,}#nomes e numeros
    dic1=[]#numeros
    dic2=[]#nomes
    lista=[]                                                   
    for linha in arq:
        linha=linha.replace('\n', '')
        lista.append(linha.split(','))
    arq.close()
    
    for i in range (1,len(lista)):
        L=lista[i]
        if L[4]==gen and L[3]== ano:
            if L[5] in dic: #verifica se ja tem uma chave no dicionário
                dic[L[5]]+= 1
            else: #escreve uma nova chave no dicionário
                dic.update({L[5]:1})
               
    dic1= sorted(dic.values())
    dic1.reverse()
    for i in dic1:#numeros
        for j in dic:#nomes

            if dic[j] == i:
                dic2.append(j)
                dic[j]=-1

    nome=[]
    publicacoes=[]
    for i in range(10):
        nome.append(dic2[i])
        publicacoes.append(dic1[i])
    #---gera hitorico-----
    x=''
    y=''
    for i in range(len(nome)):
        if i != 0:
            x +=','
            y +=','   
        x += str(nome[i])
        y += str(publicacoes[i])
        
    h='busca_2,'+'Ano:'+ano+',Gênero:'+gen+'|'+x+'|'+y+'|'+'\n'
    escrever(h)


    #-----------------
    return(graphics2(nome,publicacoes,ano,gen))


def graphics2(dic2,dic1,ano,gen):
    x = dic2
    y = dic1

    plt.barh(x,y)
    plt.xlabel('Genero')
    plt.ylabel('Empresas')
    plt.title('Empresas X Publicações ano {0} Genero {1}'.format(ano,gen))
    plt.subplots_adjust(left = 0.22, bottom = 0.09)
    plt.show()
  
#-------------------------------------BUSCA 3----------------------------------
def busca_3 (regiao):
    def pegarConsoles():
        console = []
        with open ('vgsales.csv', 'r') as vendasArquivo:
            leitor_csv = csv.reader(vendasArquivo)
            for line in leitor_csv: 
                
                if(line[2]) not in console:
                    console.append(line[2]) #add a plataforma
            del(console[0]) #deleta a palavra plataform
        vendasArquivo.close()
        return console #lista de todos os platadormas existentes no banco de dado


    
    with open ('vgsales.csv', 'r') as vendasArquivo:
        leitor_csv = csv.reader(vendasArquivo)
        console = pegarConsoles()

        #Constroi os listas com 'n' zeros, sendo 'n' a quantidade de consoles
        somatorioValorVendasConsole = [0 for k in range(len(console))]
        quantidadeDeVendasConsole = [0 for k in range(len(console))]
        mediaDeCadaConsole = [0 for k in range(len(console))]

        for line in leitor_csv: #Percorre todas as linhas do arquivo
            meuContador = 0 #Mesma coisa que id ou indice
            for k in console: #k serA cada um dos consoles
                if(line[2] == k):
                    somatorioValorVendasConsole[meuContador] += float(line[regiao])
                    quantidadeDeVendasConsole[meuContador] += 1
                    break # So precisa percorrer ate que o primeiro console apareca
                meuContador += 1 #contador utilizado para resgate por indice

        meuContador = 0
        for k in console: #calcula as mEdias de cada um dos consoles de acordo com a regiao
            if(float(somatorioValorVendasConsole[meuContador]) != 0 or float(quantidadeDeVendasConsole[meuContador]) != 0):
                mediaDeCadaConsole[meuContador] = float(somatorioValorVendasConsole[meuContador]) / float(quantidadeDeVendasConsole[meuContador])
            else: #para nao dividir por zero
                mediaDeCadaConsole[meuContador] = 0
            meuContador += 1

        top10medias = []
        top10console = []
        top10med=[]
        top10con=[]
        contador = 0
        top10={}
        if regiao == 6:
            regiao='NA'
        if regiao == 7:
            regiao='EU'
        if regiao == 8:
            regiao='JP'
        if regiao == 9:
            regiao='Other'
        
        for k in range(32):
            top10medias.append(mediaDeCadaConsole[contador])
            top10con.append(console[contador])
            contador += 1

        for i in range(32):
            top10.update({top10con[i]:top10medias[i]})
        top10medias = sorted(top10.values())
        top10medias.reverse()
        
        for i in top10medias:#numeros
            for j in top10:#nomes

                if top10[j] == i:
                    top10console.append(j)
                    top10[j]=-1

        c = 0
        top10mediasPlot = []
        top10consolePlot = []

        for k in range(10):
            top10mediasPlot.append(top10medias[c])
            top10consolePlot.append(top10console[c])
            c += 1
    vendasArquivo.close()
#------Gera historico--
    x=''
    y=''
    for i in range(len(top10consolePlot)):
        if i != 0:
            x +=','
            y +=','   
        x += str(top10consolePlot[i])
        y += str(top10mediasPlot[i])
        
    h='busca_3,'+'Região:'+regiao+'|'+x+'|'+y+'|'+'\n'
    escrever(h)


#----------------------


    return graphics3(top10consolePlot, top10mediasPlot,regiao)


def graphics3(top10consolePlot, top10mediasPlot,regiao):
        x = ()
        y = ()
        x = top10consolePlot
        y = top10mediasPlot

        plt.scatter(x, y, s = 30)
        plt.grid(True)
        plt.xlabel('Plataforma:')
        plt.ylabel('Médias:')
        plt.title('Média X Plataforma,Região {0}'.format(regiao))
        plt.show()

#-------------------------------------BUSCA 4 -----------------------------------------------------------
def busca_4(gen):
    arq = open('vgsales.csv', 'r')
    lista = []                                                     
    L = []                                                                                      
    med = [0,0,0,0,0]
    regiao = ['NA', 'EU', 'JP', 'Other', 'Global']
    for linha in arq:
        linha=linha.replace('\n', '')
        lista.append(linha.split(','))
    arq.close()

    for i in range (1,len(lista)):
        L = lista[i]
        if L[4] == gen : 
            med[0] += float(L[6])
            med[1] += float(L[7])
            med[2] += float(L[8])
            med[3] += float(L[9])
            med[4] += float(L[10])
            
    loop0(0,med,regiao,gen)
#-------Recursiva--------
def loop0(i,med,regiao,gen): 
    med[i] *= 100.00 / (2*med[4])
    i += 1
    if i != 5:
        return loop0(i,med,regiao,gen)
    
    x=''
    y=''
    return loop1(0,med,gen,regiao,x,y)

    graphics4(med,regiao,gen)

def loop1(i,med,gen,regiao,x,y):
      
    if i != 0:
        x +=','
        y +=','   
    x += str(regiao[i])
    y += str(med[i])
    i += 1
    if i != 5:
        return loop1(i,med,gen,regiao,x,y)
    h='busca_4,'+'Gênero:'+gen+'|'+x+'|'+y+'|'+'\n'
    escrever(h)
    graphics4(med,regiao,gen)
#-----------Tela  
def graphics4(med,regiao,gen):
    cor = ['#4682B4', '#708090', '#6A5ACD', '#191970', '#ADD8E6']
    plt.pie(med, labels = regiao,
            startangle = 90,
            colors = cor,
            shadow = True,
            explode = (0, 0, 0, 0, 0),
            autopct = '%1.1f%%')
    plt.title('Região X Média,Gênero:{0}'.format(gen))
    plt.show()       
#-------------------------------------BUSCA 5 ---------------------------------
def busca_5(anoA,anoB,gen,intervalo):
    lista=[]
    anos=[]

    
    while anoA != anoB+1:
        x=busca_1(str(anoA),'1',gen)
        lista.append(x)
        anos.append(str(anoA)) 
        anoA+= 1
#--- Gera historico--
    x=''
    y=''
    for i in range(len(lista)):
        if i != 0:
            x +=','
            y +=','   
        x += str(anos[i])
        y += str(lista[i])
        
    h='busca_5,'+'Gênero:'+gen+',Intervalo:'+intervalo+'|'+x+'|'+y+'|'+'\n'
    escrever(h)

#------------------
    graphics5(lista,anos,gen,intervalo)
    #return busca_5() ################

def graphics5(lista,anos,gen,intervalo):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    x = anos
    y = lista
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation (45)
    plt.bar(x,y)
    plt.ylabel('Média Global')
    plt.title('Médias globais entre {0}, Gênero: {1}'.format(intervalo,gen))
    plt.show()
#-----------------------------BUSCA 6 -----------------------------------------
def busca_6(ano, ano2,qgen):   
    arq = open('vgsales.csv', 'r')
    lista=[]                                                     
    L=[]
    xano =[]
    cont=-1
    game=''
    gnome=''
    n=['Action','Role-Playing', 'Shooter', 'Platform', 'Sports','Simulation',
           'Fighting','Misc', 'Adventure','Racing', 'Puzzle','Strategy']
    
    dic={'Action':0,'Role-Playing':0, 'Shooter':0, 'Platform':0, 'Sports':0,'Simulation':0,
           'Fighting':0,'Misc':0, 'Adventure':0,'Racing':0, 'Puzzle':0,'Strategy':0}
    ano1 = 0
    an1 = 0
    an2 = 0
    ano22 = 0
    ano1 = ano
    ano22 = ano2
    an1 = ano1
    an2 = ano22
    intervalo = str(an1)+'-'+str(an2)
    while ano1 <= ano22:
        xano.append(ano1)
        ano1 += 1
        
    nomes=[]
    valor=[0,0,0,0,0,0,0,0,0,0,0,0]
    valorgame=[0,0,0,0,0,0,0,0,0,0,0,0]
    g1=[]
    g2=[]
    g3=[]
    g4=[]
    g5=[]
    g6=[]
    g7=[]
    g8=[]
    g9=[]
    g10=[]
    g11=[]
    g12=[]
    
    for linha in arq:
        linha=linha.replace('\n', '')
        lista.append(linha.split(','))   
    arq.close()
    a=ano
    b=ano2
    while a != b+1:
        for i in range (1,len(lista)):
            L=lista[i]
            for j in range (12):
                    if L[4]== n[j] and L[3]== str(a):
                        valor[j] += 1      
                        dic[n[j]] += 1
        a += 1
        
    valor.sort(reverse=True)
    
    for i in range(12):
        for i in valor:#numeros
            for j in dic:#nomes
                if dic[j] == i:
                    nomes.append(j)
                    dic[j]=-1

    while ano != ano2 +1:
        cont +=1
        for i in range (1,len(lista)):
            L=lista[i]
            for j in range (12):
                    if L[4]== nomes[j] and L[3]== str(ano):
                        valorgame[j] += 1                        
        ano += 1 
        g1.append(valorgame[0])
        g2.append(valorgame[1])
        g3.append(valorgame[2])
        g4.append(valorgame[3])
        g5.append(valorgame[4])
        g6.append(valorgame[5])
        g7.append(valorgame[6])
        g8.append(valorgame[7])
        g9.append(valorgame[8])
        g10.append(valorgame[9])
        g11.append(valorgame[10])
        g12.append(valorgame[11])
        valorgame=[0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(len(nomes)):
            if i != 0:
                gnome +=','   
            gnome += str(nomes[i])
    m =''
    n =''
    o =''
    p =''
    q =''
    r =''
    s =''
    t =''
    u =''
    v =''
    w =''
    x =''
    for i in range(len(g1)):
            if i != 0:
                m += ','
                n += ','
                o += ','
                p += ','
                q += ','
                r += ','
                s += ','
                t += ','
                u += ','
                v += ','
                w += ','
                x += ','       
            m += str(g1[i])
            n += str(g2[i])
            o += str(g3[i])
            p += str(g4[i])
            q += str(g5[i])
            r += str(g6[i])
            s += str(g7[i])
            t += str(g8[i])
            u += str(g9[i])
            v += str(g10[i])
            w += str(g11[i])
            x += str(g11[i])
            
    game = m+'*'+n+'*'+o+'*'+p+'*'+q+'*'+r+'*'+s+'*'+t+'*'+u+'*'+v+'*'+w+'*'+x

    #--- Gera historico---
    xxx=''
    for i in range(len(xano)):
        if i != 0:
            xxx +=','  
        xxx += str(xano[i])

    h='busca_6,Gêneros:'+str(qgen)+',Intervalo:'+intervalo+'|'+str(gnome)+'|'+game+'|'+str(qgen)+'|'+xxx+'|'+str(an1)+'|'+str(an2)+'\n'
    escrever(h)
    
    graphics6(game,gnome, xano, qgen, an1, an2)

def graphics6(game,gnome, xano, qgen, an1, an2):
    A=[]
    g0=[]
    g1=[]
    g2=[]
    g3=[]
    g4=[]
    g5=[]
    g6=[]
    g7=[]
    g8=[]
    g9=[]
    g10=[]
    g11=[]

    game=game.split('*')
    gnome=gnome.split(',')
    g0=game[0].split(',')
    g1=game[1].split(',')
    g2=game[2].split(',')
    g3=game[3].split(',')
    g4=game[4].split(',')
    g5=game[5].split(',')
    g6=game[6].split(',')
    g7=game[7].split(',')
    g8=game[8].split(',')
    g9=game[9].split(',')
    g10=game[10].split(',')
    g11=game[11].split(',')
    
    for i in range(len(g0)):
        g0[i]=int(g0[i])
        g1[i]=int(g1[i])
        g2[i]=int(g2[i])
        g3[i]=int(g3[i])
        g4[i]=int(g4[i])
        g5[i]=int(g5[i])
        g6[i]=int(g6[i])
        g7[i]=int(g7[i])
        g8[i]=int(g8[i])
        g9[i]=int(g9[i])
        g10[i]=int(g10[i])
        g11[i]=int(g11[i])

    i = qgen

    if i >= 1:
        plt.plot(xano, g0, label = gnome[0])
    if i >= 2:
        plt.plot(xano, g1, label = gnome[1])
    if i >= 3:
        plt.plot(xano, g2, label = gnome[2])
    if i >= 4:
        plt.plot(xano, g3, label = gnome[3])
    if i >= 5:
        plt.plot(xano, g4, label = gnome[4])
    if i >= 6:
        plt.plot(xano, g5, label = gnome[5])
    if i >= 7:
        plt.plot(xano, g6, label = gnome[6])
    if i >= 8:
        plt.plot(xano, g7, label = gnome[7])
    if i >= 9:
        plt.plot(xano, g8, label = gnome[8])
    if i >= 10:
        plt.plot(xano, g7, label = gnome[9])
    if i >= 11:
        plt.plot(xano, g10, label = gnome[10])
    if i >= 12:
        plt.plot(xano, g11, label = gnome[11])

    plt.ylabel('Número de jogos')
    plt.xlabel('Intervalo de anos')
    plt.title('Número de jogos por gênero no ano de {0} - {1}'.format(an1, an2))
    plt.legend()
    
    plt.show()

#-----------------------------BUSCA 13-----------------------------------------
def busca_13(ano1, ano2, gen):
    intervaloAnos = []
    intervalo=str(ano1)+'-'+str(ano2)
    lista = []
    anos_str = []
    top20_mundial = []
    c = 0
    ano = ano1
    
    while ano1 <= ano2:#gera uma lista com todos os anos
        intervaloAnos.append(ano1)
        ano1 += 1

    anos_str = str(intervaloAnos)#anos em str
        
    with open ('vgsales.csv', 'r') as vendasArquivo:
        leitor_csv = csv.reader(vendasArquivo)

        for line in leitor_csv:
            if (line[3] in anos_str) and (line[4] == gen):
                lista.append(line)#cria uma lista com as linhas que correspondam ao genero e ao intervalo de anos

        for i in range(20):
            top20_mundial.append(lista[i])#da lista gerada, separa os 20 primeiros lugares 

        jogosTop20 = []
        vendasTop20_jpsales = []
        vendasTop20_eusales = []

        for line in top20_mundial:
            if (line[1]) in jogosTop20:
                jogosTop20.append(line[1]+'..R')#append os jogos
            else:
                jogosTop20.append(line[1])
            if (line[7]) != ' ' or 0 or '0':
                vendasTop20_eusales.append(float(line[7]))#append nas vendas de eu sales
            else:
                vendasTop20_eusales.append(0)#append 0 se nao tiver valor algum 
            if (line[8]) != ' ' or 0 or '0':
                vendasTop20_jpsales.append(float(line[8]))#append nas vendas jp sales
            else:
                vendasTop20_jpsales.append(0)
    vendasArquivo.close()

    #--- Gera historico--
    x=''
    y=''
    z=''
    for i in range(len(jogosTop20)):
        if i != 0:
            x +=','
            y +=','
            z +=','
        x += str(jogosTop20[i])
        y += str(vendasTop20_jpsales[i])
        z += str(vendasTop20_eusales[i])
    h='busca_13,'+'Gênero:'+gen+',Intervalo:'+intervalo+'|'+x+'|'+y+'|'+z+'|'+'\n'
    escrever(h)

#------------------
    return (graphics13(jogosTop20, vendasTop20_jpsales, vendasTop20_eusales,intervalo, gen))

def graphics13(jogosTop20, vendasTop20_jpsales, vendasTop20_eusales,intervalo, gen):

    plt.scatter(vendasTop20_jpsales, jogosTop20, color = 'b', label = 'Vendas no Japão')
    plt.scatter(vendasTop20_eusales, jogosTop20, color = 'r', label = 'Vendas na Europa')
    plt.xlabel('Vendas nas regiões EU e JP')
    plt.ylabel('Top 20 jogos ')
    plt.title('Top 20 jogos entre {0},Gênero: {1}'.format(intervalo, gen))
    plt.grid(True)
    plt.subplots_adjust(left = 0.39, right = 0.97)
    plt.legend()
    plt.show()
#------------------------------------------------------------------------------------------------------------
def ler(arquivo,ano,gen,intervalo,reg,busca):
    A=[]
    x=[]
    y=[]
    yy=[]
    z=[]
    zz=[]
    arq = open( user +'.txt', 'r')
    for linha in arq:
        A = linha.split('|')
        if A[0]== arquivo and busca != 6:
            
            x = A[1].split(',')
            yy = A[2].split(',')
            for i in range(len(yy)):
                y.append(float(yy[i]))
            arq.close()
            if busca == 1:
                graphics(x,y,ano)
                print('Você utilizou dados já pesquisados')
                return(1)
            if busca == 2:
                graphics2(x,y,ano,gen)
                print('Você utilizou dados já pesquisados')
                return(1)
            if busca == 3:
                graphics3(x,y,reg)
                print('Você utilizou dados já pesquisados')
                return(1)
            if busca == 4:
                graphics4(y,x,gen)
                print('Você utilizou dados já pesquisados')
                return(1)
            if busca == 5:
                graphics5(y,x,gen,intervalo)
                print('Você utilizou dados já pesquisados')
                return(1)
            if busca == 13:
                zz = A[3].split(',')
                for i in range(20):
                    z.append(float(zz[i]))
                a = intervalo.split('-')
                ano1 = str(a[0])
                ano2 = str(a[1])
                graphics13(x,y,z,gen,intervalo)
                print('Você utilizou dados já pesquisados')
                return(1)
        if A[0]== arquivo and busca == 6:
            xano=[]
            B = A[4].split(',')
            for i in range(len(B)):
                xano.append(int(B[i])) 
            qgen=int(A[3])
            an1=int(A[5])
            an2=int(A[6])
            graphics6(A[2],A[1],xano, qgen, an1, an2)
            print('Você utilizou dados já pesquisados')
            return(1)
    arq.close()
    return(0)                 
            
def escrever (valor):
    arq = open(user+'.txt', 'a')
    arq.write(valor)
    arq.close()
def hist():
    z=[]
    print('_'*80)
    arq = open(user +'.txt', 'r')
    for linha in arq:
        if linha[0:1] == '1' or linha[0:1] == '2':
            print('HISTÓRICO:\n')
        else:
            z=linha.split('|')
            print(z[0])

    arq.close()

#--------------------------------------MÓDULO DE MENU---------------------------------------------------------
        
def start(x):
    print('_'*80)
    print('1- Fazer buscas')
    print('2- Meu histórico')
    print('3- Sair')
    print('_'*80)
    op=input('Digite a opção correspondente\n')
    if op == '1':
        if x =='1':
            menu_1()
        else:
            menu_2()
            
    if op == '2':
        hist()
    if op == '3':
        return()

    return start(x)

def menu_1():
    print('_'*80)
    print('\t\t\t\tBUSCAS')
    print('-'*80)
    print('1:   Média global de vendas por gênero de jogos que \n\tforam lançados em um determinado ano.')
    print('-'*80)
    print('2:   Quais as 10 empresas que mais publicaram em um determinado\n\t ano, usando um determinado gênero')
    print('-'*80)
    print('3:   Top 10 média de vendas por plataforma para uma determinada região.')
    print('-'*80)
    print('4:   Média de vendas de acordo com um determinado gênero dos jogos \n\tvendidos em NA, EU, JP, Outros e global.')
    print('-'*80)
    print('5:   Média das Vendas globais por ano,baseadas em um determinado intervalo\n\tde anos e um gênero.')
    print('-'*80)
    print('6:  Quantidade de jogos de acordo com os “X” maiores gênero em um\n\t intervalo de anos.')
    print('-'*80)
    print('13: Média global de vendas por gênero de jogos que \n\tforam lançados em um determinado ano.')
    print('_'*80)

    op=input('Digite a opção que deseja buscar ["0" para retornar ao menu inicial]\n')
    if op=='0':#------------------------------------------------------------------------
        return
    if op=='1':#-----------------------------------------------------------------------
        ano=input('Digite o ano que deseja visualizar\n')
        try:
            ano = int(ano)
        except:
            print('Ano inválido!')
            return menu_1()

        if ano < 1980 or ano > 2020:
            print('Ano inválido!')
            return menu_1()
        x = ler('busca_1,Ano:'+str(ano),str(ano),0,0,0,1)   #arquivo,ano,genero,intervalo,regiao,busca
        if x == 0 :
            busca_1(str(ano),'0','0')
        return menu_1()
    if op=='2':#---------------------------------------------------------------------###
        ano= input('Digite o ano que deseja visualizar\n')
        try:
            ano = int(ano)
        except:
            print ('Ano inválido!')
            return menu_1()
        
        if ano < 1980 or ano > 2020:
            print('Ano inválido!')
            return menu_1()
            print('-'*80)
        print('-'*80)
        print('Escolha o gênero:')
        print('-'*80)

        gen = input('1-Action\n2-Role-Playing\n3-Shooter\n4-Platform\n5-Sports\n6-Simulation\n7-Fighting\n8-Misc\n9-Adventure\n10-Racing\n11-Puzzle\n12-Strategy\n')
        try:
            gen=int(gen)
        except:
            print('Opção inválida!')
            return menu_1()
        if gen < 0 or gen > 12:
            print('Opção inválida!')
            return menu_1()        

        if gen == 1:
            gen='Action'
        if gen == 2:
            gen='Role-Playing'
        if gen == 3 :
            gen='Shooter'
        if gen == 4 :
            gen='Platform'
        if gen == 5:
            gen='Sports'
        if gen == 6 :
            gen='Simulation'
        if gen == 7 :
            gen='Fighting'
        if gen == 8 :
            gen='Misc'
        if gen == 9 :
            gen='Adventure'
        if gen == 10 :
            gen='Racing'
        if gen == 11 :
            gen='Puzzle'
        if gen == 12 :
            gen='Strategy'
        if gen == 0:
            return menu_1()
        x=ler('busca_2,Ano:'+str(ano)+',Gênero:'+str(gen),str(ano),str(gen),0,0,2)#arquivo,ano,genero,intervalo,regiao,busca
        if x == 0 :
            busca_2(str(ano),gen)
        return menu_1()
    if op=='3':#--------------------------------------------------------------------
        print('Regiões:\n1- NA\n2- EU\n3- JP\n4- Other\n')
        regiao=input('Digite a região que deseja visualizar\n')
        try:
            regiao=int(regiao)
        except:
            print('Opção inválida!')
            return menu_1()
        regiao+=5
        r=regiao
        if regiao < 6 or regiao > 9:
            print('Opção inválida!')
            return menu_1()
        if regiao == 6:
            regiao = 'NA'
        if regiao == 7:
            regiao = 'EU'
        if regiao == 8:
            regiao = 'JP'
        if regiao == 9:
            regiao = 'Other'
            
        x=ler('busca_3,Região:'+regiao,0,0,0,regiao,3)   #arquivo,ano,genero,intervalo,regiao   
        if x == 0:
            busca_3(r)
        return menu_1()
    
    if op=='4':#--------------------------------------------------------------------
        print('-'*80)
        print('Escolha o gênero:   \t["0" para retornar ao menu inicial]')
        print('-'*80)
        gen=input('1-Action\n2-Role-Playing\n3-Shooter\n4-Platform\n5-Sports\n6-Simulation\n7-Fighting\n8-Misc\n9-Adventure\n10-Racing\n11-Puzzle\n12-Strategy\n')

        try:
            gen=int(gen)
        except:
            print('Opção inválida!')
            return menu_1()
        if gen < 0 or gen > 12:
            print('Opção inválida!')
            return menu_1()        

        if gen == 1:
            gen='Action'
        if gen == 2:
            gen='Role-Playing'
        if gen == 3 :
            gen='Shooter'
        if gen == 4 :
            gen='Platform'
        if gen == 5:
            gen='Sports'
        if gen == 6 :
            gen='Simulation'
        if gen == 7 :
            gen='Fighting'
        if gen == 8 :
            gen='Misc'
        if gen == 9 :
            gen='Adventure'
        if gen == 10 :
            gen='Racing'
        if gen == 11 :
            gen='Puzzle'
        if gen == 12 :
            gen='Strategy'
        if gen == 0 :
            return menu_1()

        x=ler('busca_4,Gênero:'+gen,0,gen,0,0,4)
        if x == 0:
            busca_4(gen)
        return menu_1()
    if op=='5':#--------------------------------------------------------------------
        print('_'*80)
        anoA =input('Digite o primeiro ano do intervalo\t["0"para sair]\n')
        try:
            anoA=int(anoA)
        except:
            print('Opção inválida!')
            return menu_1()
        if anoA == 0:
            return menu_1()
        anoB =input('Digite o segundo ano do intervalo\t["0"para sair]\n')
        
        try:
            anoB=int(anoB)
        except:
            print('Opção inválida!')
            return menu_1()        
        if anoB == 0:
            return menu_1()
        
        if anoA > anoB:
            a = 0
            a = anoB
            anoB = anoA
            anoA = a

        if anoA < 1980 or anoB > 2020:
            print('Intervalo inválido.')
            return menu_1()

        print('-'*80)
        print('Escolha o gênero:')
        print('-'*80)
        gen=input('1-Action\n2-Role-Playing\n3-Shooter\n4-Platform\n5-Sports\n6-Simulation\n7-Fighting\n8-Misc\n9-Adventure\n10-Racing\n11-Puzzle\n12-Strategy\n')

        try:
            gen = int(gen)
        except:
            print('Opção inválida!')
            return menu_1()
        if gen < 0 or gen > 12:
            print('Opção inválida!')
            return menu_1()
        if gen ==1:
            gen='Action'
        if gen ==2:
            gen='Role-Playing'
        if gen ==3:
            gen='Shooter'
        if gen ==4:
            gen='Platform'
        if gen ==5:
            gen='Sports'
        if gen ==6:
            gen='Simulation'
        if gen ==7:
            gen='Fighting'
        if gen ==8:
            gen='Misc'
        if gen ==9:
            gen='Adventure'
        if gen ==10:
            gen='Racing'
        if gen ==11:
            gen='Puzzle'
        if gen == 12:
            gen='Strategy'
        if gen == 0 :
            return()
        intervalo=(str(anoA)+'-'+str(anoB))
        
        x = ler('busca_5,Gênero:'+str(gen)+',Intervalo:'+str(intervalo),0,str(gen),intervalo,0,5) #arquivo,ano,genero,intervalo,regiao,busca 
        if x == 0:
            busca_5(anoA,anoB,gen,intervalo)
        return menu_1()
    
    if op=='6':#--------------------------------------------------------------------
        print('_'*80)
        anoA =input('Digite o primeiro ano do intervalo\t["0"para sair]\n')
        if anoA == 0:
            return()
        try:
            anoA = int(anoA)
        except:
            print('Ano inválido!')
            return menu_1()
        
        anoB =input('Digite o segundo ano do intervalo\t["0"para sair]\n')
        if anoB == 0:
            return()
        try:
            anoB = int(anoB)
        except:
            print('Ano inválido!')
            return menu_1()
        
        if anoA > anoB:
            a = 0
            a = anoB
            anoB = anoA
            anoA = a

        if anoA < 1980 or anoB > 2020:
            print('Intervalo inválido!')
            return menu_1()

        qgen =input('Digite a quantidade de gêneros que deseja visualizar [1 a 12] \t["0"para sair]\n')

        try:
            qgen = int(qgen)
        except:
            print('Opção inválida!')

        if qgen < 1 or qgen > 12:
            print('Número inválido!')
            return menu_1()
            
        intervalo=(str(anoA)+'-'+str(anoB))
        
        x = ler('busca_6,Gêneros:'+str(qgen)+',Intervalo:'+str(intervalo),0,0,intervalo,0,6) #arquivo,ano,genero,intervalo,regiao,busca 
        if x == 0:
            busca_6(anoA,anoB,qgen)
        return menu_1()
    
    if op=='13':#-------------------------------------------------------------------
        print('_'*80)
        anoA = input('Digite o primeiro ano do intervalo\t["0"para sair]\n')
        if anoA == 0:
            return menu_1()
        try:
            anoA = int(anoA)
        except:
            print('Ano inválido')
            return menu_1()
        
        
        anoB = input('Digite o segundo ano do intervalo\t["0"para sair]\n')

        if anoB == 0:
            return menu_1()
        try:
            anoB = int(anoB)
        except:
            print('Ano inválido!')
            return menu_1()
        
        if anoA < 1980 or anoA > 2020 or anoB < 1980 or anoB > 2020:
            print('Intervalo indisponível!')
            return menu_1()
            print('-'*80)
        if anoB == 0:
            return menu_1()
        if anoA > anoB:
            a = 0
            a = anoB
            anoB = anoA
            anoA = a
        print('-'*80)
        print('Escolha o gênero:')
        print('-'*80)
        gen=input('1-Action\n2-Role-Playing\n3-Shooter\n4-Platform\n5-Sports\n6-Simulation\n7-Fighting\n8-Misc\n9-Adventure\n10-Racing\n11-Puzzle\n12-Strategy\n')

        try:
            gen = int(gen)
        except:
            print('Opção inválida!')
            return menu_1()
        if gen < 0 or gen > 12:
            print('Opção inválida!')
            return menu_1()
        
        if gen == 1:
            gen='Action'
        if gen == 2:
            gen='Role-Playing'
        if gen == 3 :
            gen='Shooter'
        if gen == 4 :
            gen='Platform'
        if gen == 5:
            gen='Sports'
        if gen == 6 :
            gen='Simulation'
        if gen == 7 :
            gen='Fighting'
        if gen == 8 :
            gen='Misc'
        if gen == 9 :
            gen='Adventure'
        if gen == 10 :
            gen='Racing'
        if gen == 11 :
            gen='Puzzle'
        if gen == 12 :
            gen='Strategy'
        if gen == 0 :
            return()
        intervalo=(str(anoA)+'-'+str(anoB))
        
        x = ler('busca_13,Gênero:'+str(gen)+',Intervalo:'+str(intervalo),0,str(gen),intervalo,0,13) #arquivo,ano,genero,intervalo,regiao,busca 
        if x == 0:
            busca_13(anoA,anoB,gen)
        return menu_1()      
    return menu_1()
def menu_2():
    print('_'*80)
    print('\t\t\t\tBUSCAS')
    print('-'*80)
    print('1:   Média global de vendas por gênero de jogos que \n\tforam lançados em um determinado ano.\n') 
    print('-'*80)
    print('2:   Quais as 10 empresas que mais publicaram em um determinado\n\t ano, usando um determinado gênero\n')
    print('-'*80)
    print('5:   Média das Vendas globais por ano,baseadas em um determinado intervalo\n\tde anos e um gênero.\n')
    print('-'*80)
    print('13: Média global de vendas por gênero de jogos que \n\tforam lançados em um determinado ano.\n')
    print('_'*80)
    
    op=input('Digite a opção que deseja buscar ["0" para retornar ao menu inicial]\n')
    if op=='0':#----------------------------------------------------------------------------------
        return()
    if op=='1':#----------------------------------------------------------------------------------
        ano=input('Digite o ano que deseja visualizar\n')
        try:
            ano =int(ano)
        except:
            print('Ano inválido!')
            return menu_2()

        if ano < 1980 or ano > 2020:
            print('Ano indisponível!')
            return menu_2()
        
        x = ler('busca_1,Ano:'+str(ano),str(ano),0,0,0,1)   #arquivo,ano,genero,intervalo,regiao,busca
        if x == 0 :
            busca_1(str(ano),'0','0')
        return menu_2()
    if op=='2':#---------------------------------------------------------------------------------
        ano= input('Digite o ano que deseja visualizar\n')
        try:
            ano=int(ano)
        except:
            print('Ano inválido!')
            return menu_2()
        
        if ano < 1980 or ano > 2020:
            print('Ano indisponível')
            return menu_2()
            print('-'*80)
        print('-'*80)
        print('Escolha o gênero:')
        print('-'*80)
        gen=input('1-Action\n2-Role-Playing\n3-Shooter\n4-Platform\n5-Sports\n6-Simulation\n7-Fighting\n8-Misc\n9-Adventure\n10-Racing\n11-Puzzle\n12-Strategy\n')

        try:
            gen = int(gen)
        except:
            print('Opção inválida!')
            return menu_2()
        if gen < 0 or gen > 12:
            print('Opção inválida!')
            return menu_2()
        
        if gen == 1:
            gen='Action'
        if gen == 2:
            gen='Role-Playing'
        if gen == 3 :
            gen='Shooter'
        if gen == 4 :
            gen='Platform'
        if gen == 5:
            gen='Sports'
        if gen == 6 :
            gen='Simulation'
        if gen == 7 :
            gen='Fighting'
        if gen == 8 :
            gen='Misc'
        if gen == 9 :
            gen='Adventure'
        if gen == 10 :
            gen='Racing'
        if gen == 11 :
            gen='Puzzle'
        if gen == 12 :
            gen='Strategy'
        if gen == 0 :
            return()
        x=ler('busca_2,Ano:'+str(ano)+',Gênero:'+str(gen),str(ano),str(gen),0,0,2)#arquivo,ano,genero,intervalo,regiao,busca
        if x == 0 :
            busca_2(str(ano),gen)
        return menu_2()
    if op=='5':#--------------------------------------------------------------------------------
        print('_'*80)
        anoA =input('Digite o primeiro ano do intervalo\t["0"para sair]\n')
        try:
            anoA=int(anoA)
        except:
            print('Opção inválida!')
            return menu_2()
        if anoA == 0:
            return menu_2()
        anoB =input('Digite o segundo ano do intervalo\t["0"para sair]\n')
        
        try:
            anoB=int(anoB)
        except:
            print('Opção inválida!')
            return menu_2()        
        if anoB == 0:
            return menu_2()
        
        if anoA > anoB:
            a = 0
            a = anoB
            anoB = anoA
            anoA = a

        if anoA < 1980 or anoB > 2020:
            print('Intervalo inválido.')
            return menu_2()

        print('-'*80)
        print('Escolha o gênero:')
        print('-'*80)
        gen=input('1-Action\n2-Role-Playing\n3-Shooter\n4-Platform\n5-Sports\n6-Simulation\n7-Fighting\n8-Misc\n9-Adventure\n10-Racing\n11-Puzzle\n12-Strategy\n')

        try:
            gen = int(gen)
        except:
            print('Opção inválida!')
            return menu_2()
        if gen < 0 or gen > 12:
            print('Opção inválida!')
            return menu_2()
        
        if gen == 1:
            gen='Action'
        if gen == 2:
            gen='Role-Playing'
        if gen == 3 :
            gen='Shooter'
        if gen == 4 :
            gen='Platform'
        if gen == 5:
            gen='Sports'
        if gen == 6 :
            gen='Simulation'
        if gen == 7 :
            gen='Fighting'
        if gen == 8 :
            gen='Misc'
        if gen == 9 :
            gen='Adventure'
        if gen == 10 :
            gen='Racing'
        if gen == 11 :
            gen='Puzzle'
        if gen == 12 :
            gen='Strategy'
        if gen == 0 :
            return menu_2()
        intervalo=(str(anoA)+'-'+str(anoB))
        
        x = ler('busca_5,Gênero:'+str(gen)+',Intervalo:'+str(intervalo),0,str(gen),intervalo,0,5) #arquivo,ano,genero,intervalo,regiao,busca 
        if x == 0:
            busca_5(anoA,anoB,gen,intervalo)
        return menu_2()
    
    if op=='13':#-------------------------------------------------------------------------------
        print('_'*80)
        anoA = input('Digite o primeiro ano do intervalo\t["0"para sair]\n')
        if anoA == 0:
            return menu_2()
        try:
            anoA = int(anoA)
        except:
            print('Ano inválido')
            return menu_2()
        
        
        anoB = input('Digite o segundo ano do intervalo\t["0"para sair]\n')

        if anoB == 0:
            return menu_2()
        try:
            anoB = int(anoB)
        except:
            print('Ano inválido!')
            return menu_2()
        
        if anoA < 1980 or anoA > 2020 or anoB < 1980 or anoB > 2020:
            print('Intervalo indisponível!')
            return menu_2()
            print('-'*80)
        if anoB == 0:
            return menu_2()
        if anoA > anoB:
            a = 0
            a = anoB
            anoB = anoA
            anoA = a
        print('-'*80)
        print('Escolha o gênero:')
        print('-'*80)
        gen=input('1-Action\n2-Role-Playing\n3-Shooter\n4-Platform\n5-Sports\n6-Simulation\n7-Fighting\n8-Misc\n9-Adventure\n10-Racing\n11-Puzzle\n12-Strategy\n')
        try:
            gen = int(gen)
        except:
            print('Opção inválida!')
            return menu_2()
        if gen < 0 or gen > 12:
            print('Opção inválida!')
            return menu_2()
        
        if gen == 1:
            gen='Action'
        if gen == 2:
            gen='Role-Playing'
        if gen == 3 :
            gen='Shooter'
        if gen == 4 :
            gen='Platform'
        if gen == 5:
            gen='Sports'
        if gen == 6 :
            gen='Simulation'
        if gen == 7 :
            gen='Fighting'
        if gen == 8 :
            gen='Misc'
        if gen == 9 :
            gen='Adventure'
        if gen == 10 :
            gen='Racing'
        if gen == 11 :
            gen='Puzzle'
        if gen == 12 :
            gen='Strategy'
        if gen == 0 :
            return()
        intervalo=(str(anoA)+'-'+str(anoB))
        
        x = ler('busca_13,Gênero:'+str(gen)+',Intervalo:'+str(intervalo),0,str(gen),intervalo,0,13) #arquivo,ano,genero,intervalo,regiao,busca 
        if x == 0:
            busca_13(anoA,anoB,gen)
        return menu_2() 
    else:
        print('Opção inválida!')
        return menu_2()
    
#-------------------------------------------------------MÓDULO DE SENHAS-----------------------
def login():
    def autenticador(x,y,operação):
        if operação=='login':
            if os.path.isfile(x +'.txt'):
                if y !='y':
                    arq = open(x +'.txt', 'r')
                    for linha in arq:
                        tipo = linha[0:1]
                        if tipo == '1':
                            password = linha[1:len(linha)-1]
                            if password == y:
                                arq.close()
                                return ('Gerente') 
                                    
                        if tipo == '2':
                            password = linha[1:len(linha)-1]
                            if password == y:
                                arq.close()
                                return ('Funcionário')
                            
                    arq.close()
                    return('0')#senha
                
            else: #nome
                return('0')
            
        if operação=='new':
            if os.path.isfile(x +'.txt'):
                print('Usuário já existe!')
                return()
            else:
                arq = open(x +'.txt', 'a')
                arq.close()
                arq = open(x +'.txt', 'a')
                arq.write(y+'\n')
                arq.close()
                print('Usuário Cadastrado!')
                return()
        
    print('_'*80)
    print ('1-Para para fazer Login\n')
    print ('2-Para criar um Novo Usuário')
    print('_'*80)
    x=input()
    print('_'*80)
    if x == '2': #novo usuário----------------------------------------------------------------
        print('\t\t\t\tNovo Usuário:')
        user=input('Usuário:\n')
        user=user.upper()
        if user == '':
            print('Usuário inválido!')
            return login()
            
        password=input('Senha:\n')
        if password == '':
            print('Senha inválida!')
            return login()
        tipo=input('Digite tipo de usuário:\n1-Gerente\n2-Funcionário\n')
        if tipo == '1' or tipo =='2':
            password = tipo+password #
            autenticador(user,password,'new')
            return login()
        else:
            print('Opção inválida!')
            return login()

    if x == '1':#login-------------------------------------------------------------------------
        print('\t\t\t\tFazer login:')
        user=input('Usuário:\n')
        user=user.upper()
        w=autenticador(user,'y','login')
        if w =='0':
            print('\tNome de usuário incorreto!, por favor tente novamente:\n')
            return login()
        password=input('Senha:\n')
        
        z=autenticador(user,password,'login')
        if z == '0':
            print('Senha incorreta!tente novamente')
            return login()
        return(user,z)
    
    else:
        print('Opção inválida!')
        return login()
#_start_____________________________________________________________________________________________
global user
print('\n\t\t\t\tBem Vindo(a)!')
user,tipo=login()
print('_'*80)
print('Conectado como:\t-{0}-\t[{1}]'.format(user,tipo))
print('_'*80)


if tipo =='Gerente':
    start('1')
else:
    start  ('0')
