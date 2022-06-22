from tkinter import *
from gad import *
import drowsydetect   
def main():
    window = Tk()
    window.title("Drowsy Driver Detection ")
    window.geometry('300x200')
    lbl = Label(window, text="Phone Number")
    lbl.grid(column=0, row=0)

    txt = Entry(window,width=10)

    txt.grid(column=1, row=0)
    def clicked():
        phone_number = str(txt.get())
        send_sms(drowsydetect.main(),phone_number)
    btn = Button(window, text="Start Monitoring", command=clicked)

    btn.grid(column=3, row=1)

    window.mainloop()

def send_sms(gender,phone_number):

    p = subprocess.Popen(["powershell.exe", 
              "C:\\Users\\Win10\\Desktop\\year4\\deeplearn\\Project\\SMS.ps1",phone_number], 
              stdout=sys.stdout)

if __name__=="__main__":
    main()