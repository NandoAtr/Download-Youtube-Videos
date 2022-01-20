from pytube import YouTube

def Geral():
    global Video

    try:
        url=input("URL Video:")
        Video=YouTube(url)
        
        
    except:
        def erro1():
            global Video
            while True:
                try:
                    print("Invalid URL, Type again.")
                    url=input("URL Video:")
                    Video=YouTube(url)
                    break
                
                except:
                    erro1()
            
    erro1()
            
    print("URL Recebida")

    
    def Confirm():
        global SN
        while True:
            print("Confirm Video Title:\n\n"+Video.title)
            SN=input("Your Video Title is that, Yes or No:")

            List=('Yes','Y')
            list2=[X.upper() for X in List]

            if SN in list2:
                break

            else:
                Confirm()

    

    print("Download Video")
    
    download1= Video.streams.get_highest_resolution()

    download1.download()



Geral()




