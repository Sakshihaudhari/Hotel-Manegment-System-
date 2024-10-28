from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   
from tkinter import messagebox
import webbrowser



def main():
    win=Tk()
    app=loginwindow(win)
    win.mainloop()


class loginwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\HOTEL RESERVATION\images\page2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=170,width=340,height=450)

        img1=Image.open(r"C:\HOTEL RESERVATION\images\contact icon.png")
        img1=img1.resize((80,80),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=170,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #===============label==================
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #================login button=================
        loginbutton=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbutton.place(x=110,y=300,width=100,height=30)
        
      



 ######################### user password ############################
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("erro","all field required")
        elif self.txtuser.get()=="renuka" and self.txtpass.get()=="renu1234":
            messagebox.showinfo("Success","Welcome to hotel crown")
       
            if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                webbrowser.open_new_tab(r"C:\HOTEL REVERVATION\hotel.py")
                if __name__ == "__main__":
                    main()
            
