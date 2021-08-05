
from tkinter import *
from ventana import *


def main():
    root = Tk()
    root.wm_title("Caja")
   # Wwin=root.winfo_screenwidth()
    #Hwin=root.winfo_screenheight()
    app = Ventana(root) 
    app.mainloop()



if __name__ == "__main__":
    main()