
__version__ = '0.1'
__author__ = 'Auditoría Continua'


import os
import speech_recognition as sr  #Libreria clave
from gtts import gTTS
from playsound import playsound  #$ pip install playsound

#sudo pip install SpeechRecognition y sudo pip install pyaudio (microfono)



def sentimiento(txt):
    import google.cloud.language
    # Create a Language client.
    language_client = google.cloud.language.LanguageServiceClient()

    # TODO (Developer): Replace this with the text you want to analyze.
    text = txt
    document = google.cloud.language.types.Document(
        content=text,
        type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

    # Use Language to detect the sentiment of the text.
    response = language_client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment

    return (u'Text: {}'.format(text))
    return (u'Sentiment: Score: {}, Magnitude: {}'.format(sentiment.score, sentiment.magnitude))


def sttstr(): 

# Record Audio
    r = sr.Recognizer() #obtiene audio desde el microfono
    with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source) #ajuntar el ruido del ambiente
         #print("DIGA LO QUÉ DESEA BUSCAR! \n")
         audio = r.listen(source)
         
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio, language='es-DO')
    except sr.UnknownValueError:
        tts_busqueda("No te pude entender saliendo")
        #print ('AHORA...')
        #sttstr()
        exit()
    except sr.RequestError as e:
        return ("Tiempo de servicio agotado, debe pagar; {0}".format(e))
        exit()





def rutageneral():
    rg = os.getcwd() + '\\FOLDER_PDF\\'
    return rg

def abrir_archivo_resultado(nombre_archivo):
  
    try:
        os.system(rutageneral() + nombre_archivo)
    except Exception as err:
           print ("Error -->: {0}".format(err))
           

def elimina_archivo(nombre_archivo):
    
    if os.path.exists(rutageneral() + nombre_archivo):
       try:
            os.remove(rutageneral() + nombre_archivo)
       except OSError as err:
           print("aqui")
           print ("Error -->: {0}".format(err))


def decir_buscar():
    #unica función es dicir texto a buscar...
    playsound(rutageneral() + "buscar.mp3")
 
       
    

def tts_busqueda(strtext):
    try: 
         tts = gTTS(strtext, lang='es')
         tts.save(rutageneral() + strtext + ".mp3")
         playsound(rutageneral() + strtext + ".mp3")
         elimina_archivo(rutageneral() + strtext + ".mp3")
    except Exception as err:
           print ("Error -->: {0}".format(err))
           tts = gTTS("Ocurrio Error", lang='es')
           tts.save(rutageneral() + 'Ocurrio Error' + ".mp3")
           playsound(rutageneral() + 'Ocurrio Error' + ".mp3")

