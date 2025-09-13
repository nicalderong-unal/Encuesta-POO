
# Autor: Nicolás Alexander Calderón García

class Encuesta:
    def __init__(self, preguntas):
        self.preguntas=preguntas
        self.respuestas=[]  

    def agregar_respuesta(self):
        print("\n-------------------------------\n|       Nueva respuesta       |\n-------------------------------")
        nombre=input(self.preguntas[0]+" Respuesta: ")
        edad=input(self.preguntas[1]+" Respuesta: ")
        idea_proyecto=input(self.preguntas[2]+" Respuesta: ")
        tiempo=input(self.preguntas[3]+" Respuesta: ")
        libreria_python=input(self.preguntas[4]+" Respuesta: ")
        motivacion=input(self.preguntas[5]+" Respuesta: ")

        estudiante=Estudiante(nombre, edad, idea_proyecto, tiempo, libreria_python, motivacion)
        self.respuestas.append(estudiante)

    def mostrar_resultados(self):
        print("\n---------------------------------\n|    Resultados de la encuesta    |\n---------------------------------\n")
        for estudiante in self.respuestas:
            print(estudiante)

    #No aplica resumen

class Estudiante:
    def __init__(self, nombre, edad, idea_proyecto, tiempo, libreria_python, motivacion):
        self.nombre=nombre
        self.edad=edad
        self.idea_proyecto=idea_proyecto
        self.tiempo=tiempo
        self.libreria_python=libreria_python
        self.motivacion=motivacion

    def __str__(self):
        return (f"{self.nombre} ({self.edad} años) | " f"Idea: {self.idea_proyecto} | " f"Tiempo: {self.tiempo} | " f"Librerías: {self.libreria_python} | " f"Motivación: {self.motivacion}/5")


def main():
    preguntas = [
        "¿Cuál es su nombre?",
        "¿Cuántos años tiene?",
        "¿Cuál es su idea de proyecto?",
        "¿Disponibilidad de tiempo? (días en específico, baja, media o alta)",
        "¿Conoce alguna librería de Python? (sí/no, ¿cuál(es)?)",
        "Motivación con el curso (1 a 5)"
    ]

    encuesta = Encuesta(preguntas)

    for i in range(10):
        encuesta.agregar_respuesta()

    encuesta.mostrar_resultados()


if __name__ == "__main__":
    main()