from logging import disable
from tkinter import *
from tkinter import ttk
from compradores import * 

    

class Ventana(Frame):
    
    Seller = Client()
    cont = 0   
    def __init__(self, master=None):
        
        super().__init__(master,width=1280, height=720)
        self.master = master
        self.pack()
        self.create_widgets()
        self.datos()
        self.habili(5)

    def datos(self):
        datos = self.Seller.consulta()
        for row in datos:
            self.grid.insert("",END, text= row[0], values=(row[1],row[2],row[3]))
    def habilib(self,bn):
        if bn == 1:
            self.btnAdd.configure(bg="#263238",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn == 2:
            self.btnDelet.configure(bg="#263238",fg="white")
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn == 3:
            self.btnChan.configure(bg="#263238",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn ==4:
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#263238",fg="white")
        else:
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")

    def habili(self,bn):
        if bn == 1:
            self.txtName.configure(state="normal")
            self.txtID.configure(state="normal")
            self.txtValue.configure(state="normal")
        elif bn == 2:
            self.txtName.configure(state="disabled")
            self.txtID.configure(state="normal")
            self.txtValue.configure(state="disabled")
        elif bn ==3:
            self.txtName.configure(state="disabled")
            self.txtID.configure(state="normal")
            self.txtValue.configure(state="normal")
        else:
            self.txtName.configure(state="disabled")
            self.txtID.configure(state="disabled")
            self.txtValue.configure(state="disabled")

    def clGrip(self):
        for i in self.grid.get_children():
            self.grid.delete(i)
        
    def cBox(self):
        self.txtName.delete(0,END)
        self.txtID.delete(0,END)
        self.txtValue.delete(0,END)

    def Busc(self):
        if self.txtID.get() == "":
                self.datos()
        else:
            try:
                dat=self.Seller.buscar(self.txtID.get())
                self.lbl4.config(text="")
                self.grid.insert("",END, text= str(dat[0]), values=(str(dat[1]),str(dat[2]),str(dat[3])))
                
            except:
                self.lbl4.config(text="ID inexistente.")
                self.datos()


    def Val(self):
        vAc=self.Seller.buscar(self.txtID.get())
        #print(vAc)
        nV = self.txtValue.get()
        nR=str(float(vAc[3]) + float(nV))

        self.grid.insert("",END, text= str(vAc[0]), values=(str(vAc[1]),str(vAc[2]),str(vAc[3])))
        self.grid.insert("",END, text= str(""), values=(str(""),str(""),str(nV)))
        self.grid.insert("",END, text= str(vAc[0]), values=(str(vAc[1]),str(vAc[2]),str(nR)))

        self.Seller.modifica(vAc[1],str(nR))
        self.lbl4.config(text="Valor actualizado.")
        self.cBox()

               
    def bAdd(self):
        self.lbl4.config(text="")     
        self.habili(1)    
        self.habilib(1)
        self.cBox()
        self.txtID.focus()
        self.cont = 1
        pass
        
                 
    def bChan(self):        
        self.lbl4.config(text="")
        self.habili(3)
        self.habilib(3)    
        self.cBox()
        self.txtID.focus()
        self.cont = 4
        pass
    
    def bDelet(self):
        self.lbl4.config(text="")
        self.habili(2) 
        self.habilib(2)   
        self.cBox()
        self.txtID.focus()  
        self.cont = 2

    def bShow(self):
        self.lbl4.config(text="")
        self.habili(2)
        self.habilib(4)    
        self.txtID.focus()    
        self.cBox()
        self.cont = 3
       

    def bSave(self): 
        self.clGrip()
        if self.cont ==1: #Add
            try:
                self.Seller.inserta(self.txtID.get(),self.txtName.get(),self.txtValue.get())
                self.lbl4.config(text="")
                self.cBox()
                self.datos()
                
            except:
                self.lbl4.config(text="Valores invalidos.")

        elif self.cont ==2: #Delet
            try:
                self.Seller.elimina(self.txtID.get())
                self.lbl4.config(text="")
                self.cBox()
                self.datos()

            except:
                self.lbl4.config(text="ID inexistente.")


        elif self.cont == 3: #Show
            self.Busc()
            
        
        elif self.cont == 4: #Change
           try:
               self.lbl4.config(text="")
               self.Val()
           except:
               self.lbl4.config(text="ID Erronea.")
                
            
          
 
    def create_widgets(self):
        frame1 = Frame(self, bg="#20292E")
        frame1.place(x=0,y=0,width=100, height=720)        

        self.btnAdd=Button(frame1,text="Añadir", command=self.bAdd, bg="#20292E", fg="white",relief=FLAT, )
        self.btnAdd.place(x=10,y=140,width=80, height=30 )        
        self.btnDelet=Button(frame1,text="Eliminar", command=self.bDelet, bg="#20292E", fg="white",relief=FLAT)
        self.btnDelet.place(x=10,y=210,width=80, height=30)        
        self.btnShow=Button(frame1,text="Explorar", command=self.bShow, bg="#20292E", fg="white",relief=FLAT)
        self.btnShow.place(x=10,y=280,width=80, height=30)
        self.btnChan=Button(frame1,text="Modificar", command=self.bChan, bg="#20292E", fg="white",relief=FLAT)
        self.btnChan.place(x=10,y=650,width=80, height=30)    

        frame2 = Frame(self,bg="#263238" )
        frame2.place(x=100,y=0,width=300, height=720)                        
        lbl1 = Label(frame2,text="ID: ",bg="#263238",fg="white")        
        lbl1.place(x=30,y=5+100)        
        self.txtID=Entry(frame2)
        self.txtID.place(x=30,y=25+100,width=160, height=20)                
        lbl2 = Label(frame2,text="Nombre: ",bg="#263238",fg="white")

        lbl2.place(x=30,y=55+110)        
        self.txtName=Entry(frame2)
        self.txtName.place(x=30,y=75+110,width=160, height=20)        
        lbl3 = Label(frame2,text="Valor: ",bg="#263238",fg="white")
        lbl3.place(x=30,y=105+120)        
    
        self.lbl4 = Label(frame2,text="",bg="#263238",fg="white",font=( NORMAL, 11))
 
        self.lbl4.place(x=35,y=500)        

        self.txtValue=Entry(frame2)
        self.txtValue.place(x=30,y=125+120,width=160, height=20)        
          
        self.btnGuardar=Button(frame2,text="Guardar", command=self.bSave, bg="#05867B", fg="white",relief=FLAT)
        self.btnGuardar.place(x=70,y=160+200,width=60, height=30)        
       


        self.grid = ttk.Treeview(self, columns=("col1","col2","col3"))        
        self.grid.column("#0",width=20)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=100, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        
        self.grid.heading("#0", text="#", anchor=CENTER)
        self.grid.heading("col1", text="ID", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Valor", anchor=CENTER)
        
        self.grid.place(x=310,y=0,width=970, height=720)
        
        
        
        
        
        