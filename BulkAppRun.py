import tkinter
from tkinter import filedialog, Text
import os
import sys, subprocess

class AppRun():
    """ Main class:
    Run/open list of applications with a click"""

    def __init__(self):
        """initilization of the Bulk run"""
        self.apps = []
        self.loadedListFilename = "saved_list.txt"
        self.Ui_screen()
    
    def addList(self,frame):
        """open the file explorer and adding the app info to the label"""
        print("this is addlist")
        for widget in frame.winfo_children():
            widget.destroy()
        filename = filedialog.askopenfilename(initialdir = '/', title="Select the Item",
                                            filetypes=(("executables","*.deb .exe"),("all files","*.*")))
        self.apps.append(filename)
        print(filename)
        for app in self.apps:
            if app:
                label = tkinter.Label(frame, text=app, bg="green")
                label.pack()
        if self.apps:
            with  open(self.loadedListFilename,"w") as f:
                for x in list(set(self.apps)):
                    print(x)
                    if type(x) is str:
                        f.write(x +',')
    
    def openApps(self):
        """open/excute the list of apps/files"""
        # for app in self.apps:
        #     os.startfile(app)
        print(sys.platform)
        platfom_ = sys.platform
        if platfom_ == "linux":
            for app in self.apps:
                subprocess.call(["xdg-open",app])
        elif platfom_ == "darwin":
            for app in self.apps:
                subprocess.call(["open", app])
        else:
            for app in self.apps:
                os.startfile(app)


    def Ui_screen(self):
        root = tkinter.Tk()
        root.config(background='blue') 
        canvas = tkinter.Canvas(root, height = 300, width = 300, bg="#14CF11")
        canvas.pack() # adding the canvas
        # adding the frame
        frame = tkinter.Frame(root, bg ="white")
        frame.place(relwidth=0.98, relheight = 0.85,relx =0.01,rely=0.01)
        if os.path.isfile(self.loadedListFilename):
            with open(self.loadedListFilename,'r') as f:
                loadedApps = f.read()
                loadedApps = loadedApps.split(',')
                self.apps = loadedApps
            if loadedApps:
                for app in loadedApps:
                    if app:
                        label = tkinter.Label(frame, text=app, bg="green")
                        label.pack()

        openFile = tkinter.Button(root, text= "Open File",
                                padx=10,pady=2, fg="white",command= lambda :self.addList(frame) ,
                                bg= "#14CF11")
        openFile.pack()
        runApps = tkinter.Button(root, text="LET'S START",
                                padx=10, pady=2, fg="Red", command= self.openApps,
                                bg="#14CF11") 
        runApps.pack()


        root.mainloop()




if __name__=="__main__":
    AppRun()