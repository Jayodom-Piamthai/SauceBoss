import webbrowser as wb 
import os
#Trackin' down your soul just to make you mine,mixin' all the lights flashing in my eyes. i believe in the sounds pumpin in my mind,as we bounce into the music. BOUNCE INTO THE MUSIC

chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
chromePath2 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito' #failsafe

print("//INITIALIZING SauceBoss//")
print("MADE BY:Ace J.P.,no copyright whatsoever")
print("-----Nhentai-----")
print("open a sauce input:[sauce] ")
print("open a home page input:home")
print("search tab input:search [search keyword]")
print("--SauceArchive--")
print("open sauce history input:0000")
print("delete history input:DELETE")
i=0
while i == 0 : #Rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind,rewind
    def sauceBoss(): # This is where the fun begins....
        CODE = input("Please enter the code:") #Enter the Nuclear code
        NumberChecker = (CODE.isnumeric()) #only number,sucker
        if CODE == ("DELETE") : #library's end
            D = open("SauceArchive.txt", "w")
            D.write("")
            D.close()
            print("History successfully wiped")
            sauceBoss()
        elif 'search' in CODE : #turn the key,flip the switch
            SearchKeyword = (CODE.split(' ',1)[1])
            theKey = f'https://nhentai.net/search/?q={SearchKeyword}'
            wb.get(chromePath).open(theKey)
            wb.get(chromePath2).open(theKey) #failsafe
        elif CODE == ("home") : #α
            wb.get(chromePath).open('https://nhentai.net')
            wb.get(chromePath2).open('https://nhentai.net') #failsafe
            sauceBoss()
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
            wb.get(chromePath).open(NuclearCode)
            wb.get(chromePath2).open(NuclearCode) #failsafe
            f = open("SauceArchive.txt", "a")
            f.write(CODE)
            f.write(" , ")
            f.close()
            sauceBoss()      
    sauceBoss() #RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,RUN IT!,.........

