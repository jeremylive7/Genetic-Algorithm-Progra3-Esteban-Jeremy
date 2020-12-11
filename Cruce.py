from math import pi, sin, cos

class Cruce:
    def creoListaDeBits(abeja):
        PARAM_SIZE_1 = 16
        PARAM_SIZE_2 = 8
        listaGenesBits = ''

        direccion_favorita = abeja.direccion_favorita
        color_favorito = abeja.color_favorito
        tolerancia_al_color = abeja.tolerancia_al_color
        angulo_desviacion = abeja.angulo_desviacion
        distancia_maxima = abeja.distancia_maxima
        
        codGeneticoDirFav = int(0xffff*direccion_favorita/(2*pi))##! Debe estar entre 0 y 2*pi
        codGeneticoTolerancia = int(0xff*tolerancia_al_color)
        codGeneticoAnguloDesviacion = int(0xffff*angulo_desviacion/(2*pi))
        codGeneticoDistanciaMaxima = int(0xff*distancia_maxima/70.71)
        
        listaGenesBits += bin(codGeneticoDirFav)[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoTolerancia)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += f'{bin(color_favorito[0])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[1])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[2])[2:].zfill(PARAM_SIZE_2)}'
        listaGenesBits += bin(codGeneticoAnguloDesviacion)[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoDistanciaMaxima)[2:].zfill(PARAM_SIZE_2)

        return listaGenesBits
