from logging import disable
from tkinter import *
from tkinter import ttk
from fpdf import FPDF
from compradores import * 



class Ventana(Frame):
    
    Seller = Client()
    cont = 0  
    So = ""
     
    def __init__(self, master=None):
        
        super().__init__(master,width=1280, height=720)
        self.master = master
        self.pack()
        self.create_widgets()
        self.bha(5)
        self.habili(5)

    def datos(self,k):
        datos = self.Seller.consulta(k)
        for row in datos:
            self.grid.insert("",END, text= row[0], values=(row[1],row[2],row[3],row[4]))

    def habilib(self,bn):
        if bn == 1:
            self.btnAdd.configure(bg="#2F3E45",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn == 2:
            self.btnDelet.configure(bg="#2F3E45",fg="white")
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn == 3:
            self.btnChan.configure(bg="#2F3E45",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn ==4:
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#2F3E45",fg="white")
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
            self.txtDes.configure(state="normal")
        elif bn == 2:
            self.txtName.configure(state="disabled")
            self.txtID.configure(state="normal")
            self.txtValue.configure(state="disabled")
            self.txtDes.configure(state="disabled")
        elif bn ==3:
            self.txtName.configure(state="disabled")
            self.txtID.configure(state="normal")
            self.txtValue.configure(state="normal")
            self.txtDes.configure(state="normal")
                    
        else:
            self.txtName.configure(state="disabled")
            self.txtID.configure(state="disabled")
            self.txtValue.configure(state="disabled")
    def bha(self,k):
        if k == 1 :
            self.btnAdd.configure(state="normal")
            self.btnShow.configure(state="normal")
            self.btnDelet.configure(state="normal")
            self.btnChan.configure(state="normal")
        else:
            self.btnAdd.configure(state="disabled")
            self.btnShow.configure(state="disabled")
            self.btnDelet.configure(state="disabled")
            self.btnChan.configure(state="disabled")
            
    def clGrip(self):
        for i in self.grid.get_children():
            self.grid.delete(i)
        
    def cBox(self):
        self.txtName.delete(0,END)
        self.txtID.delete(0,END)
        self.txtValue.delete(0,END)
        self.txtDes.delete(0,END)
    def gripb (self):
        self.grid.heading("#0", text="#", anchor=CENTER)
        self.grid.heading("col1", text="ID", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Valor", anchor=CENTER)
        self.grid.heading("col4", text="Descripcíon", anchor=CENTER)
        
    def Busc(self):

        val=list(self.txtID.get())
        print(val)

        if val[0] == "f":
            self.f="factura"+self.So
            
            v=self.txtID.get()
            self.vf=v.split("-")
            print(self.vf)

            if self.txtID.get() == "f":
                
                self.datos(self.f)
                
            else:
                try:
                    print(self.f)
                    Fa = self.Seller.buscar(self.vf[1],self.f,1);

                    self.grid.heading("#0", text="# Factura", anchor=CENTER)
                    self.grid.heading("col1", text="ID ", anchor=CENTER)
                    self.grid.heading("col2", text="Nombre", anchor=CENTER)
                    self.grid.heading("col3", text="Fecha ", anchor=CENTER)
                    self.grid.heading("col4", text="Valor / Descripcion", anchor=CENTER)
                    

                    self.grid.insert("",END, text= str(Fa[0]), values=(str(Fa[1]),str(Fa[2]),str(Fa[3]),str(Fa[4])))
                    self.grid.insert("",END, text= str(""), values=(str(""),str(""),str(""),Fa[5]))
                    print("6")
                except:
                    self.lbl4.config(text="ID inexistente.")
                    self.datos(self.f)
        else:
            
            if self.txtID.get() == "0":
                self.datos(self.So)
            else:
                try:
                    datos = self.Seller.STab(self.txtID.get());
                    self.grid.heading("col2", text="Fecha", anchor=CENTER)
                    for row in datos:
                       self.grid.insert("",END, text= row[0], values=(row[1],row[2],row[3],row[4]))
                    
                except:
                    self.lbl4.config(text="ID inexistente.")
                    self.datos(self.So)

    def impri(self,v1,v2,v3,n,i,Nu,d):
        
        f= str(self.So+ " - "+ str(Nu))
        da=self.Seller.dateNow()
        pdf = FPDF(orientation= 'P', unit= 'mm', format= 'A4')
        pdf.add_page()
        pdf.add_font('Popp', '', 'Poppins-Regular.ttf', uni=True)
        pdf.image('F.png', x = 10, y = 10, w = 190, h = 280)
        pdf.set_font('Popp', '', 15)
        f1= str(self.So+ str(Nu))
        if len(f) > 8:
            pdf.text(x=160, y=40, txt=f)
        elif len(f) > 12:
            pdf.text(x=150, y=40, txt=f)
        else:
            pdf.text(x=165, y=40, txt=f)
            
        pdf.text(x=68, y= 82, txt=n)
        pdf.text(x=164, y= 125, txt=v1)
        pdf.text(x=40, y= 125, txt=i)
        pdf.text(x=97, y= 125, txt=n)
        pdf.text(x=164, y= 141, txt=v2)
        pdf.text(x=164, y= 157, txt=v3)
        pdf.text(x=40, y= 157, txt=i)
        pdf.text(x=97, y= 157, txt=n)
        pdf.text(x=164, y= 230, txt=v3)
        pdf.text(x=12, y= 62, txt=da)
        
        pdf.text(x=22, y= 242, txt="Descripcíon:")
        pdf.text(x=25, y= 250, txt=d)

        print(self.So)
        self.Seller.insfa(i,n,da,v3,d,self.So)
        
        t="./f/{}-{}.pdf".format(f1,i)
        pdf.output(t)


    def Val(self):
        
        vAc=self.Seller.buscar(self.txtID.get(),self.So,2)
        nV = self.txtValue.get()
        print(vAc)
        nR=str(float(vAc[3]) + float(nV))
        desc = self.txtDes.get()

        self.grid.insert("",END, text= str(vAc[0]), values=(str(vAc[1]),str(vAc[2]),str(vAc[3]),str(vAc[4])))
        self.grid.insert("",END, text= str(""), values=(str(""),str(""),str(nV),desc))
        self.grid.insert("",END, text= str(vAc[0]), values=(str(vAc[1]),str(vAc[2]),str(nR)))
      
        self.Seller.modifica(vAc[1],str(nR),self.So)
        self.Seller.insTab(vAc[1],str(nR),desc)
        
        try:
            N=self.Seller.maxI(self.So)
            if N == NONE:
                v = 0
            else:
                a=list(N)
                print(a)
                v=int(a[0])+1
            
            self.impri(str(vAc[3]),str(nV),str(nR),str(vAc[2]),str(vAc[1]),str(v),desc)
        
            
        except:
            self.impri(str(vAc[3]),str(nV),str(nR),str(vAc[2]),str(vAc[1]),str(1),desc)
            
        
        self.lbl4.config(text="Valor actualizado.")
        #self.impri(str(vAc[3]),str(nV),str(nR),str(vAc[2]),str(vAc[1]),)

        self.cBox()

    def bSa(self):
        self.clGrip()
        self.So = "sa"
        self.btnSa.configure(bg="#2F3E45",fg="white")
        self.btnSb.configure(bg="#20292E",fg="white")
        self.datos(self.So)
        self.bha(1)

    def bSb(self):
        self.clGrip()
        self.So = "sb"
        self.btnSb.configure(bg="#2F3E45",fg="white")
        self.btnSa.configure(bg="#20292E",fg="white")
        self.datos(self.So)
        self.bha(1)

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
        self.gripb()
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        if self.cont ==1: #Add
            try:

                self.Seller.inserta(self.txtID.get(),self.txtName.get(),self.txtValue.get(),self.So,self.txtDes.get())
                self.Seller.newTable(self.txtID.get(),self.txtValue.get(),self.txtDes.get())
                self.lbl4.config(text="")
                self.cBox()
                self.datos(self.So)
                
            except:
                self.lbl4.config(text="Valores invalidos.")

        elif self.cont ==2: #Delet
            try:
                print("1")
                self.Seller.elimina(self.txtID.get(),self.So)
                print("1")
                self.lbl4.config(text="")
                self.cBox()
                self.datos(self.So)

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
        self.btnAdd.place(x=0,y=140,width=110, height=30 )        
        self.btnDelet=Button(frame1,text="Eliminar", command=self.bDelet, bg="#20292E", fg="white",relief=FLAT)
        self.btnDelet.place(x=0,y=210,width=110, height=30)        
        self.btnShow=Button(frame1,text="Explorar", command=self.bShow, bg="#20292E", fg="white",relief=FLAT)
        self.btnShow.place(x=0,y=280,width=110, height=30)
        self.btnChan=Button(frame1,text="Modificar", command=self.bChan, bg="#20292E", fg="white",relief=FLAT)
        self.btnChan.place(x=0,y=350,width=110, height=30)    

        self.btnSa=Button(frame1,text="Sa", command=self.bSa, bg="#20292E", fg="white",relief=FLAT)
        self.btnSa.place(x=0,y=650,width=110, height=30)  
        self.btnSb=Button(frame1,text="Sb", command=self.bSb, bg="#20292E", fg="white",relief=FLAT)
        self.btnSb.place(x=0,y=680,width=110, height=30)  


        frame2 = Frame(self,bg="#2F3E45" )
        frame2.place(x=100,y=0,width=1200, height=720)                        
        lbl1 = Label(frame2,text="ID: ",bg="#2F3E45",fg="white")        
        lbl1.place(x=30,y=5+100)        
        self.txtID=Entry(frame2)
        self.txtID.place(x=30,y=25+100,width=160, height=20)                
        lbl2 = Label(frame2,text="Nombre: ",bg="#2F3E45",fg="white")

        lbl2.place(x=30,y=55+110)        
        self.txtName=Entry(frame2)
        self.txtName.place(x=30,y=75+110,width=160, height=20)        
        lbl3 = Label(frame2,text="Valor: ",bg="#2F3E45",fg="white")
        lbl3.place(x=30,y=105+120)        
    
        self.lbl4 = Label(frame2,text="",bg="#2F3E45",fg="white",font=( NORMAL, 11))
 
        self.lbl4.place(x=35,y=500)        

        self.txtValue=Entry(frame2)
        self.txtValue.place(x=30,y=125+120,width=160, height=20)        
          
        self.btnGuardar =  Button(frame2,text="Guardar", command=self.bSave, bg="#05867B", fg="white",relief=FLAT)
        self.btnGuardar.place(x=70,y=160+200,width=60, height=30)        
       
        lbl5 = Label(frame2,text="Descripción: ",bg="#2F3E45",fg="white")
        lbl5.place(x=120,y=670)        
        self.txtDes=Entry(frame2)
        self.txtDes.place(x=207,y=670,width=780, height=20)   


        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4"))        
        self.grid.column("#0",width=20)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=100, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=100, anchor=CENTER)

        self.grid.heading("#0", text="#", anchor=CENTER)
        self.grid.heading("col1", text="ID", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Valor", anchor=CENTER)
        self.grid.heading("col4", text="Descripcíon", anchor=CENTER)

        self.grid.place(x=310,y=0,width=970, height=650)
        
        
        
        
        
        