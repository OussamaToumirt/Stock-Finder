import tkinter as tk
from tkinter import ttk
from tkinter import *
from selenium import webdriver
import time
import requests
import random
from tkinter import messagebox
import os.path



root = tk.Tk()
root.title("Stock Finder")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("1000x600")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)

style = ttk.Style(root)
widgets_frame = ttk.Frame(root, padding=(40,0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)
# Import the tcl file
root.tk.call("source", "proxttk.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk")

d = tk.IntVar(value=2)
# Label
text1 = ttk.Label(widgets_frame, text="Stock Finder",font="gotham 40  bold",foreground="#333333")
text1.grid(row=0, column=0, pady=50, columnspan=2)






d = tk.IntVar(value=2)


# Entry
box = ttk.Entry(widgets_frame)
box.insert(0, "")
box.grid(row=2, column=0, padx=250, pady=0, sticky="ew")


#get image
def stockfinder():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')


    the_url = box.get()
    print("This Tools Developed By : Oussama Toumirt @Oussama.toumirt")
    url = 'https://getpaidstock.com/token.php?url='+str(the_url)
    driver = 'chromedriver.exe'
    browser = webdriver.Chrome(driver, options=options)
    browser.get(url)



    dester = browser.find_element_by_xpath('/html/body/center/a[1]')
    link = dester.get_attribute('href')
    print("Searching..")
    browser.get(link)

    time.sleep(3)
    download = browser.find_element_by_xpath('/html/body/div[3]/header/a[2]/img')
    src = download.get_attribute('src')
    print("Downloading...")


    n = random.randint(0,1000)


    directory = './images/'
    filename = str(n)+"_stockfinder.jpg"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)

    file = open(file_path, "wb")
    file.write(requests.get(src).content)
    file.close()

    print("Done")
    messagebox.showinfo("Success", "".join("Done, Please don't forget follow me @oussama.toumirt"))

    browser.quit()

















# Label
text1 = ttk.Label(root, text=" Enter URL ",foreground="#333333")
text1.grid(row=0, column=0, pady=155, columnspan=2)





accentbutton = ttk.Button(widgets_frame, text="Download", style="AccentButton", command=stockfinder)
accentbutton.grid(row=10, column=0, padx=300, pady=30, sticky="nsew")
root.mainloop()