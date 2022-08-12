import json
import requests
import pandas as pd

root_url = r'https://swapi.dev/api/people/'


def get_data(url):
    try:
        response = requests.get(url)
        data = response.content.decode()
    except Exception as e:
        print("Could'nt reach the server")
        return None
    else:
        json_data = json.loads(data)
    return json_data


def get_top_ten_characters(json_data, max_characters=10):
    characters = json_data['results']
    characters.sort(key=lambda x:len(x['films']), reverse=True)
    
    df = pd.DataFrame(characters)
    df['height'] = pd.to_numeric(df['height'])
    df = df.sort_values(by=["height"],ascending=False) 

    species_type = []
    for x in df['species']:
        if x:
            x = list(x)[0] 
            print(x)
            sp_data = json.loads(requests.get(x).content.decode())#['name'])
            species_type.append(sp_data['name'])
        else:
            species_type.append('')

    appearances = [len(x) for x in df['films']]

    df['appearances'] = appearances
    df['species'] = species_type
    return df

def show_data(selected_characters,max_characters=10):
    print(selected_characters.head(max_caracters)    
    return


def write_data(selected_characters,filename='Exported.csv'):
    export_columns = ['name','species','height','appearances']
    selected_characters.to_csv(filename, index=False, header=False, columns=export_columns, sep=',', encoding='utf-8')
    os.startfile(filename)
    return 

def post_data(url, filename=''):
    '''

    Uploading the files to the server.

    url      -> server URL.
    filename -> Name of the file to be uploaded.

    '''
    
    files = {}
    files['file'] = filename

    if not filename: return

    try:
        response = requests.post(url,files)
    except:
        print("Couldn't reach URL")
        return None
    else:
        is_uploaded = response.status == 200
        if is_uploaded : print("Success : File(s) uploaded successfully!")
        else           : print("Error :" + str(response.status) + ": Couldn't upload file(s)!")
    return

results = get_data(root_url)
selected_characters  = get_top_ten_characters(results)
write_data(selected_characters)
