from pytube import YouTube, Stream
import os

os.system("cls")
#pip install pytube pra funcionar certinho
while True:
    
    print("""
    
██╗░░░██╗██████╗░███████╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗
╚██╗░██╔╝██╔══██╗██╔════╝██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
░╚████╔╝░██████╔╝█████╗░░█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██████╦╝█████╗░░
░░╚██╔╝░░██╔═══╝░██╔══╝░░██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
░░░██║░░░██║░░░░░███████╗██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝░░░██║░░░╚██████╔╝██████╦╝███████╗
░░░╚═╝░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝

██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
    
    
    
    """)
    url = input("Digite a url do video ou (S) para sair: ")
    if url == "S" or url == "s":
        break
    yt = YouTube(url)
    MaxQuality = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    formatoVideo = MaxQuality.mime_type
    if formatoVideo == 'video/mp4':
        print("Formato de video: mp4")
        print("Qualidade:", MaxQuality.resolution)
        print("Tamanho:", MaxQuality.filesize)
        print("Baixando...")
        MaxQuality.download()
        print("Download concluido!")
        break
    else:
        print("Formato de video nao suportado!")



  