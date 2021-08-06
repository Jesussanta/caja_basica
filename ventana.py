from logging import disable
from tkinter import *
from tkinter import ttk
from compradores import * 

    

class Ventana(Frame):
    
    Seller = Client()
    cont = 0   
    def __init__(self, master=None):
        
        super().__init__(master,width=700, height=260)
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
            self.btnAdd.configure(bg="#03738C",fg="white")
            self.btnDelet.configure(bg="#013440",fg="white")
            self.btnChan.configure(bg="#013440",fg="white")
            self.btnShow.configure(bg="#013440",fg="white")
        elif bn == 2:
            self.btnDelet.configure(bg="#03738C",fg="white")
            self.btnAdd.configure(bg="#013440",fg="white")
            self.btnChan.configure(bg="#013440",fg="white")
            self.btnShow.configure(bg="#013440",fg="white")
        elif bn == 3:
            self.btnChan.configure(bg="#03738C",fg="white")
            self.btnDelet.configure(bg="#013440",fg="white")
            self.btnAdd.configure(bg="#013440",fg="white")
            self.btnShow.configure(bg="#013440",fg="white")
        elif bn ==4:
            self.btnAdd.configure(bg="#013440",fg="white")
            self.btnDelet.configure(bg="#013440",fg="white")
            self.btnChan.configure(bg="#013440",fg="white")
            self.btnShow.configure(bg="#03738C",fg="white")
        else:
            self.btnAdd.configure(bg="#013440",fg="white")
            self.btnDelet.configure(bg="#013440",fg="white")
            self.btnChan.configure(bg="#013440",fg="white")
            self.btnShow.configure(bg="#013440",fg="white")

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
        if self.cont ==1:
            try:
                self.Seller.inserta(self.txtID.get(),self.txtName.get(),self.txtValue.get())
                self.lbl4.config(text="")
                self.cBox()
                self.datos()
                
            except:
                self.lbl4.config(text="Valores invalidos.")
        elif self.cont ==2:
            try:
                self.Seller.elimina(self.txtID.get())
                self.lbl4.config(text="")
                self.cBox()
                self.datos()

            except:
                self.lbl4.config(text="ID inexistente.")


        elif self.cont == 3: #Show
            self.Busc()
            
        
        elif self.cont == 4:
           try:
               self.lbl4.config(text="")
               self.Val()
           except:
               self.lbl4.config(text="ID Erronea.")
                
            
          
 
    def create_widgets(self):
        frame1 = Frame(self, bg="#013440")
        frame1.place(x=0,y=0,width=100, height=259)        

        self.btnAdd=Button(frame1,text="Añadir", command=self.bAdd, bg="#013440", fg="white",relief=FLAT, )
        self.btnAdd.place(x=10,y=50,width=80, height=30 )        
        self.btnDelet=Button(frame1,text="Eliminar", command=self.bDelet, bg="#013440", fg="white",relief=FLAT)
        self.btnDelet.place(x=10,y=90,width=80, height=30)        
        self.btnShow=Button(frame1,text="Explorar", command=self.bShow, bg="#013440", fg="white",relief=FLAT)
        self.btnShow.place(x=10,y=130,width=80, height=30)
        self.btnChan=Button(frame1,text="Modificar", command=self.bChan, bg="#013440", fg="white",relief=FLAT)
        self.btnChan.place(x=10,y=200,width=80, height=30)    

        frame2 = Frame(self,bg="#03738C" )
        frame2.place(x=100,y=0,width=150, height=259)                        
        lbl1 = Label(frame2,text="ID: ",bg="#03738C",fg="white")        
        lbl1.place(x=30,y=5)        
        self.txtID=Entry(frame2)
        self.txtID.place(x=30,y=25,width=100, height=20)                
        lbl2 = Label(frame2,text="Nombre: ",bg="#03738C",fg="white")

        lbl2.place(x=30,y=55)        
        self.txtName=Entry(frame2)
        self.txtName.place(x=30,y=75,width=100, height=20)        
        lbl3 = Label(frame2,text="Valor: ",bg="#03738C",fg="white")
        lbl3.place(x=30,y=105)        
    
        self.lbl4 = Label(frame2,text="",bg="#03738C",fg="white")
        self.lbl4.place(x=30,y=210)        

        self.txtValue=Entry(frame2)
        self.txtValue.place(x=30,y=125,width=100, height=20)        
          
        self.btnGuardar=Button(frame2,text="Guardar", command=self.bSave, bg="#039691", fg="white",relief=FLAT)
        self.btnGuardar.place(x=50,y=160,width=60, height=30)        
       


        self.grid = ttk.Treeview(self, columns=("col1","col2","col3"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        
        self.grid.heading("#0", text="#", anchor=CENTER)
        self.grid.heading("col1", text="ID", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Valor", anchor=CENTER)
        
        self.grid.place(x=250,y=0,width=420, height=250)
        
        
        
        
        
        