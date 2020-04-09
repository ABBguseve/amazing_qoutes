# Amazing Qoutes

Amazing Qoutes är en websida som visar upp AI genererade qoutes. Qoutesen är genererade av en tränad vikt och läggs sedan upp på hemsidan. Nya qoutes genereras i intervall och byts ut mot den gamla quoten.

## Starta

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
### Köra koden
Se till att du har navigerat till rätt folder innan du startar koden. Du ska vara i "amazing_qoutes".

* Starta först upp hemisdan på localhost i din webläsare. Du borde se att det står "Start the python script to generate the first quote". Testa att updatera sidan om ingen text kommer upp.
* Starta sedan python scriptet (Viktigt att du har navigerat till rätt folder).

Det kommer att ta någon minut för scriptet att generera första qouten då "tar" filen måsta packas upp. Qouten borde skrivas ut i terminalen och ska då också finnas på hemsidan. 

Koden är satt på ett intervall på en minut och kommer att fortsätta generera qoutes i det intevallet tills scriptet avbryts. 
