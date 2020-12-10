from math import pi, sin, cos

class Cruce:

    def get_float(x, nP): return '{0:.{n}f}'.format(x, n=nP)

    def get_bin(x): return format(x, 'b')

    def convertIntToBinario(pParam: int):
        return Cruce.get_bin(pParam)

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
            print("entro")
            res = "0."
        else:
            res = bin(whole).lstrip("0b") + "."

        for x in range(cantidad):
            whole, dec = str((Cruce.decimal_converter(dec)) * 2).split(".")
            dec = int(dec)
            res += whole

        return res

    def puntoPosicion(binario):
        for i in range(len(binario)-1):
            if binario[i] == ".":
                return i
        return 0

    def eliminoPunto(binario):
        parte_1, parte_2 = binario.split(".")
        return parte_1+parte_2

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
        direccion_favorita = 2.366
        color_favorito = 255 #(255, 0, 0)
        tolerancia_al_color = 0.554
        angulo_desviacion = 30.39
        distancia_maxima = 71

        cantidad = 2

        direccion_favorita_hijo_con_punto = Cruce.float_bin(direccion_favorita, cantidad)
        print("direccion.. %s" % direccion_favorita_hijo_con_punto)
        color_favorito_hijo = Cruce.convertIntToBinario(color_favorito)
        tolerancia_al_color_hijo_con_punto = Cruce.float_bin(tolerancia_al_color, cantidad)
        print("tolerancia... %s" % tolerancia_al_color_hijo_con_punto)
        angulo_desviacion_hijo_con_punto = Cruce.float_bin(angulo_desviacion, cantidad)
        print("angulo... %s" % angulo_desviacion_hijo_con_punto)
        distancia_maxima_hijo = Cruce.convertIntToBinario(distancia_maxima)

        posicion_punto_direccion = Cruce.puntoPosicion(direccion_favorita_hijo_con_punto)
        posicion_punto_desviacion = Cruce.puntoPosicion(angulo_desviacion_hijo_con_punto)
        posicion_punto_tolerancia = Cruce.puntoPosicion(tolerancia_al_color_hijo_con_punto)

        direccion_favorita_hijo = Cruce.eliminoPunto(direccion_favorita_hijo_con_punto)
        angulo_desviacion_hijo = Cruce.eliminoPunto(angulo_desviacion_hijo_con_punto)
        tolerancia_al_color_hijo = Cruce.eliminoPunto(tolerancia_al_color_hijo_con_punto)

        parte_hijo_binario += direccion_favorita_hijo
        parte_hijo_binario += color_favorito_hijo
        parte_hijo_binario += tolerancia_al_color_hijo
        parte_hijo_binario += angulo_desviacion_hijo
        parte_hijo_binario += distancia_maxima_hijo

        largo_direccion = len(direccion_favorita_hijo)
        largo_color_favorito = len(color_favorito_hijo)
        largo_tolerancia = len(tolerancia_al_color_hijo)
        largo_angulo_desviacion = len(angulo_desviacion_hijo)
        largo_distancia_maxima = len(distancia_maxima_hijo)

        lista_largo_variables = []
        lista_largo_variables.append(largo_direccion)
        lista_largo_variables.append(largo_direccion+largo_color_favorito)
        lista_largo_variables.append(largo_direccion+largo_color_favorito+largo_tolerancia)
        lista_largo_variables.append(largo_direccion+largo_color_favorito+largo_tolerancia+largo_angulo_desviacion)
        lista_largo_variables.append(largo_direccion+largo_color_favorito+largo_tolerancia+largo_angulo_desviacion+largo_distancia_maxima)

        lista_largo_variables_por_parametro = []
        lista_largo_variables_por_parametro.append(largo_direccion)
        lista_largo_variables_por_parametro.append(largo_color_favorito)
        lista_largo_variables_por_parametro.append(largo_tolerancia)
        lista_largo_variables_por_parametro.append(largo_angulo_desviacion)
        lista_largo_variables_por_parametro.append(largo_distancia_maxima)

        result.append(parte_hijo_binario)
        result.append(posicion_punto_direccion)
        result.append(posicion_punto_desviacion)
        result.append(lista_largo_variables_por_parametro)
        result.append(lista_largo_variables)
        result.append(posicion_punto_tolerancia)

        return result

    def creoListaDeBits2(abeja):
        result = []
        parte_hijo_binario = ""

        """
        direccion_favorita = abeja.direccion_favorita
        color_favorito = abeja.color_favorito
        tolerancia_al_color = abeja.tolerancia_al_color
        angulo_desviacion = abeja.angulo_desviacion
        distancia_maxima = abeja.distancia_maxima
        """
        direccion_favorita = 4.777
        color_favorito = 200  # (255, 0, 0)
        tolerancia_al_color = 0.253
        angulo_desviacion = 26.22
        distancia_maxima = 40

        cantidad = 2

        direccion_favorita_hijo_con_punto = Cruce.float_bin(
            direccion_favorita, cantidad)
        color_favorito_hijo = Cruce.convertIntToBinario(color_favorito)
        tolerancia_al_color_hijo_con_punto = Cruce.float_bin(
            tolerancia_al_color, cantidad)
        angulo_desviacion_hijo_con_punto = Cruce.float_bin(
            angulo_desviacion, cantidad)
        distancia_maxima_hijo = Cruce.convertIntToBinario(distancia_maxima)

        posicion_punto_direccion = Cruce.puntoPosicion(
            direccion_favorita_hijo_con_punto)
        posicion_punto_desviacion = Cruce.puntoPosicion(
            angulo_desviacion_hijo_con_punto)
        posicion_punto_tolerancia = Cruce.puntoPosicion(
            tolerancia_al_color_hijo_con_punto)

        direccion_favorita_hijo = Cruce.eliminoPunto(
            direccion_favorita_hijo_con_punto)
        angulo_desviacion_hijo = Cruce.eliminoPunto(
            angulo_desviacion_hijo_con_punto)
        tolerancia_al_color_hijo = Cruce.eliminoPunto(
            tolerancia_al_color_hijo_con_punto)

        parte_hijo_binario += direccion_favorita_hijo
        parte_hijo_binario += color_favorito_hijo
        parte_hijo_binario += tolerancia_al_color_hijo
        parte_hijo_binario += angulo_desviacion_hijo
        parte_hijo_binario += distancia_maxima_hijo

        largo_direccion = len(direccion_favorita_hijo)
        largo_color_favorito = len(color_favorito_hijo)
        largo_tolerancia = len(tolerancia_al_color_hijo)
        largo_angulo_desviacion = len(angulo_desviacion_hijo)
        largo_distancia_maxima = len(distancia_maxima_hijo)

        lista_largo_variables = []
        lista_largo_variables.append(largo_direccion)
        lista_largo_variables.append(largo_direccion+largo_color_favorito)
        lista_largo_variables.append(
            largo_direccion+largo_color_favorito+largo_tolerancia)
        lista_largo_variables.append(
            largo_direccion+largo_color_favorito+largo_tolerancia+largo_angulo_desviacion)
        lista_largo_variables.append(largo_direccion+largo_color_favorito +
                                     largo_tolerancia+largo_angulo_desviacion+largo_distancia_maxima)

        lista_largo_variables_por_parametro = []
        lista_largo_variables_por_parametro.append(largo_direccion)
        lista_largo_variables_por_parametro.append(largo_color_favorito)
        lista_largo_variables_por_parametro.append(largo_tolerancia)
        lista_largo_variables_por_parametro.append(largo_angulo_desviacion)
        lista_largo_variables_por_parametro.append(largo_distancia_maxima)

        result.append(parte_hijo_binario)
        result.append(posicion_punto_direccion)
        result.append(posicion_punto_desviacion)
        result.append(lista_largo_variables_por_parametro)
        result.append(lista_largo_variables)
        result.append(posicion_punto_tolerancia)

        return result

"""
    def createColor(pColor1, pColor2):
        binario_1 = []
        binario_2 = []
        binario_hijo = []

        for i in pColor1:
            binario_1.append(Cruce.convertIntToBinario(i))

        for o in pColor2:
            binario_2.append(Cruce.convertIntToBinario(o))

        for u in range(len(binario_1)):
            binario_11 = binario_1[u]
            binario_22 = binario_2[u]

            binario_slice1 = []
            binario_slice2 = []

            largo1 = int(len(binario_11)/2)
            largo2 = int(len(binario_22)/2)

            if largo1 % 2 != 0:
                binario_slice1 = [binario_11[i:i+largo1+1]
                                  for i in range(0, len(binario_11), largo1+1)]
            else:
                binario_slice1 = [binario_11[i:i+largo1]
                                  for i in range(0, len(binario_11), largo1)]

            if largo2 % 2 != 0:
                binario_slice2 = [binario_22[i:i+largo2+1]
                                  for i in range(0, len(binario_22), largo2+1)]
            else:
                binario_slice2 = [binario_22[i:i+largo2]
                                  for i in range(0, len(binario_22), largo2)]

            binario_hijo.append(
                Cruce.convertBinarioToInt(binario_slice1[0]+binario_slice2[1]))

        return binario_hijo

    def creoAnguloHijo(direccion_1, direccion_2):
        dic1 = Cruce.float_bin(direccion_1)
        dic2 = Cruce.float_bin(direccion_2)

        dic11 = []
        dic22 = []

        num_izq_1, num_der_1 = dic1.split(".")
        num_izq_2, num_der_2 = dic2.split(".")

        dic11.append(num_izq_1)
        dic11.append(num_der_1)

        dic22.append(num_izq_2)
        dic22.append(num_der_2)

        int_1 = int(dic11[0], 2)
        int_2 = int(dic22[1], 2)
        result = str(int_1)+"."+str(int_2)

        return result

    def creoHijo(x, y):
        angulo1 = Cruce.convertIntToBinario(x)
        angulo2 = Cruce.convertIntToBinario(y)
        angulo11 = []
        angulo22 = []

        largo1 = int(len(angulo1)/2)
        largo2 = int(len(angulo2)/2)

        if largo1 % 2 != 0:
            angulo11 = [angulo1[i:i+largo1+1]
                        for i in range(0, len(angulo1), largo1+1)]
        else:
            angulo11 = [angulo1[i:i+largo1]
                        for i in range(0, len(angulo1), largo1)]

        if largo2 % 2 != 0:
            angulo22 = [angulo2[i:i+largo2+1]
                        for i in range(0, len(angulo2), largo2+1)]
        else:
            angulo22 = [angulo2[i:i+largo2]
                        for i in range(0, len(angulo2), largo2)]

        result = Cruce.convertBinarioToInt(angulo11[0]+angulo22[1])

        return result
"""
