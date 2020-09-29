class Juego(): 
    def __init__(self):
        self.intento = 0
        self.long = 0
        self.palabra = ""
        self.condicion = False
        self.dificultad = 0

    def tirar(self): 
        return 0

    def score_final(self, puntaje): 
        return puntaje

    def devolver_intento(self):
        return self.intento

    def palabra_correcta(self, pal):
        if self.palabra.lower == pal.lower:
            self.condicion = True
            return True
        else:
            self.intento -= 1
            if self.intento == 0: #termina juego
                return False

    def devolver_longitud(self):
        return self.long

    def devolver_condicion(self):
        return self.condicion

    def devolver_palabra(self):
        return self.palabra

    def setear_palabra(self,pal):
        self.palabra = pal
        self.long = len(pal)

    def setear_intentos(self,inte):
        self.intento = inte

    def devolver_dificultad(self):
        return self.dificultad

    def setear_dificultad(self,dificultad):
        self.dificultad = dificultad