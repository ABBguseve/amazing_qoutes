# Amazing Qoutes

Amazing Qoutes är en websida som visar upp AI genererade qoutes. Qoutesen är genererade av en tränad vikt och läggs sedan upp på hemsidan. Nya qoutes genereras i intervall och byts ut mot den gamla quoten.

## Installation

För att Kunna köra python scriptet som genererar qoutes är det vissa saker som behövs installeras. Detta görs genom att skriva in detta i terminalen:
```
pip install gtts
pip install gpt_2_simple
pip install tarfile
```
Tensorflow behöver vara i version 1.13.1 för att scriptet ska fungera detta gör du genom att skriva detta i terminalen
```
pip install tensorflow==1.13.1
```
## Köra koden

Se till att du har navigerat till rätt folder innan du startar koden. Du ska vara i "amazing_qoutes".

* Starta först upp hemisdan på localhost i din webläsare. Du borde se att det står "Start the python script to generate the first quote". Testa att updatera sidan om ingen text kommer upp.
* Starta sedan python scriptet (Viktigt att du har navigerat till rätt folder).

Det kommer att ta någon minut för scriptet att generera första qouten då "tar" filen måsta packas upp. Qouten borde skrivas ut i terminalen och ska då också finnas på hemsidan. 

Koden är satt på ett intervall på en minut och kommer att fortsätta generera qoutes i det intevallet tills scriptet avbryts. 

# Mitt Arbete

Här beskirver jag hur jag har arbetat, vilka problem som har uppkommit, hur jag löste de samt vad jag skulle gjord annorlunda om jag fick göra om projektet och förbättringsmöjligheter.

## Problem och Lösningar

* Jag hade till en början problem med att ladda ner den tränade vikten från google colab. Jag frågade några klasskamrater om hjälp och lyckade sedan ladda upp filen på min google driva för att sedan ladda ner dem till min dator.
* Jag hade också problem att få tensorflow att fungera. Jag fick höra att det berodde på att versionen jag hade var för ny och jag fick då gå egenom några gammla versioner för att hitta den som funngerade. 
* Jag visste inte heller hur jag skulle kunna läsa av texten i en textfil med javascript. Jag hittade sedan en lösning online från någon som hade haft ett liknande problem. 
* Ett annat problem jag hade var att jag inte kunde få python scriptet att skriva ut text documentet på rätt ställe. Det var en enkel lösning på det här problemet vilket var att jag behövde navigera till en annan folder för att scriptyet skulle kunna köras rätt.

## Förändringar jag skulle vilja göra

