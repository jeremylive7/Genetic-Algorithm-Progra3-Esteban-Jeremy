from math import pi, sin, cos

class Cruce:

    def get_float(x, nP): return '{0:.{n}f}'.format(x, n=nP)

    def get_bin(x): 
        var= format(x, 'b')
        while len(var)<8:
            var="0"+var
        return var

    def convertIntToBinario(pParam: int):
        return Cruce.get_bin(pParam)

    def convertIntToBinarioTripleta(pParam: int):
        result = []

        for i in range(len(pParam)):
            while len(pParam[i])<8:
                pParam[i]="0"+pParam[i]
            result.append(pParam[i])

        return result

    def convertBinarioToInt(pParam):
        return int(pParam, 2)

    def decimal_converter(num):
        while num > 1:
            num /= 10
        return num

    def float_bin(number, cantidad):
        whole, dec = str(number).split(".")
        whole = int(whole)
        dec = int(dec)
        if whole == 0:
            res = "0."
        else:
            res = bin(whole).lstrip("0b") + "."

        for x in range(cantidad):
            whole, dec = str((Cruce.decimal_converter(dec)) * 2).split(".")
            dec = int(dec)
            res += whole

        return res

    def puntoPosicion(binario):
        for i in range(len(binario)):
            if binario[i] == ".":
                return i
        return 0

    def eliminoPunto(binario):
        parte_1, parte_2 = binario.split(".")#FFFF*0.75555
        resultado = parte_1+parte_2
        return resultado

    def creoListaDeBits(abeja):
        result = []
        parte_hijo_binario = ""

        """
        direccion_favorita = abeja.direccion_favorita
        color_favorito = abeja.color_favorito
        tolerancia_al_color = abeja.tolerancia_al_color
        angulo_desviacion = abeja.angulo_desviacion
        distancia_maxima = abeja.distancia_maxima
        """
        direccion_favorita = 2.366 #
        tolerancia_al_color = 0.554     
        angulo_desviacion = 30.39
        distancia_maxima = 71
        color_favorito = (255, 0, 0)

        listaGenesBits=''
        codGeneticoDirFav=int(0xffff*direccion_favorita/(2*pi))##! Debe estar entre 0 y 2*pi
        
        codGeneticoTolerancia=int(0xffff*tolerancia_al_color)
        
        codGeneticoAnguloDesviacion=int(0xffff*angulo_desviacion/(2*pi))

        codGeneticoDistanciaMaxima=int(0xffff*distancia_maxima/70.71)

        
        
        PARAM_SIZE_1=16
        PARAM_SIZE_2=8
        listaGenesBits += bin(codGeneticoDirFav)[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoTolerancia)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += f'{bin(color_favorito[0])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[1])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[2])[2:].zfill(PARAM_SIZE_2)}'
        listaGenesBits += bin(codGeneticoDistanciaMaxima)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += bin(codGeneticoDistanciaMaxima)[2:].zfill(PARAM_SIZE_2)
        
        print("hijo direccion: %s" % listaGenesBits[:16])
        print("hijo tolerancia: %s" % listaGenesBits[16:32])
        print("hijo color: %s" % listaGenesBits[16:32])
        print("hijo angulo: %s" % listaGenesBits[40:56])
        print("hijo distancia: %s" % listaGenesBits[4])
        return listaGenesBits