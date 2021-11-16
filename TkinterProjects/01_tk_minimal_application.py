#!/usr/bin/env python3

import tkinter as tk
import tkinter.font

class Application(tk.Frame):
    """ ===================================================="""
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        #self.geometry("600x550+300+300")
        
        helv36 = tkinter.font.Font(family="Helvetica", size=36, weight="bold")
        self.createWidgets()

    def createWidgets(self):
        
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

app = Application()
app.master.geometry("600x550+300+300")
app.master.title("Aplicatie Simpla")
app.mainloop()
