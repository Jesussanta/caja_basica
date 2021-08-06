import mysql.connector

class Client:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="compradores")

    def __str__(self):
        datos=self.consulta()        
        aux=""
       
        return aux
        
    def consulta (self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM s1")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar (self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM s1 WHERE ID = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta (self,ID, Nombre, Valor ):
        cur = self.cnn.cursor()
        sql='''insert into s1 (ID, Nombre, Valor) VALUES('{}', '{}', '{}')'''.format(ID, Nombre, Valor)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina (self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM s1 WHERE ID = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica (self, ID,Valor ):
        cur = self.cnn.cursor()
        
        sql='''UPDATE `s1` SET `Valor` = '{}' WHERE `ID`= {}'''.format(Valor,ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
