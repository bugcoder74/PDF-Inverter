import tkinter as tk
from tkinter.ttk import Progressbar

from tkinter import PhotoImage, filedialog, messagebox
import converter
import time
import threading

input_file = None
output_file = None

inready = False
outready = False



#def f():
#    print("before sleep")
#    time.sleep(3)
#    print("after sleep")

##def startConversion():
##    global input_file
##    global output_file
##    global progress
##    converter.main(input_file,output_file)
##    print("converter called")
##    tk.messagebox.showinfo("Success","Inversion Successfull")
##    progress.stop()
    
def startConversion():
    global input_file
    global output_file
    global progress
    global root
    global progressLabel

    if (inready and outready):
        startButton['state'] = tk.DISABLED
        progress.grid(row=1,column=0,sticky="ew",padx=120)
        progress.start(10)
        progressLabel['text'] = "Processing.. Please Wait"
        root.update_idletasks()
        progressLabel.grid(row=0,column=0,pady=2)
        converter.invertPagePdf(input_file)
        converter.generateInvertedPDF(output_file)
        tk.messagebox.showinfo("Success","Inversion Successfull")
        progress.stop()
        progressLabel['text'] = "Successfully Inverted.."
        root.update_idletasks()
    else:
        tk.messagebox.showerror("Error!","Please select source and output pdf files")

def inputButton():
    global input_file
    global inready
    global inputButton
    file = tk.filedialog.askopenfile()
    print(file.name)
    input_file = file.name
    inready = True
    inputButton['text']="Select Source File - Selected"
    root.update_idletasks()
    
    

def outputButton():
    global output_file
    global outready
    global outputButton
    file = tk.filedialog.asksaveasfile(title="Create Output File",filetypes = (("PDF Files","*.pdf"),("all files","*.*")))
    print(file.name)
    output_file = file.name
    outready = True
    outputButton['text'] = "Create Output File - Selected"

def startButton():
    global progress
    global startButton

    #startButton['state'] = tk.DISABLED
    #progress.grid(row=0,column=0,sticky="ew",padx=120)
    #progress.start(10)
    #time.sleep(5)
    #progress.stop()
    p = threading.Thread(target=startConversion)
    p.start()
    #p.join()
    #print("Gone out")

def resetButton():
    global startButton
    global input_file
    global output_file
    global inready
    global outready
    global progress
    global progressLabel
    global inputButton
    global outputButton
    
    print("Reset Button Pressed")
    
    startButton['state'] = "normal"
    progress.stop()
    progress.grid_forget()
    progressLabel.grid_forget()

    input_file = None
    output_file = None
    inready = False
    outready = False

    inputButton['text'] = "Select Source File"
    outputButton['text'] = "Create Output File"
    

root = tk.Tk()

root.title("HDR PDF Inverter")

screen_width = int(root.winfo_screenwidth()/2)
screen_height = int(root.winfo_screenheight()/1.5)

root.geometry(str(screen_width)+"x"+str(screen_height))
root.resizable(False,False)

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

rootFrame = tk.Frame(root,bg="grey")
rootFrame.grid(row=0,column=0,sticky="nsew")
rootFrame.grid_propagate(False)

rootFrame.grid_columnconfigure(0,weight=1)
rootFrame.grid_rowconfigure(0,weight=2)
rootFrame.grid_rowconfigure(1,weight=1)
rootFrame.grid_rowconfigure(2,weight=1)
rootFrame.grid_rowconfigure(3,weight=1)
rootFrame.grid_rowconfigure(4,weight=1)

iconFrame = tk.Frame(rootFrame)
inputFrame = tk.Frame(rootFrame)
outputFrame = tk.Frame(rootFrame)
progressFrame = tk.Frame(rootFrame)
startFrame = tk.Frame(rootFrame)


iconFrame.grid(row=0,column=0,sticky="nsew")
inputFrame.grid(row=1,column=0,sticky="nsew")
outputFrame.grid(row=2,column=0,sticky="nsew")
progressFrame.grid(row=3,column=0,sticky="nsew")
startFrame.grid(row=4,column=0,sticky="nsew")


iconFrame.grid_propagate(False)
inputFrame.grid_propagate(False)
outputFrame.grid_propagate(False)
progressFrame.grid_propagate(False)
startFrame.grid_propagate(False)

iconFrame.grid_rowconfigure(0,weight=1)
iconFrame.grid_columnconfigure(0,weight=3)
iconFrame.grid_columnconfigure(1,weight=3)

inputFrame.grid_rowconfigure(0,weight=1)
inputFrame.grid_columnconfigure(0,weight=1)

outputFrame.grid_rowconfigure(0,weight=1)
outputFrame.grid_columnconfigure(0,weight=1)

progressFrame.grid_rowconfigure(0,weight=1)
progressFrame.grid_rowconfigure(1,weight=1)
progressFrame.grid_columnconfigure(0,weight=1)
progressFrame.grid_propagate(False)

startFrame.grid_rowconfigure(0,weight=1)
startFrame.grid_columnconfigure(0,weight=1)
startFrame.grid_rowconfigure(1,weight=1)

photoIcon = tk.PhotoImage(file="icon1.png")
photoLabel = tk.Label(iconFrame,image=photoIcon,anchor="e")
photoLabel.grid(row=0,column=0,sticky="nsew")
textLabel = tk.Label(iconFrame, text="HDR Pdf - Inverter",font=("",32),anchor="w")
textLabel.grid(row=0,column=1,sticky="nsew",padx=10)


inputLabel = tk.LabelFrame(inputFrame,text="Select the PDF to be Inverted")
inputLabel.grid(row=0,column=0,sticky="nsew",padx=100)
inputLabel.grid_columnconfigure(0,weight=1)
inputLabel.grid_rowconfigure(0,weight=1)

outputLabel = tk.LabelFrame(outputFrame,text="Create File Name for Inverted PDF")
outputLabel.grid(row=0,column=0,sticky="nsew",padx=100)
outputLabel.grid_columnconfigure(0,weight=1)
outputLabel.grid_rowconfigure(0,weight=1)

startButton = tk.Button(startFrame,text="Start Inversion",font=("",16),command=startButton,relief='ridge',border=2)
startButton.grid(row=0,column=0,pady = 1)

progress = tk.ttk.Progressbar(progressFrame, orient=tk.HORIZONTAL, mode="indeterminate", length=100)
#progress.grid(row=0,column=0,sticky="ew",padx=120)
#progress.start(20)

progressLabel = tk.Label(progressFrame, text = "Processing.. PLease Wait", font=("",12))

inputButton = tk.Button(inputLabel,text="Select Source File",relief="flat",command=inputButton)
inputButton.grid(row=0,column=0)

outputButton = tk.Button(outputLabel,text="Create Output File",relief="flat",command=outputButton)
outputButton.grid(row=0,column=0)

resetButton = tk.Button(startFrame,text="Reset",font=("",16),command=resetButton,relief='ridge',border=2)
resetButton.grid(row=1,column=0,pady=(1,10))







root.mainloop()
