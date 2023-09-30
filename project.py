from tkinter import *
from plyer import notification
from tkinter import messagebox
import time
# from gtts import gTTS
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.ttk import Progressbar
# import os,sys


def goto_signup_clicked(destroy_this_window): #toggle from login to signup
    destroy_this_window.destroy()
    sign=Tk()
    sign.title("SignUp")
    sign.geometry("500x300") #300x200
    sign.config(background = "black", pady=10)
    
    global clock
    clock=Label(sign, font=("times", 14), bg= "black",fg="white")
    clock.place(x = 350, y = 5)
     
    lbs = Label(sign, text = "SignUp", bg = "black", fg="white", font=20)
    lbs.place(x=210, y=5)

    lb2_s = Label(sign, text = "Username  ", bg="black", fg="white")
    lb2_s2 = Entry(sign)
    lb2_s.place(x=110, y=40)
    lb2_s2.place(x=210, y=40)


    lb2_ps = Label(sign, text = "Password  ", bg="black", fg="white")
    lb2_ps2 = Entry(sign,show="*")
    lb2_ps.place(x=110, y=80)
    lb2_ps2.place(x=210,y=80)
   
    def reg():                      # register function to register new user
        username = lb2_s2.get()
        pas = lb2_ps2.get()
        file =  open("username.txt","a")
        file1= open("password.txt","a")
        score_file= open("score.txt","a")
        fiIn = open('username.txt').readlines()
        fiIn1 = open('password.txt').readlines()
        score_f=open("score.txt").readlines()
        if username=="" or pas=="":
            messagebox.showerror("Error", "Fields are mandatory")
        elif (username+"\n") in fiIn:
            print("Exists")
            messagebox.showerror("Error", "User already exists")
        else:
            print("not Exists")
            if len(pas)>9:
                messagebox.showerror("Error","you can set short password")
                lb2_ps2.delete(0,END)
            else:    
                file.write(username+"\n")
                file1.write(pas+"\n")
                score_file.write("0\n")
                lb2_ps2.delete(0,END)
                lb2_s2.delete(0,END)
                messagebox.showinfo("Congratulations", "Registered successfully")
            file.close()
            file1.close()
                
    bts = Button(sign, text="Register", command=reg)
    bts.place(x=210, y=120)
    bts3 = Button(sign, text="Go to Signin", command=lambda:createframelogin("Login",sign))
    bts3.place(x=290, y=120)
    dis.place(x=100, y=150)

def dis():                      # login to authenticate user
    user = lb2_u2.get()
    pas = lb2_p2.get()
    filo1 = open('username.txt').readlines()
    filo2 = open('password.txt').readlines()
    if user=="" or pas=="":
        messagebox.showerror("Error", "Enter credentials")
       
    flag=0
    for i in range(0,len(filo1)):
        if((user+"\n")==filo1[i]):
            if ((pas+"\n") ==filo2[i]):
                messagebox.showinfo("Congratulations", "Login successful")
                flag=1
                window.destroy()
                b()
                break
            else:
                messagebox.showerror("Error", "Login unsuccessfull!!\nIncorrect password\nplease try again")
                break
    if(flag!=1):
        messagebox.showerror("Error", "Login unsuccessful!!!Try again")
    lb2_u2.delete(0,END)
    lb2_p2.delete(0,END)


def createframelogin(s,destroy_this_window):    # basic frame creation
    destroy_this_window.destroy()
    global window
    window=Tk()
    window.title(s)
    window.geometry("500x300")   #300x200
    window.config(background = "black", pady=10)
    
    global clock
    clock=Label(window, font=("times", 14), bg= "black",fg="white")
    clock.place(x = 350, y = 5)

    # tick()
    #tt1=Thread(target=ticksmall)
    #tt1.start()
    file =  open("username.txt","a")
    file1= open("password.txt","a")
    global lb2_u
    global lb2_u2
    lb1 = Label(window, text = "Login Form", bg = "black", fg="white", font=20)
    lb1.place(x=210, y=5)

    lb2_u = Label(window, text = "Username  ", bg="black", fg="white")
    lb2_u2 = Entry(window)
    global lb2_p
    global lb2_p2

    lb2_u.place(x=110, y=40)
    lb2_u2.place(x=210, y=40)


    lb2_p = Label(window, text = "Password  ", bg="black", fg="white")
    lb2_p2 = Entry(window,show="*") 
    
    
    lb2_p.place(x=110, y=80)
    lb2_p2.place(x=210,y=80)
    bt = Button(window, text="Login")                         ## bt=login log
    bt.place(x=210, y=120)                                    ## bt2 =head to signup
    bt.config(command=dis)
    bt2 = Button(window, text="SignUp",command = lambda:goto_signup_clicked(window))
    bt2.place(x=270, y=120)
    return window
    
class noneclass:        # an empty class just to wrap the main application in function
    def destroy(self):
        pass
    pass

def b():
    global k
    k=Tk()
    k.title('Notifier')
    k.geometry("500x300")
    img = Image.open("notify-label.png")
    tkimage = ImageTk.PhotoImage(img)
    img_label = Label(k, image=tkimage).grid()


    t_label = Label(k, text="Task name",font=("poppins", 10))
    t_label.place(x=12, y=70)


    global title 
    title =  Entry(k, width="25",font=("poppins", 13))
    title.place(x=123, y=70)

 
    m_label = Label(k, text="Display Message", font=("poppins", 10))
    m_label.place(x=12, y=120)


    global msg
    msg = Entry(k, width="40", font=("poppins", 13))
    msg.place(x=123,height=30, y=120)


    time_label = Label(k, text="Set Time", font=("poppins", 10))
    time_label.place(x=12, y=175)


    global time1
    time1 = Entry(k, width="5", font=("poppins", 13))
    time1.place(x=123, y=175)


    global time_min_label
    time_min_label = Label(k, text="min", font=("poppins", 10))
    time_min_label.place(x=175, y=180)


    but = Button(k, text="Task Remider", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                 relief="raised",
                 command=get_details)
    but.place(x=170, y=230)

    k.resizable(0,0)
    k.mainloop()



def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
   

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("Timer set", "set Reminder ?")
        k.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Task-Reminder",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

a=noneclass()
login_window=createframelogin("Login",a)
login_window.mainloop()
