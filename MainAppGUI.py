# Use Tkinter for python 2, tkinter for python 3
import Tkinter

class MainApplication(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)

        button = Tkinter.Button(self, text=u"Search", command=self.OnButtonClick())
        button.grid(column=1,row=0)

        label = Tkinter.Label(self, anchor="w", fg="black", bg="grey")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
        print "You Clicked the button!"

    def OnPressEnter(self, event):
        print "You press enter!"
        

if __name__ == "__main__":
    app = MainApplication(None)
    app.title('Soccer Scores')
    app.mainloop()
'''class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # <create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
'''
