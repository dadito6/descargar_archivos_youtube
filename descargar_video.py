import pytube
def video(url):
        Youtube= pytube.YouTube(url)
        video=Youtube.streams.first()
        video.download(r'C:\Users\cesar\Desktop\descargar_python\videos')
def audio(url):
    Youtube=pytube.YouTube(url)
    audio=Youtube.streams.get_audio_only()
    audio.download(r'C:\Users\cesar\Desktop\descargar_python\videos')
    
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
try:
    url= input('Ingrese la url del video :')
except:
    print('Se ingreso una url invalida')    


while not salir:
 
    print ("1. Descargar Video")
    print ("2. Descargar Audio")
    print ("3. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        video(url)
    elif opcion == 2:
        audio(url)
    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
