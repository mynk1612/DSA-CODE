from tkinter import *
import backend

def search_command():
    try:
         word = word_data.get()
         output = backend.translate(word)
         t1.delete('1.0',END)
         if type(output) == list:
             t1.insert(END,backend.warning)
             for x in output:
                  t1.insert(END,'\n' + str(x) + '\n')
         elif word == '':
              t1.delete('1.0',END)
         else:
             t1.insert(END,output)
         
    except:
        pass
    
def about_command():
    newWindow = Toplevel()
    newWindow.resizable(0,0)
    newWindow.title("About")
    newWindow.geometry("300x100")
    nl1 = Label(newWindow,text = "Developer:Mayank Kandpal\n Abhishek Rawat\n Sourav Mehra\nProgram Developed in Python\nWhatsapp: +917300959719\nEmail:help.dicgui12@gmail.com")
    nl1.pack()
    


window = Tk()
window.title("Word-Defination")
window.geometry('680x600')
window.resizable(0,0)

l1 = Label(window, text = "Enter Word",  font = ("Arial",16,"bold"))
l1.grid( row = 0 , column = 0 , columnspan = 2)

word_data = StringVar()
e1 = Entry(window, textvariable = word_data , width = 40, bd = 5, font = ('Arial',14,'bold'))
e1.grid(row = 0 , column = 2)

b1 = Button(window,text = 'Search' , width = 12 , command = search_command,font = ("Arial",12,"bold"))
b1.grid(row = 1 , column = 2 )

b2 = Button(window,text = "About" ,command = about_command,font = ("Arial",9,"bold"))
b2.grid(row = 0 , column = 4 , columnspan = 2 )

t1 = Text(window, height = 27.5 , width = 75)
t1.configure(font = ("Arial",12,"bold"))
t1.grid(row = 2 , column = 0 , columnspan = 5 )


window.mainloop()