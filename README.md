# Amazing Quotes

Amazing Quotes är en websida som visar upp AI genererade quotes. Quotesen är genererade av en tränad vikt och läggs sedan upp på hemsidan. Nya quotes genereras i intervall och byts ut mot den gamla quoten. Sidan är tänkt att updateras dagligen men intervallet är nu kortare för att kunna demostreras bättre. 

## Installation

För att Kunna köra python scriptet som genererar quotes är det vissa saker som behövs installeras. Detta görs genom att skriva in detta i terminalen:
```
pip install gtts

pip install gpt_2_simple

pip install tarfile
```
Tensorflow behöver vara i version 1.13.1 för att scriptet ska fungera detta gör du genom att skriva detta i terminalen
```
pip install tensorflow==1.13.1
```
### Live Server

Jag kör själv med en extention i visual studio sam heter **Live Server**. Den gör det egentligen lättare att göra hemsidan men det funkar även bättre att köra programmet med Live Server. 

**Instalation Live server**

För att instalera, gå till extention i visual studio och sök efter live server. Ladda ner den första som kommer up. Efter det så högerklickar du på [html](https://github.com/ABBguseve/amazing_qoutes/blob/master/website/index.html) filen och klickar på **Open with Live Server**. Hemsidan kommer då öppnas i din standard webläsare och koden kan då fungera bättre. 
## Köra koden

Se till att du har navigerat till rätt folder innan du startar koden. Du ska vara i "amazing_quotes".

* Börja med att köra [**downloader.py**](https://github.com/ABBguseve/amazing_qoutes/blob/master/qouteGeneration/downloader.py). Det tar ett tag för programmet att ladda ner filen från google drive.
* Starta sedan upp hemisdan på localhost i din webläsare. Du borde se att det står "Start the python script to generate the first quote". Testa att updatera sidan om ingen text kommer upp.
* Starta sedan [**QuoteGenerator.py**](https://github.com/ABBguseve/amazing_qoutes/blob/master/qouteGeneration/QouteGenarator.py) (Viktigt att du har navigerat till rätt folder).

Det kommer att ta någon minut för scriptet att generera första quoten då "tar" filen måsta packas upp. Quoten borde skrivas ut i terminalen och ska då också finnas på hemsidan. 

Koden är satt på ett intervall på en minut och kommer att fortsätta generera quotes i det intevallet tills scriptet avbryts. 

# Mitt Arbete

Här beskirver jag hur jag har arbetat, vilka problem som har uppkommit, hur jag löste de samt vad jag skulle gjord annorlunda om jag fick göra om projektet och förbättringsmöjligheter.

## Problem och Lösningar

* Jag hade till en början problem med att ladda ner den tränade vikten från google colab. Jag frågade några klasskamrater om hjälp och lyckade sedan ladda upp filen på min google driva för att sedan ladda ner dem till min dator.
* Jag hade också problem att få tensorflow att fungera. Jag fick höra att det berodde på att versionen jag hade var för ny och jag fick då gå egenom några gammla versioner för att hitta den som funngerade. 
* Jag visste inte heller hur jag skulle kunna läsa av texten i en textfil med javascript. Jag hittade sedan en lösning online från någon som hade haft ett liknande problem. 
* Ett annat problem jag hade var att jag inte kunde få python scriptet att skriva ut text documentet på rätt ställe. Det var en enkel lösning på det här problemet vilket var att jag behövde navigera till en annan folder för att scriptyet skulle kunna köras rätt.

## Förändringar jag skulle vilja göra

En sak som jag skulle vilja lägga till och även hade tänkt ha med i början är att det finns en till sektion på hemsidan där det finns en knapp som man kan klicka på för att direkt generera en egen quote. Jag tog inte med detta eftersom att jag fick problem med att starta python scriptet från hemsidan och kände att jag inte ville lägga för mycket tid på det, jag ville istället fokusera på huvudelen av projektet. 
