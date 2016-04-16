import sqlite3

def tabla():
    try:
        print("BIENVENIDO")
        conexion= sqlite3.connect("C:/Users/mario/Desktop/sqlite3/db")
        consulta = conexion.cursor()
        sql = """CREATE TABLE db (
         NOMBRE  CHAR(20) NOT NULL,
         APELLIDO  CHAR(20),
         EDAD INT,
         SEXO CHAR(1) )"""

        if (consulta.execute(sql)):
            print("Tabla creada con éxito")

    except Exception:
        print("hubo error en la conexion")

        consulta.close()
        conexion.commit()
        conexion.close()

def ingresar_datos ():

    NOMBRE=input("ingresar tu nombre")
    APELLIDO=input("ingresa tu apellido")
    EDAD=input("ingresar edad")

    conexion=sqlite3.connect("C:/Users/mario/Desktop/sqlite3/db")
    consulta=conexion.cursor()
    argumentos=(NOMBRE,APELLIDO,EDAD)

    sql="""
    INSERT INTO db (NOMBRE,APELLIDO,EDAD)
    VALUES (?,?,?)
    """
    if(consulta.execute(sql,argumentos)):

        print("registro guardo con exito" )
    else : print("error")
    consulta.close()

    conexion.commit()
    conexion.close()

if __name__=="__main__":
    tabla()
    ingresar_datos()