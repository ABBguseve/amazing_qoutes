from gtts import gTTS
import tensorflow as tf
import gpt_2_simple as gpt2 
import tarfile
from datetime import datetime #Importerar alla nödvändiga extentions

filepath = "quoteGeneration/checkpoint_amazingquotes.tar"

with tarfile.open(filepath, 'r') as tar: #Öppnar och packar upp .tar filen med den tränade vikten
    tar.extractall()

sess = gpt2.start_tf_sess() 
gpt2.load_gpt2(sess, run_name='runtwitter') #Nödvändiga gtp2 funktioner för att vikten ska kunna generera quotes

def createQuote(): #Funktion som genererar quotes och returnar dem i en lista
    text= gpt2.generate(sess, #gtp2 funktion som genererar quoten
            run_name='runtwitter',
            length= 20,
            temperature=0.7,
            prefix=',"',
            nsamples=1,
            batch_size=1,
            return_as_list=True
            )          
    Quote= text[0] #Vi vill bara ha första itemet i listan för att där ligger hela quoten
    return Quote

def postQuote(): #Funktion som tar den genererade quoten och skriver in det i ett text dokument
    text = createQuote() #Kör funkitonen för att generera quote
    doc = open("website/dailyquote.txt","w+") #Öppnar textfilen för att sedan kunna skriva in quoten
    doc.write(text) #Skriver in quoten i text dokumentet
    print(text)

print("Quote: ")
postQuote() #Kör funktion för att posta och generera quote
print("*******************************")

now = datetime.now() #Använder pythons inbyggda timefunktion för att ta reda på vad klockan är
current_time = int(now.strftime("%M")) #Sätter en variabel för antal minuter som har gått denna timme (%M står för minuter ändra det för att få andra enheter på tiden t.ex %H eller %D)
checkTime = current_time #Gör en till variabel med samma värde för att sedan kolla ett intervall

while True: #En loop som gör att koden körs hela tiden och då updaterar Dagliga Quoten
    now = datetime.now() 
    current_time = int(now.strftime("%M")) #Tar reda på tiden igen
    if current_time == checkTime+1: #Kollar om tiden nu är en minut mer än vad den var förra gången
        checkTime = current_time #Sätter den förra tiden till nuvarande tid för att kunna kolla intervallet igen
        print("Quote: ")
        postQuote() #Kör funktion för att posta och generera quote
        print("*******************************")
