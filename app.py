#immediately starts up welcome page
from welcome import *
from tkinter import ttk
from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import messagebox
from time import sleep
from google_images_download import google_images_download
import os
import winshell
from random import randint
import requests, json, time
from urllib.request import urlopen

#LOADING ANIMATION
def loggedin():
    sleep(2)
    wnd_.destroy()

wnd_ = tk.ThemedTk()
wnd_.get_themes()
wnd_.set_theme('equilux')
wnd_.title("Logging in....")
wnd_.geometry("130x70+550+325")
wnd_.iconbitmap('form.ico')
wnd_.config(bg="black")
wnd_.minsize(width = 130, height = 70)
wnd_.maxsize(width = 130, height = 70)
wnd_.overrideredirect(1)

Label(text=" ", bg="black").pack()
message = ttk.Label(wnd_, text="  Logging In..", width=120, font=("Helvetica, 15"),foreground="white", background="black")
message.pack()
Label(text=" ", bg="black").pack()

wnd_.after(200, loggedin)
wnd_.mainloop()


def appPage():

    status = False

    try:
        if urlopen("https://www.google.com/"):
            status = True
    except:
        pass

    if status == True:

        #HOME PAGE
        wnd = tk.ThemedTk()
        wnd.get_themes()
        wnd.set_theme('equilux')
        wnd.title("TravelSorter")
        wnd.geometry("600x450+340+130")
        wnd.iconbitmap('form.ico')
        wnd.config(bg="black")
        wnd.minsize(width = 600, height = 450)
        wnd.maxsize(width = 600, height = 450)


        def return_to_home():
            if messagebox.askyesno("Confirmation","Are you sure you want to log out?") == True: 
                wnd.destroy()
                welcome_page()
            else:
                pass

        def exiting():
            if messagebox.askyesno("Confirmation","Are you sure you want to exit?") == True: 
                wnd.destroy()

                wnd__ = tk.ThemedTk()
                wnd__.get_themes()
                wnd__.set_theme('equilux')
                wnd__.title("Exiting....")
                wnd__.geometry("130x70+550+325")
                wnd__.iconbitmap('form.ico')
                wnd__.config(bg="black")
                wnd__.minsize(width = 130, height = 70)
                wnd__.maxsize(width = 130, height = 70)
                wnd__.overrideredirect(1)

                Label(text=" ", bg="black").pack()
                message = ttk.Label(wnd__, text="    Exiting....", width=120, font=("Helvetica, 15"),foreground="white", background="black")
                message.pack()
                Label(text=" ", bg="black").pack()

                def destroy():
                    wnd__.destroy()
                    
                wnd__.after(1000, destroy)
                wnd__.mainloop()
                print("Thank You!")

            else:
                pass
        
        home = PhotoImage(file="form.png")
        home_button = ttk.Button(wnd, width='6', command=return_to_home)
        home_button.config(image=home)
        home_button.grid(row=0, column=0)

        home_label = ttk.Label(wnd,relief=RIDGE, text="             TravelSorter                ", font=("Helvetica, 28"),foreground="white", background="black")
        home_label.grid(row=0, column=1)

        exit_ = PhotoImage(file="exit.png")
        exit_button = ttk.Button(wnd, width='6', command=exiting)
        exit_button.config(image=exit_)
        exit_button.grid(row=0, column=2)

        Label(wnd, text=" ", bg="black").grid(row=1,column=0)
        Label(wnd, text=" ", bg="black").grid(row=1,column=1)
        Label(wnd, text=" ", bg="black").grid(row=1,column=2)

        Label(wnd, text=" ", bg="black").grid(row=2,column=0)

        defaultpic = PhotoImage(file="defaultlocation.png")
        piclabel = Label(wnd, image=defaultpic)
        piclabel.config(image=defaultpic)
        piclabel.grid(row=2, column=1)

        Label(wnd, text=" ", bg="black").grid(row=2,column=2)
        Label(wnd, text=" ", bg="black").grid(row=3,column=0)
        Label(wnd, text=" ", bg="black").grid(row=3,column=1)
        Label(wnd, text=" ", bg="black").grid(row=3,column=2)
        Label(wnd, text=" ", bg="black").grid(row=4,column=0)

        message = ttk.Label(wnd, text="    LOCATION     ", font=("Helvetica, 15"),foreground="white", background="black")
        message.grid(row=4, column=1)

        Label(wnd, text=" ", bg="black").grid(row=4,column=2)
        Label(wnd, text=" ", bg="black").grid(row=5,column=0)

        location_entry = ttk.Entry(width=30, text=("Helvetica, 15"),foreground="white")
        location_entry.grid(row=5,column=1)
        location_entry.insert(0,"Delhi")
        Label(wnd, text=" ", bg="black").grid(row=5,column=2)

        Label(wnd, text=" ", bg="black").grid(row=6,column=0)
        Label(wnd, text=" ", bg="black").grid(row=6,column=1)
        Label(wnd, text=" ", bg="black").grid(row=6,column=2)

        def submittion():
            global location
           
            location = location_entry.get()

            if len(location) == 0:
                messagebox.showinfo("Entry Error!","Please Enter A Valid Location!")
            else:
                user_proof = username_get()

                response = google_images_download.googleimagesdownload()

                arguments = {"keywords":location+" beautiful city images","limit":5,"print_urls":False,"silent_mode":True,"format":"png","no_directory":True,"output_directory":"C:/Users/aayus/Desktop/PROJECTS/LOGIN","save_source":"paths","exact_size":"320,160"} 
                paths = response.download(arguments)
                
                with open("paths.txt","r") as f:
                    splits = f.read()
                    content = splits.split("//")
                    loc1 = content[1]
                    loc2 = content[3]
                    loc3 = content[5]
                    loc4 = content[7]
                    loc5 = content[9]

                    req = loc1.split("\t")
                    req2 = loc2.split("\t")
                    req3 = loc3.split("\t")
                    req4 = loc4.split("\t")
                    req5 = loc5.split("\t")

                    
                    filepath1 = req[0]
                    filepath2 = req2[0]
                    filepath3 = req3[0]
                    filepath4 = req4[0]
                    filepath5 = req5[0]
               
                    f.close()

                filepaths = [filepath1,filepath2,filepath3,filepath4,filepath5]

                val = randint(0,4)

                display = filepaths[val]
                
                location_pic = PhotoImage(file=display)
                pic_label = Label(wnd, image=location_pic)
                pic_label.config(image=location_pic)
                pic_label.grid(row=2, column=1)

                try:
                    os.remove(filepath1)
                    os.remove(filepath2)
                    os.remove(filepath3)
                    os.remove(filepath4)
                    os.remove(filepath5)

                    os.remove('paths.txt')
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    print("Removed")
                except:
                    print("Files don't exist.")
                    
                wnd.update()
                wnd.mainloop()
            
        Label(wnd, text=" ", bg="black").grid(row=7,column=0)

        submit = ttk.Button(text="SUBMIT", width=30, command=submittion)
        submit.grid(row=7, column=1)

        Label(wnd, text=" ", bg="black").grid(row=7,column=2)

        Label(wnd, text=" ", bg="black").grid(row=8,column=0)
        Label(wnd, text=" ", bg="black").grid(row=8,column=1)
        Label(wnd, text=" ", bg="black").grid(row=8,column=2)
        
        def information():
            
            # enter your api key here 
            api_key = 'AIzaSyC7j4YF2vuCFoLQAX309U-k__8OkMMOAN0'
              
            # url variable store url 
            url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
              
            # get method of requests module 
            # return response object 
            r = requests.get(url + 'query=' + location +"+top+locations+"+
                                    '&key=' + api_key) 
              
            # json method of response object convert 
            #  json format data into python format data 
            x = r.json() 
              
            # now x contains list of nested dictionaries  
            # we know dictionary contain key value pair 
            # store the value of result key in variable y 
            y = x['results']

            filepath = os.path.join('C:/Users/aayus/Desktop/PROJECTS/LOGIN/TopLocationsInforamtion', 'TopLocationsOf'+location+".txt")
            f = open(filepath,"a")

            # keep looping upto lenght of y 
            for i in range(len(y)): 
                  
                # Print value corresponding to the 
                # 'name' key at the ith index of y 
                loc_ = y[i]['name']
                loc = str(loc_)
                rating_ = y[i]['rating']
                rating = str(rating_)
                try:
                    open_or_not = y[i]['opening_hours']['open_now']

                    if open_or_not == 0:
                        open_or_not = "Closed."
                    else:
                        open_or_not = "Open."
                except:
                    open_or_not = "Info not provided"
                try:
                    type_loc = (y[i]['types'][0]).upper()       
                except:
                    type_loc = "Info not provided"

                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                time_ = str(current_time)
                
                f.write("Location: " + loc +"\n")
                f.write("Rating: " + rating +"\n")
                f.write("Open Now?: " + open_or_not +"\n")
                f.write("Timestamp: " + time_ +"\n")
                f.write("Type Of Location: " + type_loc +"\n")
                f.write("\n")

            f.close()

            messagebox.showinfo("Downloaded Completed!","File Containing Requested Information Has Been Downloaded.")

            #os.remove(filepath)
            
        Label(wnd, text=" ", bg="black").grid(row=9,column=0)
        showinfo = ttk.Button(text="TOP LOCATION DETAILS", width=30, command=information)
        showinfo.grid(row=9, column=1)
        Label(wnd, text=" ", bg="black").grid(row=9,column=2)

        def toolbar():

            def checkhistory():
                print("DONE")
                
            menu = Menu(wnd,font=("Helvetica, 12"))
            wnd.config(menu=menu)

            subMenu = Menu(menu, tearoff=0,font=("Helvetica, 8"))
            menu.add_cascade(label="Search History", menu=subMenu)
            subMenu.add_command(label="Check History", command=checkhistory)
            subMenu.add_command(label="Download History", command=checkhistory)
            subMenu.add_separator()
            subMenu.add_command(label="Clear History", command=checkhistory)
        toolbar()
            
        wnd.mainloop()
    else:
        wnd = Tk()
        messagebox.showinfo("Connection Error","Please connect to a Wi-Fi connection.")
        wnd.withdraw()
    
appPage()

