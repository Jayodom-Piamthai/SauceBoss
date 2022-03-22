from tkinter import *
from PIL import ImageTk,Image
import webbrowser as wb

#how much can we push this stupid idea,Ace. how much can i waste my time doing this

chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
chromePath2 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito' #failsafe

root=Tk()
root.title("SauceBoss")
root.iconbitmap("projectAndShits(transparent).ico")

frame=LabelFrame(root,padx=30,pady=60)
SauceBoss=Label(frame,text=("- SauceBoss -"),font=("Helvetica",40,"bold"))
#logo
logo=Image.open("Logo.png")
logoRE=logo.resize((200,200),Image.ANTIALIAS)
ResizedLogo=ImageTk.PhotoImage(logoRE)
headLogo= Label(frame,image = ResizedLogo)
searchBar=Entry(frame,width=50,bg="black",fg="white")
#button
search=Button(frame,text="Search",bg="black",fg="magenta",command=lambda:clicked(modeus.get()))
#type
mode=[
    ("sauce",1,4,1),("tag",2,4,2)
]
modeus=IntVar()
modeus.set("sauce")
for type,mv,rowPos,columnPos in mode:
    Radiobutton(frame,text=type,variable=modeus,value=mv).grid(row=rowPos,column=columnPos)
def clicked(value):
    if value == 1 :
        theKey = f'https://nhentai.net/search/?q={searchBar.get()}'
        wb.get(chromePath).open(theKey)



#placement
frame.grid(padx=5,pady=5)
SauceBoss.grid(row=0,columnspan=69)
headLogo.grid(row=1,columnspan=69)
searchBar.grid(row=2,columnspan=69)
search.grid(row=3,columnspan=69)

mainloop()