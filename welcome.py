from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import sqlite3

def registration_page():

    wnd = tk.ThemedTk()
    wnd.get_themes()
    wnd.set_theme('equilux')
    wnd.geometry('300x500+400+100')
    wnd.title("Registration Form")
    wnd.configure(bg="black")
    wnd.iconbitmap('form.ico')
    wnd.minsize(width = 300, height = 500)
    wnd.maxsize(width = 300, height = 500)

    welcome_text = ttk.Label(text="Registration Form", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    welcome_text.config(anchor=CENTER)
    welcome_text.pack(padx=10, pady=10)

    main_frame = Frame(width=300, height=380)
    main_frame.config(background="black")

    username_label = ttk.Label(text="USERNAME", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    username_label.config(anchor=CENTER)
    username_label.pack(pady=10)

    username_entry = ttk.Entry(width=30)
    username_entry.pack()
    username_entry.insert(0,"a#b123")

    Label(text=" ", bg="black").pack()

    email_label = ttk.Label(text="EMAIL", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    email_label.config(anchor=CENTER)
    email_label.pack(pady=10)

    email_entry = ttk.Entry(width=30)
    email_entry.pack()
    email_entry.insert(0,"abc@randomemail.com")

    Label(text=" ", bg="black").pack()
    password_label = ttk.Label(text="PASSWORD", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    password_label.config(anchor=CENTER)
    password_label.pack(pady=10)

    password_entry = ttk.Entry(width=30, show="*")
    password_entry.pack()
    password_entry.insert(0,"password")

    Label(text=" ", bg="black").pack()

    confirm_pass_label = ttk.Label(text="CONFIRM PASSWORD", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    confirm_pass_label.config(anchor=CENTER)
    confirm_pass_label.pack(pady=10)

    confirm_pass_entry = ttk.Entry(width=30, show="*")
    confirm_pass_entry.pack()
    confirm_pass_entry.insert(0,"password")

    Label(text=" ", bg="black").pack()

    def passf():
        #global username, email, password
        
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_pass = confirm_pass_entry.get()

        checks_passed = True

        #Email Authentication
        if ("@" not in email) or (".com" not in email):
            messagebox.showinfo("Invalid Input","Enter Valid Info")
            checks_passed = False
            wnd.destroy()
            registration_page()

        if confirm_pass != password:
            messagebox.showinfo("Registration Error","Entered Passwords do not match. Please try again.")
            checks_passed = False
            wnd.destroy()
            registration_page()

        conn = sqlite3.connect('users.db')
        cursor = conn.execute('SELECT * from USERINFO')
        for row in cursor:
            if row[1] == email:
                messagebox.showinfo("Already Exists","The Entered Email Already Has An Exisitng Account")
                conn.close()
                wnd.destroy()
                registration_page()
            if row[0] == username:
                messagebox.showinfo("Already Exists","The Entered Username Has Already Been Taken")
                conn.close()
                wnd.destroy()
                registration_page()
        conn.close()
                
        #table name= USERINFO
        #COLUMNS: USERNAME, EMAIL, PASSWORD
        if checks_passed == True:
            conn = sqlite3.connect('users.db')
            conn.execute('INSERT INTO USERINFO(USERNAME, EMAIL, PASSWORD)VALUES(?,?,?)',(username, email, password))
            conn.commit()
            conn.close()
            
            wnd.destroy()
        
    submit_button = ttk.Button(text="SUBMIT", width=30, command=passf)
    submit_button.pack()

    Label(text=" ", bg="black").pack()

    def back_home():
        wnd.destroy()
        welcome_page()

    home_button = ttk.Button(text="HOME", width=30, command=back_home)
    home_button.pack()
    
    main_frame.pack()
    wnd.mainloop()

users = {}

conn = sqlite3.connect('users.db')
cursor = conn.execute('SELECT * from USERINFO')
for row in cursor:
    users[row[1]] = row[2]
    print("Username of " + row[1] + ": " + row[0])
conn.close()

print(users)

def login_page():

    wnd = tk.ThemedTk()
    wnd.get_themes()
    wnd.set_theme('equilux')
    wnd.geometry('300x300+400+200')
    wnd.title("Login")
    wnd.configure(bg="black")
    wnd.iconbitmap('form.ico')
    wnd.minsize(width = 300, height = 375)
    wnd.maxsize(width = 300, height = 375)

    welcome_text = ttk.Label(text="Login", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    welcome_text.config(anchor=CENTER)
    welcome_text.pack(padx=10, pady=10)

    main_frame = Frame(width=300, height=380)
    main_frame.config(background="black")

    email_label = ttk.Label(text="EMAIL", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    email_label.config(anchor=CENTER)
    email_label.pack(pady=10)

    email_entry = ttk.Entry(width=30)
    email_entry.pack()
    email_entry.insert(0,"abc@randomemail.com")

    Label(text=" ", bg="black").pack()

    password_label = ttk.Label(text="PASSWORD", font=("Helvetica, 15"),foreground="white", background="black",width=300)
    password_label.config(anchor=CENTER)
    password_label.pack(pady=10)

    password_entry = ttk.Entry(width=30, show="*")
    password_entry.pack()
    password_entry.insert(0,"password")

    Label(text=" ", bg="black").pack()

    def login():
        global email
        
        email = email_entry.get()
        password = password_entry.get()

        if email not in users.keys():
            messagebox.showinfo("LogIn Error","Entered email is incorrect.")
            wnd.destroy()
            login_page()
        if password == users[email]:
            print("Logged In")
            wnd.destroy()
        else:
            messagebox.showinfo("LogIn Error","Entered email or password is incorrect.")
            wnd.destroy()
            login_page()
           
    submit_button = ttk.Button(text="LOG IN", width=30, command=login)
    submit_button.pack()

    Label(text=" ", bg="black").pack()

    def back_home():
        wnd.destroy()
        welcome_page()
        
    home_button = ttk.Button(text="HOME", width=30, command=back_home)
    home_button.pack()
   
    main_frame.pack()
    wnd.mainloop()

#registration_page()
#login_page()

def welcome_page():
    wnd = tk.ThemedTk()
    wnd.get_themes()
    wnd.set_theme('equilux')
    wnd.geometry('400x300+400+200')
    wnd.title("Welcome")
    wnd.configure(bg="black")
    wnd.iconbitmap('form.ico')
    wnd.minsize(width = 300, height = 375)
    wnd.maxsize(width = 300, height = 375)

    welcome = ttk.Label(text="Welcome to TravelSorter!", font=("Helvetica, 15"),foreground="white", background="black",width=400)
    welcome.config(anchor=CENTER)
    welcome.pack()

    Label(text=" ", bg="black").pack()
    Label(text=" ", bg="black").pack()
    Label(text=" ", bg="black").pack()
    Label(text=" ", bg="black").pack()
    
    exist = ttk.Label(text="Exisiting User?", font=("Helvetica, 15"),foreground="white", background="black",width=400)
    exist.config(anchor=CENTER)
    exist.pack()

    Label(text=" ", bg="black").pack()

    def transfer_to_login():
        wnd.destroy()
        login_page()

    def transfer_to_regis():
        wnd.destroy()
        registration_page()
    
    login_button = ttk.Button(text="LOGIN", width=30, command=transfer_to_login)
    login_button.pack()

    Label(text=" ", bg="black").pack()
    new = ttk.Label(text="New User?", font=("Helvetica, 15"),foreground="white", background="black",width=400)
    new.config(anchor=CENTER)
    new.pack()
    Label(text=" ", bg="black").pack()

    regis_button = ttk.Button(text="REGISTER", width=30, command=transfer_to_regis)
    regis_button.pack()
    wnd.mainloop()

welcome_page()

def username_get():
    return email

"""Code to clear database if required,
conn = sqlite3.connect('users.db')
conn.execute('DELETE FROM USERINFO;')
conn.commit()
print("Successful!")
conn.close()"""



