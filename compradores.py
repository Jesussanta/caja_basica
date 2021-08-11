import mysql.connector
from datetime import datetime

class Client:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="compradores")
   


    def __str__(self):
        datos=self.consulta()        
        aux=""
       
        return aux
    def dateNow(self):
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt


    def DeTable (self,ID):
        cur = self.cnn.cursor()
        sql='''DROP TABLE `{}`;'''.format(ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n
    
    def STab (self, ID):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM `{}`".format(ID))
        datos = cur.fetchall()
        cur.close()    
        return datos



    def newTable (self,ID,Valor ):
        cur = self.cnn.cursor()
        sql=''' CREATE TABLE `{}` (`#` INT NOT NULL AUTO_INCREMENT,`ID` INT NOT NULL, `Fecha` TEXT NOT NULL, `Valor` FLOAT NOT NULL,PRIMARY KEY (`#`), UNIQUE INDEX `#_UNIQUE` (`#` ASC) VISIBLE);'''.format(ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        self.insTab(ID,Valor)
        return n

    def consulta (self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM s1")
        datos = cur.fetchall()
        cur.close()    
        return datos
    def maxI (self):
        cur = self.cnn.cursor()
        sql= "select N from factura where N = (select MAX(N) from factura); "
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def buscar (self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM s1 WHERE ID = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def insfa(self,ID,N,F,V):
        dt= str(self.dateNow())
        cur = self.cnn.cursor()
        sql='''INSERT INTO `factura` (`ID`,`Nombre`, `Fecha`,`Valor`) VALUES ('{}','{}', '{}','{}');'''.format(ID,N,F,V)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    


    
    def insTab (self,ID, Valor ):

        dt= str(self.dateNow())
        cur = self.cnn.cursor()
        sql='''INSERT INTO `{}` (`ID`,`Fecha`, `Valor`) VALUES ('{}','{}', '{}');'''.format(ID, ID, dt, Valor)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

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
        self.DeTable(Id)
        return n   

    def modifica (self, ID,Valor ):
        cur = self.cnn.cursor()
        
        sql='''UPDATE `s1` SET `Valor` = '{}' WHERE `ID`= {}'''.format(Valor,ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
