import json
import requests
import pandas as pd


def get_data(url):
    try:
        response = requests.get(url)
        data = response.content.decode()
    except Exception as e:
        print("Error : Could'nt reach the server")
        print(e)
        return None
    else:
        json_data = json.loads(data)
    return json_data


def get_top_characters(json_data, max_characters=10):
    characters = json_data['results']
    characters.sort(key=lambda x:len(x['films']), reverse=True)
    
    df = pd.DataFrame(characters)
    df['height'] = pd.to_numeric(df['height'])
    df = df.sort_values(by=["height"],ascending=False) 

    species_type = []
    for x in df['species']:
        if x:
            x = list(x)[0] 
            sp_data = json.loads(requests.get(x).content.decode())
            species_type.append(sp_data['name'])
        else:
            species_type.append('')

    appearances = [len(x) for x in df['films']]

    df['appearances'] = appearances
    df['species'] = species_type
    return df

def show_data(selected_characters,max_characters=None):
    if not max_characters: max_characters = int(selected_characters.shape[0])
    print(selected_characters.head(max_characters))
    return


def write_data(selected_characters,filename='Exported.csv'):
    export_columns = ['name','species','height','appearances']
    selected_characters.to_csv(filename, index=False, header=False, columns=export_columns, sep=',', encoding='utf-8')
    return filename

def post_data(url, filename=''):
    '''
    Uploading the files to the server.

    url      -> server URL.
    filename -> Name of the file to be uploaded.

    '''
    
    files = {}

    if not filename: return
    files = {'file': open(filename ,'rb')}

    try:
        response = requests.post(url,files)
        upload_status = response.status_code
    except Exception as e:
        print("Couldn't reach URL")
        print(e)
        return None
    else:
        if upload_status == 200  :
            print("Success : File(s) uploaded successfully! - status : " + str(upload_status))
            print(str(response.text))
        else:
             print("Error : Couldn't upload file(s)! - status : " + str(upload_status))
    return response.text,upload_status


if __name__ == '__main__':
    url    = r'https://swapi.dev/api/people/'
    server = r'http://httpbin.org/anything'

    results = get_data(url)
    if results:
        selected_characters  = get_top_characters(results)
        if selected_characters is not None:
           show_data(selected_characters)
           write_data(selected_characters)
           post_data(server,'Exported.csv')
