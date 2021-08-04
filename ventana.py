from tkinter import *
from tkinter import ttk


    

class Ventana(Frame):
       
    def __init__(self, master=None):
        self.master = master
        self.pack()
        self.create_widgets()
        
    def fNuevo(self):         
        pass
    
    def fGuardar(self):        
        pass
                 
    def fModificar(self):        
        pass
    
    def fEliminar(self):
        pass

    def fCancelar(self):
        pass

    def create_widgets(self):
        frame1 = Frame(self, bg="#0F5C8C")
        frame1.place(x=0,y=0,width=93, height=259)        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="#17A0BF", fg="white",relief=FLAT )
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="#17A0BF", fg="white",relief=FLAT)
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="#17A0BF", fg="white",relief=FLAT)
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        

        frame2 = Frame(self,bg="#45BFB3" )
        frame2.place(x=93,y=0,width=150, height=259)                        
        lbl1 = Label(frame2,text="ID: ")
        
        lbl1.place(x=3,y=5)        
        self.txtISO3=Entry(frame2)
        self.txtISO3.place(x=3,y=25,width=100, height=20)                
        lbl2 = Label(frame2,text="Nombre: ")

        lbl2.place(x=3,y=55)        
        self.txtName=Entry(frame2)
        self.txtName.place(x=3,y=75,width=100, height=20)        
        lbl3 = Label(frame2,text="Valor: ")
        lbl3.place(x=3,y=105)        

        self.txtCapital=Entry(frame2)
        self.txtCapital.place(x=3,y=125,width=100, height=20)        
          
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="#7CA653", fg="white")
        self.btnGuardar.place(x=10,y=160,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="#F2913D", fg="white")
        self.btnCancelar.place(x=80,y=160,width=60, height=30)        


        self.grid = ttk.Treeview(self, columns=("col1","col2","col3"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        
        self.grid.heading("#0", text="#", anchor=CENTER)
        self.grid.heading("col1", text="ID", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Valor", anchor=CENTER)
        
        self.grid.place(x=247,y=0,width=420, height=250)
        
        
        
        
        
        