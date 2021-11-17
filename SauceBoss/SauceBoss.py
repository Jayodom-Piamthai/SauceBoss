import webbrowser as wb 
import os
#Trackin' down your soul just to make you mine,mixin' all the lights flashing in my eyes. i believe in the sounds pumpin in my mind,as we bounce into the music. BOUNCE INTO THE MUSIC

print("//INITIALIZING SauceBoss//")
print("MADE BY:Ace J.P.,no copyright whatsoever")
print("for sauce opening in incognito please input the code below")
print("for sauce history please input code:0000")
print("for COMPLETE HISTORY WIPE please input :DELETE")
def sauceBoss(): # This is where the fun begins....
    CODE = input("Please enter the code:") #Enter the Nuclear code
    NumberChecker = (CODE.isnumeric()) #only number,sucker
    if CODE == ("DELETE") : #library's end
        D = open("SauceArchive.txt", "w")
        D.write("")
        D.close()
        print("History successfully wiped")
        sauceBoss()
    elif CODE == ("home") :
        wb.get(chromePath).open('https://nhentai.net')
        wb.get(chromePath2).open('https://nhentai.net') #failsafe
    elif NumberChecker == False: #ONLY NUMBER
        print("ERROR")
        sauceBoss()
    elif CODE == ("0000") : #library's Gate
        print("activate archive")
        a = open("SauceArchive.txt", "r")
        print(a.read())
        sauceBoss()
    else: #Nuclear's Launch
        NuclearCode = f'https://nhentai.net/g/{CODE}/'  
        chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
        chromePath2 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito' #failsafe
        wb.get(chromePath).open(NuclearCode)
        wb.get(chromePath2).open(NuclearCode) #failsafe
        f = open("SauceArchive.txt", "a")
        f.write(CODE)
        f.write(" , ")
        f.close()
        sauceBoss()      
sauceBoss() #RUN IT!
