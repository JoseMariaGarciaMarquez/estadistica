def estadistica(data):
    print("--------------------------------------------------------------\n"
         "Programa que recibe un dataframe, calcula datos estadísticos\n"
         "Muestra los gráficos exploratorios, transforma los datos\n"
         "Y devuelve un dataframe listo para hacer Kirgging más adelante\n"
         "--------------------------------------------------------------\n")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
    #----Datos
    print(data.head(),"\n")
    
    D = input("Vector de datos: ")
    X = input("Vector X: ")
    Y = input("Vector Y: ")
    x = data[X]
    y = data[Y]
    datos = data[D]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
    #----Limpieza de datos
    resp = int(input("¿Desea pre-procesar los datos?\n1. SI\n2. NO\n"))
    if resp == 1:
        repe = int(input("Eliga el pre-procesado que desea:\n1. DATOS REPETIDOS\n2. DATOS INCOMPLETOS\n3. REMOVER CEROS\n4. VALORES ALTOS\n5. VALORES BAJOS\n"))
        if repe == 1:
            data = data.drop_duplicates()
            datos = data[D]
            x = data[X]
            y = data[Y]
            print("⚙️SU SET DE DATOS HAN SIDO PRE-PROCESADOS⚙️")
        
        elif repe == 2:
            data = data.notna()
            datos = data[D]
            x = data[X]
            y = data[Y]
            print("⚙️SU SET DE DATOS HAN SIDO PRE-PROCESADOS⚙️")
        
        elif repe == 3:
            data = data[data[D] > 0]
            print("⚙️SU SET DE DATOS HAN SIDO PRE-PROCESADOS⚙️")
            
        elif repe == 4:
            valor = float(input("Valor: "))
            data = data[data[D] < valor]
            datos = data[D]
            x = data[X]
            y = data[Y]
            print("⚙️SU SET DE DATOS HAN SIDO PRE-PROCESADOS⚙️")
            
        elif repe == 5:
            valor = float(inut("Valor: "))
            data = data[data[D] > valor]
            datos = data[D]
            x = data[X]
            y = data[Y]
            print("⚙️SU SET DE DATOS HAN SIDO PRE-PROCESADOS⚙️")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
    print("-----------------------------\n"
        "📊CALCULAR LOS ESTADÍSTICOS📊\n"
         "-----------------------------")
    med = np.mean(datos)
    median = np.median(datos)
    moda = sts.mode(datos)
    var = np.var(datos)
    std = np.std(datos)
    asi = sts.skew(datos)
    cur = sts.kurtosis(datos)

    print("TENDENCIA CENTRAL\nMedia: {:2.4f} ppm\nMediana: {:2.4f} ppm \nModa: {} ppm\n"
      "\nDISPERSION:\nVarianza: {:2.4f} ppp^2\nDesviacion estandar: {:2.4f} ppm\n"
      "\nFORMA:\nCoeficiente de asimetria: {:2.4f}\nCoeficiente de curtosis: {:2.4f}\n".format(med, median, moda[0][0], var, std, asi, cur))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

    print("-------------------------------\n"
        "🧭🗺GRÁFICOS EXPLORATORIOS🗺🧭\n"
         "-------------------------------")
    fig, ax = plt.subplots(2,2, figsize = (8,8), dpi = 200)
    ax[0,0].hist(datos, color = 'darkorange')
    ax[0,0].set_title("Histograma")
    
    ax[1,0].boxplot(datos, labels = "D", vert = False, sym = '+r')
    ax[1,0].set_title("Diagrama de caja")
    
    ax[0,1].scatter(x,y, c = datos)
    ax[0,1].set_title("Dispersión de datos")
    
    ax[1,1].hist(datos, bins = 100, histtype = 'stepfilled', cumulative = True)
    ax[1,1].set_title("Histograma acumulativo")
    
    plt.suptitle("GRAFICOS EXPLORATORIOS")
    plt.show()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    trans = int(input("¿Desea transformar los datos?\n1. SI\n2. NO\n"))
    if trans == 1:
        op = int(input("Escoga una transformación:\n1. RAIZ\n2. LOG\n3. Z-SCORE\n"))
        if op ==1:
            print("FUNCIONA RAIZ")
            datos = np.sqrt(datos)
            print("-----------------------------\n"
                "📊CALCULAR LOS ESTADÍSTICOS📊\n"
                    "-----------------------------")
            med = np.mean(datos)
            median = np.median(datos)
            moda = sts.mode(datos)
            var = np.var(datos)
            std = np.std(datos)
            asi = sts.skew(datos)
            cur = sts.kurtosis(datos)
            print("TENDENCIA CENTRAL\nMedia: {:2.4f} ppm\nMediana: {:2.4f} ppm \nModa: {} ppm\n"
              "\nDISPERSION:\nVarianza: {:2.4f} ppp^2\nDesviacion estandar: {:2.4f} ppm\n"
              "\nFORMA:\nCoeficiente de asimetria: {:2.4f}\nCoeficiente de curtosis: {:2.4f}\n".format(med, median, moda[0][0], var, std, asi, cur))
                
            print("-------------------------------\n"
                "🧭🗺GRÁFICOS EXPLORATORIOS🗺🧭\n"
                 "-------------------------------")
            
            fig, ax = plt.subplots(2,2, figsize = (8,8), dpi = 200)
            ax[0,0].hist(datos, color = 'darkorange')
            ax[0,0].set_title("Histogtama")
            
            ax[1,0].boxplot(datos, labels = "D", vert = False, sym = '+r')
            ax[1,0].set_title("Diagrama de caja")
            
            ax[0,1].scatter(x,y, c = datos)
            ax[0,1].set_title("Dispersión de datos")
            
            ax[1,1].hist(datos, bins = 100, histtype = 'stepfilled', cumulative = True)
            ax[1,1].set_title("Histograma acumulativo")
            
            plt.suptitle("GRAFICOS EXPLORATORIOS")
            plt.savefig("RESULTADOS.png")
            print("🥑Resultados salvados🥑")
            
        elif op == 2:
            print("FUNCIONA LOG")
            datos = np.log(datos)
            print("-----------------------------\n"
                "📊CALCULAR LOS ESTADÍSTICOS📊\n"
                    "-----------------------------")
            med = np.mean(datos)
            median = np.median(datos)
            moda = sts.mode(datos)
            var = np.var(datos)
            std = np.std(datos)
            asi = sts.skew(datos)
            cur = sts.kurtosis(datos)
            print("TENDENCIA CENTRAL\nMedia: {:2.4f} ppm\nMediana: {:2.4f} ppm \nModa: {} ppm\n"
              "\nDISPERSION:\nVarianza: {:2.4f} ppp^2\nDesviacion estandar: {:2.4f} ppm\n"
              "\nFORMA:\nCoeficiente de asimetria: {:2.4f}\nCoeficiente de curtosis: {:2.4f}\n".format(med, median, moda[0][0], var, std, asi, cur))
                
            print("-------------------------------\n"
                "🧭🗺GRÁFICOS EXPLORATORIOS🗺🧭\n"
                 "-------------------------------")
            fig, ax = plt.subplots(2,2, figsize = (8,8), dpi = 200)
            ax[0,0].hist(datos, color = 'darkorange')
            ax[0,0].set_title("Histograma")
            
            ax[1,0].boxplot(datos, labels = "D", vert = False, sym = '+r')
            ax[1,0].set_title("Diagrama de caja")
            
            ax[0,1].scatter(x,y, c = datos)
            ax[0,1].set_title("Dispersión de datos")
            
            ax[1,1].hist(datos, bins = 100, histtype = 'stepfilled', cumulative = True)
            ax[1,1].set_title("Histograma acumulativo")
            
            plt.suptitle("GRAFICOS EXPLORATORIOS")
            plt.savefig("RESULTADOS.png")
            print("🥑Resultados salvados🥑")

        
        else:
            print("FUNCIONA Z")
            datos = sts.zscore(datos)
            print("-----------------------------\n"
                "📊CALCULAR LOS ESTADÍSTICOS📊\n"
                    "-----------------------------")
            med = np.mean(datos)
            median = np.median(datos)
            moda = sts.mode(datos)
            var = np.var(datos)
            std = np.std(datos)
            asi = sts.skew(datos)
            cur = sts.kurtosis(datos)
            print("TENDENCIA CENTRAL\nMedia: {:2.4f} ppm\nMediana: {:2.4f} ppm \nModa: {} ppm\n"
              "\nDISPERSION:\nVarianza: {:2.4f} ppp^2\nDesviacion estandar: {:2.4f} ppm\n"
              "\nFORMA:\nCoeficiente de asimetria: {:2.4f}\nCoeficiente de curtosis: {:2.4f}\n".format(med, median, moda[0][0], var, std, asi, cur))
                
            print("-------------------------------\n"
                "🧭🗺GRÁFICOS EXPLORATORIOS🗺🧭\n"
                 "-------------------------------")
            fig, ax = plt.subplots(2,2, figsize = (8,8), dpi = 200)
            ax[0,0].hist(datos, color = 'darkorange')
            ax[0,0].set_title("Histograma")
            
            ax[1,0].boxplot(datos, labels = "D", vert = False, sym = '+r')
            ax[1,0].set_title("Diagrama de caja")
            
            ax[0,1].scatter(x,y, c = datos)
            ax[0,1].set_title("Dispersión de datos")
            
            ax[1,1].hist(datos, bins = 100, histtype = 'stepfilled', cumulative = True)
            ax[1,1].set_title("Histograma acumulativo")
            
            plt.suptitle("GRAFICOS EXPLORATORIOS")
            plt.savefig("RESULTADOS.png")
            print("🥑Resultados salvados🥑")
            
    else:
        
        fig, ax = plt.subplots(2,2, figsize = (8,8), dpi = 200)
        ax[0,0].hist(datos, color = 'darkorange')
        ax[0,0].set_title("Histograma")
        
        ax[1,0].boxplot(datos, labels = "D", vert = False, sym = '+r')
        ax[1,0].set_title("Diagrama de caja")
        
        ax[0,1].scatter(x,y, c = datos)
        ax[0,1].set_title("Dispersión de datos")
        
        ax[1,1].hist(datos, bins = 100, histtype = 'stepfilled', cumulative = True)
        ax[1,1].set_title("Histograma acumulativo")
        
        plt.suptitle("GRAFICOS EXPLORATORIOS")
        
        plt.savefig("RESULTADOS.png")
        print("🥑Resultados salvados🥑")
        
    print("-----------------------------------------------------------------------\n"
        "CODE BY: GARCÍA MÁRQUEZ JOSÉ MARÍA💻\n"
        "UNAM GEOPHYSICAL ENGINEERING STUDENT🤓\n"
        "SAY THANKS💲 AT: https://paypal.me/Chemitas96?country.x=MX&locale.x=es_XC\n"
        "Suggestions at: josemariagarciamarquez2.72@gmail.com Subject: SUGGEST\n"
        "------------------------------------------------------------------------")
    
    return data