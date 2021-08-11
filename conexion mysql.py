# conexion

import mysql.connector as sql

conexion = sql.connect(host = 'poner el host',
                       database = 'poner la base de datos',
                       user = 'poner el usuario',
                       password = 'poner la clave')

cursor = conexion.cursor()



# ejemplo query del dni

consultadni = 'SELECT dni FROM alumnos'
cursor.execute(consultadni)
listadni = [dni[0] for dni in cursor] 

    
# cargar a la base de datos
    
while True:
    
    database = input('Desea cargar una base de datos? (Si/No): \n')
    
    if database == 'No':
        print('Muchas gracias\n')
        break
    elif database == 'Si':
        print('Excelente, por favor comienza con tu dni para validarte en la base de datos\n')
        
        while True:
            dni = int(input('Ingrese su dni: \n'))
            if dni in listadni:
                print('el dni ya se encuentra en la base de datos\n')
                break
            else:
                nombre = input('Ingrese su nombre: \n')
                apellido = input('Ingrese su apellido: \n')
                email = input('Ingrese su email: \n')     
                fecha_nac = input('Ingrese su fecha de nacimiento (AAAA-MM-DD): \n')
                query = 'INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES (%s,   %s,%s,%s,%s)'
                cursor.execute(query, (nombre, apellido, dni, email,fecha_nac))
                conexion.commit()
                print('Datos subidos')
                break
    else:
        print('Por favor respetar consignas')

# cerrar

cursor.close()
conexion.close()
