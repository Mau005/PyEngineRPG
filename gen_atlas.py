

def archivos(ruta,lista,nombre_archivo):
    resultados = ""
    for procesar in range(len(lista)):
        resultados += lista[procesar]

    formato = """
    {
        "%s": {
            %s
        }
    }
    """ % (nombre_archivo,resultados)

    archivo = open(ruta,'w')
    archivo.write(formato)
    archivo.close()

def contexto(tamx,tamy,cuadrox,cuadroy):
    resultado = []

    cantidadX = int(tamx/cuadrox)
    cantidadY = int(tamy/cuadroy)
    conteo = 0
    for num in range(0,cantidadX):
        for numy in range(0,cantidadY):
            conteo+=1
            resultado.append(f'"{conteo}": [{cuadrox*num}, {cuadroy*numy}, {cuadrox}, {cuadroy}],\n')


    return resultado





archivos("test.atlas",contexto(1024,1024,128,32),"tu_hermana.png")