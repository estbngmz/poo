# IMPORTACION DE LIBRERIAS
# Libreria sqlite
import sqlite3
# Libreria manejo de errores sqlite  
from sqlite3 import Error  
# Libreria manejo de fecha Python
from datetime import datetime
from datetime import time
# Libreria manejo de caracteres
import re


# CODIGO RECURRENTE:
# 1) cursorObj = con.cursor(): recorre la base de datos con el objeto cursor
# 2) Try/Except: evita que el programa se quiebre cuando ya existe la base de datos o alguna tabla, avisa al usuario si se
   # creo o no
# 3) con.commit(): asegura persistencia guardando la tabla en el disco
# 4) cursorObj.execute(): ejecuta una cadena de comando para Sqlite3
# 5) cad = ''' ''': cadena  de comando   para Sqlite3

# OBJETO DE CONEXION:
def Conexion():
    try:
        # Establece la conexion y crea base de datos
        con = sqlite3.connect('MediaMaraton.db')
        print("Se ha creado la base de datos MediaMaraton.db")
        return con
    except: Error
    print(Error)
    print("La base de datos MediaMaraton.db ya existe, no se ha creado una nueva")


# ********** ATLETA **********

# Funcion: crear la tabla de Materias en la base de datos
# Retorna: no retorna
# Parametros: (con: objeto de conexion)
# Variables: (con: sql3)
def CrearTablaAtleta(con):
    cursorObj = con.cursor()
    # Cadena de comando para Sqlite3
    cad = '''CREATE TABLE IF NOT EXISTS Atleta(
            ID text NOT NULL,
            Inscripcion integer NOT NULL,
            Nombre text,
            Apellido text,
            FechaNacimiento date,
            Pais text,
            Ciudad text,
            PRIMARY KEY(ID, Inscripcion))
        '''
    # Crea la tabla Atleta
    try:
        cursorObj.execute(cad)
    except Error:
        print("La tabla Atleta ya existe, no se ha creado una nueva")
    else:
        print("Se ha creado la tabla Atleta en la base de datos MediaMaraton.db")
    con.commit()

# Funcion: recibir la informacion del atleta y escribirla en una lista
# Retorna: lista con la informacion del Atleta
# Parametros: objeto de conexion
# Variables: (codigo: int, nombre: str, facultad: str, departamento: str, creditos: float, idioma: str, materia: list)
def LeerAtleta(con):
    cursorObj = con.cursor()
    # Leer ID
    cursorObj.execute('SELECT ID FROM Atleta')
    controlList = cursorObj.fetchall()
    control = False
    while not control:
        ID = input("Ingrese ID: ")
        if (ID,) in controlList:
            print("El ID ingresado ya existe")
        else:
            validar = re.compile('^[a-zA-Z0-9]+$')
            # Verificamos si la cadena cumple con la validación
            if validar.match(ID):
                control = True
            else:
                print("¡Ingrese un ID válido, sólo letras y números!")      
    ID = ID.ljust(12)  
    # Leer Inscripcion
    cursorObj.execute('SELECT Inscripcion FROM Atleta')
    controlList = cursorObj.fetchall()
    control = False
    while not control:
        Inscripcion = input("Ingrese némero de inscripción: ")
        try:
            Inscripcion = int(Inscripcion)
        except ValueError:
                print("¡Inscripción inválida!")
        else:
            if (Inscripcion,) in controlList:
                print("El número de inscripción ya existe")
            elif Inscripcion < 0:
                print("El número de inscripción no puede ser negativo")
            else:
                Inscripcion = str(Inscripcion)
                control = True
    Inscripcion = Inscripcion.ljust(12)
    # Leer Nombre
    control = False
    while not control:
        Nombre = input("Ingrese nombre: ")
        try:
            Nombre = float(Nombre)
            print("¡Nombre inválido!")
        except ValueError:
            control = True
    Nombre = Nombre.ljust(12)
    # Leer Apellido
    control = False
    while not control:
        Apellido = input("Ingrese apellido: ")
        try:
            Apellido = float(Apellido)
            print("¡Apellido inválido!")
        except ValueError:
            control = True
    Apellido = Apellido.ljust(12)
    # Leer FechaNacimiento
    print("Fecha de Nacimiento:")
    # Leer Año
    control = False
    while not control:
        Ano = input("Ingrese año de nacimiento: ")
        try:
            Ano = int(Ano)
        except ValueError:
            print("¡Año inválido!")
        else:
            if Ano <= 1922:
                print("Los participanes no pueden tener más de 100 años")
            elif Ano >= 2009:
                print("Los participanes no pueden tener menos de 14 años")
            else:
                Ano = str(Ano)
                control = True
    # Leer Mes
    control = False
    while not control:
        Mes = input("Ingrese mes de nacimiento: ")
        try:
            Mes = int(Mes)
        except ValueError:
            print("¡Mes inválido!")
        else:
            if Mes <= 0:
                print("Mes Inválido")
            elif Mes > 12:
                print("Mes Inválido")
            else:
                Mes = str(Mes)
                control = True
    # Leer Dia
    control = False
    while not control:
        Dia = input("Ingrese día de nacimiento: ")
        try:
            Dia = int(Dia)
        except ValueError:
            print("¡Día inválida!")
        else:
            if Dia <= 0:
                print("Día Inválido")
            elif Dia > 31:
                print("Día Inválido")
            else:
                Dia = str(Dia)
                control = True
    FechaNacimientoInput = (Ano+"-"+Mes+"-"+Dia)
    # Convierte la cadena a formato de fecha
    FechaNacimiento = datetime.strptime(FechaNacimientoInput, '%Y-%m-%d').date()
    # Leer Pais
    control = False
    while not control:
        Pais = input("Ingrese país de origen: ")
        try:
            Pais = float(Pais)
            print("¡País inválido!")
        except ValueError:
            control = True  
    Pais = Pais.ljust(12)
    # Leer Ciudad
    control = False
    while not control:
        Ciudad = input("Ingrese ciudad de origen: ")
        try:
            Ciudad = float(Ciudad)
            print("¡Ciudad inválida!")
        except ValueError:
            control = True 
    Ciudad = Ciudad.ljust(12)
    Atleta = (ID, Inscripcion, Nombre, Apellido, FechaNacimiento, Pais, Ciudad)
    return Atleta

# Funcion: escribir informacion del atleta en la tabla Atleta
# Retorna: no
# Parametros: objeto de conexion, lista Atleta
# Variables: (miAtleta: list)
def EscribirTablaAtleta(con, miAtleta):
    cursorObj = con.cursor()
    cad = '''INSERT INTO Atleta VALUES(?, ?, ?, ?, ?, ?, ?)'''
    cursorObj.execute(cad, miAtleta)
    con.commit()

def ConsultarTablaAtleta(con):  # funcion para consultar información en la tabla Materias
    cursorObj = con.cursor()
    cursorObj.execute('SELECT ID FROM Atleta')
    controlList = cursorObj.fetchall()
    print(controlList)
    control = False
    while not control:
        ID = input("Ingrese ID: ")
        ID = ID.ljust(12)
        if (ID,) in controlList:
            ID = str(ID)
            control = True        
        else:
            print("El ID no existe") 
    cursorObj.execute('SELECT* FROM Atleta WHERE ID = "' + ID + '"')
    filas = cursorObj.fetchall()
    print("*ID: "+str(filas[0][0]))
    print("*Inscripcion: "+str(filas[0][1])) 
    print("*Nombre: "+filas[0][2])
    print("*Apellido: "+filas[0][3])
    print("*Fecha de nacimiento: "+str(filas[0][4]))
    print("*Pais: "+filas[0][5])
    print("*Ciudad: "+filas[0][6])

# Función: modificar información en la tabla Materias
# Retorna: lista con la información consultada
# Parámetros: objeto de conexión
# Datos: con: sql3, codmat: int, filas: list, control: bool, control1: bool
def ActualizarTablaAtleta(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT ID FROM Atleta')
    controlList = cursorObj.fetchall()
    control = False
    while not control:
        ID = input("Ingrese ID del atleta a actualizar: ")
        ID = ID.ljust(12)
        if (ID,) in controlList:
            ID = str(ID)
            control = True        
        else:
            print("El ID no existe") 
    control = False
    while not control:
        con.commit()
        cursorObj.execute('SELECT* FROM Atleta WHERE ID = "' + ID + '"')
        filas = cursorObj.fetchall()
        print("*ID: "+str(filas[0][0]))
        print("*Inscripcion: "+str(filas[0][1])) 
        print("*Nombre: "+filas[0][2])
        print("*Apellido: "+filas[0][3])
        print("*Fecha de nacimiento: "+str(filas[0][4]))
        print("*Pais: "+filas[0][5])
        print("*Ciudad: "+filas[0][6])
        opcActualizar = input("""
                            Menú de Actualización

                            1. Actualizar Inscripcion
                            2. Actualizar Nombre
                            3. Actualizar Apellido
                            4. Actualizar Fecha de nacimiento
                            5. Actualizar Pais
                            6. Actualizar ciudad
                            7. Salir del Menú de Actualización

                            Seleccione Opción>>>: """)
        # actualiza la información de la tabla Materias según el código y la opción escogida por el usuario
        if opcActualizar == "1":
            control1 = False
            while not control1:
                Inscripcion = input("Ingrese numero de inscripción: ")
                try:
                    Inscripcion = int(Inscripcion)
                except ValueError:
                        print("¡Inscripción inválida!")
                else:
                    if Inscripcion < 0:
                        print("El número de inscripción no puede ser negativo")
                    else:
                        Inscripcion = str(Inscripcion)
                        control1 = True
                        Inscripcion = Inscripcion.ljust(12)
            cad = 'UPDATE Atleta SET Inscripcion = "' + Inscripcion + '" WHERE ID = "' + ID + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "2":
            control1 = False
            while not control1:
                Nombre = input("Ingrese nombre: ")
                try:
                    Nombre = float(Nombre)
                    print("¡Nombre inválido!")
                except ValueError:
                    control1 = True
            Nombre = Nombre.ljust(12)
            cad = 'UPDATE Atleta SET Nombre = "' + Nombre + '" WHERE ID = "' + ID + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "3":
            control1 = False
            while not control1:
                Apellido = input("Ingrese apellido: ")
                try:
                    Apellido = float(Apellido)
                    print("¡Apellido inválido!")
                except ValueError:
                    control1 = True
            Apellido = Apellido.ljust(12)
            cad = 'UPDATE Atleta SET Apellido = "' + Apellido + '" WHERE ID = "' + ID + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "4":
            control1 = False
            # Leer FechaNacimiento
            print("Fecha de Nacimiento:")
            # Leer Año
            control1 = False
            while not control1:
                Ano = input("Ingrese año de nacimiento: ")
                try:
                    Ano = int(Ano)
                except ValueError:
                    print("¡Año inválido!")
                else:
                    if Ano <= 1922:
                        print("Los participanes no pueden tener más de 100 años")
                    elif Ano >= 2009:
                        print("Los participanes no pueden tener menos de 14 años")
                    else:
                        Ano = str(Ano)
                        control1 = True
            # Leer Mes
            control1 = False
            while not control1:
                Mes = input("Ingrese mes de nacimiento: ")
                try:
                    Mes = int(Mes)
                except ValueError:
                    print("¡Mes inválido!")
                else:
                    if Mes <= 0:
                        print("Mes Inválido")
                    elif Mes > 12:
                        print("Mes Inválido")
                    else:
                        Mes = str(Mes)
                        control1 = True
            # Leer Dia
            control1 = False
            while not control1:
                Dia = input("Ingrese día de nacimiento: ")
                try:
                    Dia = int(Dia)
                except ValueError:
                    print("¡Día inválida!")
                else:
                    if Dia <= 0:
                        print("Día Inválido")
                    elif Dia > 31:
                        print("Día Inválido")
                    else:
                        Dia = str(Dia)
                        control1 = True
            FechaNacimientoInput = (Ano+"-"+Mes+"-"+Dia)
            # Convierte la cadena a formato de fecha
            FechaNacimiento = datetime.strptime(FechaNacimientoInput, '%Y-%m-%d').date()
            cad = 'UPDATE Atleta SET FechaNacimiento = "' + str(FechaNacimiento) + '" WHERE ID = "' + ID + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "5":
            control1 = False
            while not control1:
                Pais = input("Ingrese país de origen: ")
                try:
                    Pais = float(Pais)
                    print("¡País inválido!")
                except ValueError:
                    control1 = True  
            Pais = Pais.ljust(12)
            cad = 'UPDATE Atleta SET Pais = "' + Pais + '" WHERE ID = "' + ID + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "6":
            control1 = False
            while not control:
                Ciudad = input("Ingrese ciudad de origen: ")
                try:
                    Ciudad = float(Ciudad)
                    print("¡Ciudad inválida!")
                except ValueError:
                    control1 = True 
            Ciudad = Ciudad.ljust(12)
            cad = 'UPDATE Atleta SET Ciudad = "' + Ciudad + '" WHERE ID = "' + ID + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "6":
            print("Se actualizo el atleta")
            control = True

def CrearTablaResultados(con):
    cursorObj = con.cursor()
    # Cadena de comando para Sqlite3
    cad = '''CREATE TABLE IF NOT EXISTS Resultados(
            Inscripcion text NOT NULL,
            Evento integer NOT NULL,
            Posicion integer,
            Tiempo date,
            Estado text,
            PRIMARY KEY(Evento, Inscripcion))
        '''
    # Crea la tabla Resultado
    try:
        cursorObj.execute(cad)
    except Error:
        print("La tabla Resultados ya existe, no se ha creado una nueva")
    else:
        print("Se ha creado la tabla Resultados en la base de datos MediaMaraton.db")
    con.commit()

def LeerResultado(con):
    Inscripcion = input("Numero de inscripcion: ")
    Inscripcion = Inscripcion.ljust(12)
    Evento = input("Numero de evento: ")
    Evento = Evento.ljust(12)
    Posicion = input("Posicion en la carrera: ")
    Posicion = Posicion.ljust(12)
    TiempoInput = input("Tiempo empleado (HH:MM): ")
    try:
        Tiempo = datetime.strptime(TiempoInput, '%H:%M').time()
        Tiempo = str(Tiempo)
        # FechaNacimiento = datetime.strptime(FechaNacimientoInput, '%Y-%m-%d').date()
    except ValueError:
        print("Formato de tiempo incorrecto, se asignará 00:00")
        Tiempo = datetime.strptime("00:00", '%H:%M').time() 
        Tiempo = str(Tiempo)   
    Estados = { "1":"Finalizo",
        "2":"Retiro",
        "3":"Descalificado"}
    leerEstado = input('''Estado:
     1) Finalizó
     2) Retiro
     3) Descalificado
        
    Seleccione un estado: ''')
    Estado = (Estados[leerEstado])
    Resultado = (Inscripcion, Evento, Posicion, Tiempo, Estado)
    return Resultado

def EscribirTablaResultados(con, miResultado):
    cursorObj=con.cursor()
    cad='''INSERT INTO Resultados VALUES(?, ?, ?, ?, ?)
        '''
    cursorObj.execute(cad, miResultado)
    con.commit()

def ActualizarTablaResultados(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT Inscripcion FROM Resultados')
    controlList = cursorObj.fetchall()
    control = False
    while not control:
        Inscripcion = input("Ingrese numero de inscripcion del atleta a actualizar: ")
        Inscripcion = Inscripcion.ljust(12)
        if (Inscripcion,) in controlList:
            Inscripcion = str(Inscripcion)
            control = True        
        else:
            print("El numero de inscripcion no existe") 
    control = False
    while not control:
        con.commit()
        cursorObj.execute('SELECT* FROM Resultados WHERE Inscripcion = "' + Inscripcion + '"')
        filas = cursorObj.fetchall()
        print("*Inscripcion: "+str(filas[0][0]))
        print("*Evento: "+str(filas[0][1])) 
        print("*Posicion: "+str(filas[0][2]))
        print("*Tiempo: "+filas[0][3])
        print("*Estado: "+str(filas[0][4]))
        opcActualizar = input("""
                            Menú de Actualización

                            1. Actualizar Evento
                            2. Actualizar Posicion
                            3. Actualizar Tiempo
                            4. Actualizar Estado
                            5. Salir del Menú de Actualización

                            Seleccione Opción>>>: """)
        # actualiza la información de la tabla Materias según el código y la opción escogida por el usuario
        if opcActualizar == "1":
            control1 = False
            while not control1:
                Evento = input("Ingrese número de evento: ")
                try:
                    Evento = int(Evento)
                except ValueError:
                        print("¡Evento inválido!")
                else:
                    if Evento <= 0:
                        print("El número de evento no puede ser negativo")
                    else:
                        Evento = str(Evento)
                        control1 = True
            cad = 'UPDATE Resultados SET Evento = "' + Evento + '" WHERE Inscripcion = "' + Inscripcion + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "2":
            control1 = False
            while not control1:
                Posicion = input("Ingrese posicion: ")
                try:
                    Posicion = int(Posicion)
                except ValueError:
                        print("¡Inscripción inválida!")
                else:
                    if Posicion <= 0:
                        print("El número de evento no puede ser negativo")
                    else:
                        Posicion = str(Posicion)
                        Posicion = Posicion.ljust(12)
                        control1 = True                     
            cad = 'UPDATE Resultados SET Posicion = "' + Posicion + '" WHERE Inscripcion = "' + Inscripcion + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "3":
            control1 = False
            while not control1:
                TiempoInput = input("Tiempo empleado (HH:MM): ")
                try:
                    Tiempo = datetime.strptime(TiempoInput, '%H:%M').time()
                    Tiempo = str(Tiempo)
                    control1 = True
                except ValueError:
                    print("Formato de tiempo incorrecto, se asignará 00:00")
                    Tiempo = datetime.strptime("00:00", '%H:%M').time() 
                    Tiempo = str(Tiempo) 
            cad = 'UPDATE Resultados SET Tiempo = "' + Tiempo + '" WHERE Inscripcion = "' + Inscripcion + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "4":
            control1 = False
            Estados = { "1":"Finalizo",
                       "2":"Retiro",
                       "3":"Descalificado"}
            leerEstado = input('''Estado:
            1) Finalizó
            2) Retiro
            3) Descalificado
        
            Seleccione un estado: ''')
            Estado = (Estados[leerEstado])
            cad = 'UPDATE Resultados SET Estado = "' + Estado + '" WHERE Inscripcion = "' + Inscripcion + '"'
            cursorObj.execute(cad)
        elif opcActualizar == "5":
            print("Se actualizo el resultado")
            control = True

def ConsultarTablaResultados(con):  # funcion para consultar información en la tabla Materias
    cursorObj = con.cursor()
    cursorObj.execute('SELECT Inscripcion FROM Resultados')
    controlList = cursorObj.fetchall()
    control = False
    while not control:
        Inscripcion = input("Ingrese Inscripcion: ")
        Inscripcion = Inscripcion.ljust(12)
        if (Inscripcion,) not in controlList:
            print("El numero de inscripcion ingresado no existe")
        else:
            control = True
    cursorObj.execute('SELECT* FROM Resultados WHERE Inscripcion = "' + Inscripcion + '"')
    filas = cursorObj.fetchall()
    print("*Inscripcion: "+str(filas[0][0]))
    print("*Evento: "+str(filas[0][1])) 
    print("*Posicion: "+str(filas[0][2]))
    print("*Tiempo: "+str(filas[0][3]))
    print("*Estado: "+(filas[0][4]))

def CrearTablaClasificacion(con):
    cursorObj=con.cursor()
    cad='''CREATE TABLE IF NOT EXISTS Clasificacion(
            Inscripcion text NOT NULL,
            Evento text NOT NULL,
            Nombre text,
            Apellido text,
            FechaNacimiento date,
            Pais text,
            Ciudad text,
            Tiempo date,
            PRIMARY KEY (Inscripcion, Evento))'''
    try:
        cursorObj.execute(cad)
    except Error:
        print("La tabla Clasificacion ya existe, no se ha creado una nueva")
    else:
        print("Se ha creado la tabla Clasificacion en la base de datos MediaMaraton.db")
    con.commit()

def EscribirTablaClasificacion(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT Inscripcion FROM Resultados')
    InscripcionList = cursorObj.fetchall()
    cursorObj.execute('SELECT Evento FROM Resultados')
    EventoList = cursorObj.fetchall()
    j = 0
    for i in InscripcionList:
        Inscripcion = str(i[0])
        #print(EventoList[j][0])
        Evento = str(EventoList[j][0])
        j += 1
        cursorObj.execute('SELECT Nombre FROM Atleta WHERE Inscripcion = "' + Inscripcion +'"')
        Nombre = cursorObj.fetchall()[0][0]
        cursorObj.execute('SELECT Apellido FROM Atleta WHERE Inscripcion = "' + Inscripcion +'"')
        Apellido = cursorObj.fetchall()[0][0]
        cursorObj.execute('SELECT FechaNacimiento FROM Atleta WHERE Inscripcion = "' + Inscripcion +'"')
        FechaNacimiento = cursorObj.fetchall()[0][0]
        cursorObj.execute('SELECT Pais FROM Atleta WHERE Inscripcion = "' + Inscripcion +'"')
        Pais = cursorObj.fetchall()[0][0]
        cursorObj.execute('SELECT Ciudad FROM Atleta WHERE Inscripcion = "' + Inscripcion +'"')
        Ciudad = cursorObj.fetchall()[0][0]
        Inscripcion = Inscripcion.ljust(12)
        cursorObj.execute('SELECT Tiempo FROM Resultados WHERE Inscripcion = "' + Inscripcion +'" AND Evento = "' + Evento +'"')
        Tiempo = cursorObj.fetchall()[0][0]
        Inscripcion = str(i[0])
        Clasificacion = (Inscripcion, Evento, Nombre, Apellido, FechaNacimiento, Pais, Ciudad, Tiempo)
    cad=('''INSERT INTO Clasificacion VALUES(?,?,?,?,?,?,?,?) ''')
    cursorObj.execute(cad, Clasificacion)
    con.commit()

def ConsultarTablaClasificacion(con):  # funcion para consultar información en la tabla Materias
    cursorObj = con.cursor()
    cursorObj.execute('SELECT Inscripcion FROM Resultados')
    controlList = cursorObj.fetchall()
    control = False
    while not control:
        Inscripcion = input("Ingrese Inscripcion: ")
        Inscripcion = Inscripcion.ljust(12)
        Evento = input("Ingrese Evento: ")
        if (Inscripcion,) not in controlList:
            print("El numero de inscripcion ingresado no existe")
        else:
            control = True
    cursorObj.execute('SELECT* FROM Clasificacion WHERE Inscripcion = "' + Inscripcion + '" AND Evento = "' + Evento +'"')
    filas = cursorObj.fetchall()
    print("*Inscripcion: "+str(filas[0][0]))
    print("*Evento: "+str(filas[0][1])) 
    print("*Nombre: "+str(filas[0][2]))
    print("*Apellido: "+str(filas[0][3]))
    print("*Fecha de nacimiento: "+(filas[0][4]))
    print("*Pais: "+str(filas[0][5]))
    print("*Ciudad: "+str(filas[0][6]))
    print("*Tiempo: "+str(filas[0][7]))

def CrearTablaCarrera(con):
    cursorObj=con.cursor()
    cad = '''CREATE TABLE IF NOT EXISTS Carrera(
            Evento text NOT NULL,
            Ano integer,
            Premio1 text,
            Premio2 text,
            Premio3 text,
            PRIMARY KEY (Evento))'''
    cursorObj.execute(cad)
    try:
        cursorObj.execute(cad)
    except Error:
        print("La tabla Carrera ya existe, no se ha creado una nueva")
    else:
        print("Se ha creado la tabla Carrera en la base de datos MediaMaraton.db")
    con.commit()

def LeerCarrera():
    Evento = input("Numero de evento: ")
    Evento = Evento.ljust(12)
    Ano = input("Año de la carrera: ")
    Premio1 = input("Premio 1er puesto: ")
    Premio2 = input("Premio 2do puesto: ")
    Premio3 = input("Premio 3er puesto: ")
    Carrera = (Evento, Ano, Premio1, Premio2, Premio3)
    return Carrera

def EscribirTablaCarrera(con, miCarrera):
    cursorObj=con.cursor()
    cad='''INSERT INTO Carrera VALUES(?, ?, ?, ?, ?)
        '''
    cursorObj.execute(cad, miCarrera)
    con.commit()

def cerrar_bd(con):
    con.close()

def main():
    Con = Conexion()
    control = False
    while not control:  # bucle menú principal
        CrearTablaAtleta(Con)
        CrearTablaResultados(Con)
        CrearTablaClasificacion(Con)
        CrearTablaCarrera(Con)
        EscribirTablaClasificacion(Con)
        opcPrincipal = input("""
                        Menú de opciones

                        1. Atleta
                        2. Resultados
                        3. Clasificacion
                        4. Carrera
                        5. Salir del Programa

                        Seleccione opción>>>: """)
        print()
        # abre un menú según el menú elegido por el usuario
        if opcPrincipal == "1":
            control1 = False  # control de permanencia en el menú
            while not control1:  # bucle menú Atleta
                opcAtleta = input("""
                                    Menú de Atleta

                                    1. Crear Atleta
                                    2. Consultar Atleta
                                    3. Actualizar Atleta
                                    4. Volver al Menú Principal
                                    5. Salir del programa

                                    Seleccione Opción>>>: """)
                print()
                # accede a una función del menú según la función elegida por el usuario
                if opcAtleta == "1":
                    AtletaCreado = LeerAtleta(Con)
                    EscribirTablaAtleta(Con, AtletaCreado)
                elif opcAtleta == "2":
                    ConsultarTablaAtleta(Con)
                elif opcAtleta == "3":
                    EscribirTablaAtleta(Con, AtletaCreado)
                elif opcAtleta == "4":
                    control1 = True  # control de salida del menú
                elif opcAtleta == "5":
                    cerrar_bd(Con)
                    print("PROGRAMA FINALIZADO")
                    control1 = True  # control de salida del menú
                    control = True  # control de salida del menú
        if opcPrincipal == "2":
            control1 = False  # control de permanencia en el menú
            while not control1: # bucle menú Resultados
                opcResultados = input("""
                                    Menú de Resultados

                                    1. Crear Resultados
                                    2. Consultar Resultados
                                    3. Actualizar Resultados
                                    4. Volver al Menú Principal 
                                    5. Salir del programa

                                    Seleccione Opción>>>: """)
                print()
                if opcResultados == "1":
                    ResultadoCreado = LeerResultado(Con)
                    EscribirTablaResultados(Con, ResultadoCreado)
                elif opcResultados == "2":
                    ConsultarTablaResultados(Con)
                elif opcResultados == "3":
                    ActualizarTablaResultados(Con) 
                elif opcResultados == "4":
                    control1 = True  # control de salida del menú
                elif opcResultados == "5":
                    cerrar_bd(Con)
                    print("PROGRAMA FINALIZADO")
                    control1 = True  # control de salida del menú
                    control = True  # control de salida del menú
        if opcPrincipal == "3":
            control1 = False  # control de permanencia en el menú
            while not control1: # bucle menú Clasificacion
                opcClasificacion = input("""
                                    Menú de Clasificacion

                                    1. Consultar Clasificacion
                                    2. Volver al Menú Principal 
                                    3. Salir del Programa

                                    Seleccione Opción>>>: """)
                print()
                if opcClasificacion == "1":
                    ConsultarTablaClasificacion(Con)  
                elif opcClasificacion == "2":
                    control1 = True  # control de salida del menú
                elif opcClasificacion == "3":
                    cerrar_bd(Con)
                    print("PROGRAMA FINALIZADO")
                    control = True  # control de salida del menú
                    control = True  # control de salida del menú
        if opcPrincipal == "4":
            control1 = False  # control de permanencia en el menú
            while not control1: # bucle menú Carrera
                opcCarrera = input("""
                                            Menú de Carrera

                                            1. Crear Carrera
                                            2. Volver al Menú Principal
                                            3. Salir del Programa

                                            Seleccione Opción>>>: """)
                print()
                if opcCarrera == "1":
                    CarreraCreada = LeerCarrera(Con)
                    EscribirTablaCarrera(Con, CarreraCreada)
                elif opcCarrera == "2":
                    control1 = True  # control de salida del menú
                elif opcCarrera == "3":
                    cerrar_bd(Con)
                    print("PROGRAMA FINALIZADO")
                    control1 = True  # control de salida del menú
                    control = True  # control de salida del menú
        if opcPrincipal == "5":
            cerrar_bd(Con)
            print("PROGRAMA FINALIZADO")
            control = True  # control de salida del menú

main()

    #AtletaCreado = LeerAtleta(Con)
    #ResultadoCreado = LeerResultado(Con)
    #CarreraCreada = LeerCarrera(Con)
    #EscribirTablaAtleta(Con, AtletaCreado)
    #EscribirTablaResultados(Con, ResultadoCreado)
    #EscribirTablaClasificacion(Con)
    #EscribirTablaCarrera(Con, CarreraCreada)
    #ActualizarTablaAtleta(Con)
    #ActualizarTablaResultados(Con)
    #ConsultarTablaAtleta(Con)
    #ConsultarTablaResultados(Con)
    #ConsultarTablaClasificacion(Con)