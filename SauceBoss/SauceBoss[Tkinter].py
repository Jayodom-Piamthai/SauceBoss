from tkinter import *
from PIL import ImageTk,Image
import webbrowser as wb

from matplotlib.colors import rgb2hex

#how much can we push this stupid idea,Ace. how much can i waste my time doing this

chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
chromePath2 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito' #failsafe

root=Tk()
root.title("SauceBoss")
root.iconbitmap("projectAndShits(transparent).ico")

frame=LabelFrame(root,padx=30,pady=60)
frame.configure(bg="gray13")
SauceBoss=Label(frame,text=("- SauceBoss -"),font=("Helvetica",40,"bold"),bg="gray13",fg="white")
#logo
logo=Image.open("Logo.png")
logoRE=logo.resize((200,200),Image.ANTIALIAS)
ResizedLogo=ImageTk.PhotoImage(logoRE)
headLogo= Label(frame,image = ResizedLogo,bg="gray13")
searchBar=Entry(frame,width=50,bg="black",fg="white")
#button
search=Button(frame,text="Search",font=("Helvetica",10,"bold"),bg="black",fg="Red",command=lambda:clicked(modeus.get()))
#type
mode=[
    ("Sauce",1,4,5),("Name Search",2,4,22),("tag",3,4,45)
]
modeus=IntVar()
modeus.set("sauce")
for type,mv,rowPos,columnPos in mode:
    Radiobutton(frame,text=type,variable=modeus,value=mv,bg="gray13",fg="violetRed3").grid(row=rowPos,column=columnPos,columnspan=columnPos+5)
def clicked(value):
    if value == 1 :
        NuclearCode = f'https://nhentai.net/g/{searchBar.get()}/'  
        wb.get(chromePath).open(NuclearCode)
        wb.get(chromePath2).open(NuclearCode) #failsafe
    if value == 2 :
        theKey = f'https://nhentai.net/search/?q={searchBar.get()}'
        wb.get(chromePath).open(theKey)
        wb.get(chromePath2).open(theKey)
    if value == 3 :
        theTag = f"https://nhentai.net/tag/{searchBar()}"
        wb.get(chromePath).open(theTag)
        wb.get(chromePath2).open(theTag)

#placement
frame.grid(padx=5,pady=5,columnspan=69)
SauceBoss.grid(row=0,columnspan=69)
headLogo.grid(row=1,columnspan=69)
searchBar.grid(row=2,columnspan=69)
search.grid(row=3,columnspan=69)

mainloop()