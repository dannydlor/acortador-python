from src.config.db import DB

class EnlacesModel():
    def traerTodos(self):
        cursor = DB.cursor()
        cursor.execute('select * from enlaces ')
        enlaces = cursor.fetchall()
        cursor.close()
        return enlaces

    def insertar_enlaces(self, enlaces,cortos):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO enlaces(enlaces,cortos) VALUES(%s,%s)',(enlaces,cortos,) )  
        cursor.close()
    
    def traer_un_enlaces(self,consultor):
        cursor = DB.cursor()
        cursor.execute("SELECT enlaces FROM enlaces WHERE cortos=%s;",(consultor,) )
        encontrado = cursor.fetchall()
        cursor.close()
        return encontrado

    
 
        