import pickle
from globales import ALUMNOS, MATERIAS, INSCRIPCIONES
from Inscripcion import Inscripcion
from Fecha import Fecha
from Materia import Materia
from Alumno import Alumno
from os import path

ALUMNOS_CSV_FILENAME = "alumnos.tsv"
MATERIAS_CSV_FILENAME = "materias.tsv"
INSCRIPCIONES_CSV_FILENAME = "inscripciones.tsv"

ALUMNOS_BIN_FILENAME = ""
MATERIAS_BIN_FILENAME = ""
INSCRIPCIONES_BIN_FILENAME = "inscripciones.bin"


def escribir_binario_inscripciones():
    with open(INSCRIPCIONES_BIN_FILENAME, 'wb') as archivo_binario:
        pickle.dump(INSCRIPCIONES, archivo_binario)


def inicializar_alumnos():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(ALUMNOS_CSV_FILENAME) and path.isfile(ALUMNOS_CSV_FILENAME):
        pass


def inicializar_materias():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(MATERIAS_CSV_FILENAME) and path.isfile(MATERIAS_CSV_FILENAME):
        pass


def inicializar_inscripciones():
    # chequeamos si el archivo csv existe y en ese caso leemos el archivos que
    # cumple con el formato CSV correcto, volcamos los datos leídos en la lista correspondiente
    # en memoria principal y luego escribimos los mismos datos en un archivo binario.
    if path.exists(MATERIAS_CSV_FILENAME) and path.isfile(MATERIAS_CSV_FILENAME):
        with open(INSCRIPCIONES_CSV_FILENAME, encoding='utf-8') as archivo_tsv:
            todas_las_lineas = archivo_tsv.readlines()
            for linea in todas_las_lineas[1:]:
                columnas = linea[:-1].split('\t')
                id_alumno = columnas[0]
                id_materia = columnas[1]
                fecha_desde_separado = columnas[2].split('/')
                fecha_desde = Fecha(int(fecha_desde_separado[0]), int(fecha_desde_separado[1]),
                                    int(fecha_desde_separado[2]))
                fecha_hasta_separado = columnas[3].split('/')
                fecha_hasta = Fecha(int(fecha_hasta_separado[0]), int(fecha_hasta_separado[1]),
                                    int(fecha_hasta_separado[2]))
                aprobado = True if columnas[4] == 'TRUE' else False
                inscripcion = Inscripcion(id_alumno, id_materia, fecha_desde, fecha_hasta, aprobado)
                INSCRIPCIONES.append(inscripcion)
        escribir_binario_inscripciones()


def mostrar_todo_inscripciones():
    for inscripcion in INSCRIPCIONES:
        print(inscripcion)


def inicializar():
    inicializar_alumnos()
    inicializar_materias()
    inicializar_inscripciones()


inicializar()
mostrar_todo_inscripciones()
