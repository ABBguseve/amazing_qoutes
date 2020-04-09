import requests

def download_file_from_google_drive(id, destination): # Funktion som laddar ner "tar" filen från google drive
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token: # Kollar så att allt stämmer med url:en
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response): # Funktion som kollar så att alla tecken stämmer
    for key, value in response.cookies.items():
        if key.startswith('download_warning'): # returnar sedan värdet om det startar på "download_warning"
            return value

    return None

def save_response_content(response, destination): # Funktion som sparar filen på datorn
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: #  Filtrerar ut vissa chunks
                f.write(chunk)

if __name__ == "__main__": # Kör själva scriptet om påståendet stämmer
    file_id = '1vT6hWRSxHfBJi7Fad0RpFBXav0rBpmI_' # Mitt file-ID på "tar" filen i min Drive
    destination = 'qouteGeneration/checkpoint_amazingquotes.tar' # Fildestination där jag vill spara filen
    download_file_from_google_drive(file_id, destination) # Kör nedladdningsfunktionen. 