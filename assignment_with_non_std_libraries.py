import json
import requests
import pandas as pd


def get_data(url):
    ''' 
    Retriveing data from the server.

    Parameters
    ----------
    URL : URL of the server from which to get the data.
    
    Returns
    --------
    The data if received, otherwise None.
    '''

    try:
        response = requests.get(url)
    except Exception as e:
        print("Error : Couldn't reach the URL", end='\n')
        print(e, end="\n")
        return None
    else:
        if response.ok:
            print('Success: Data retrieved successfully! - Status code: ' +
            str(response.status_code), end='\n')
            data = response.text
            json_data = json.loads(data)
        else:
            print("Error :" + str(response.status_code) + " -  Couldn't find the data", end='\n')
    return json_data


def get_top_characters(json_data, max_characters=10):
    '''
    Extracting requreed data into a json object.

    Parameters
    ----------
    json_data :
    The json file containing the data from server.
       
    max_characters :
    Number of characters for which the data should be filtered.
    By default, extracts data for 10 characters if no value is passed.

    Returns
    -------
    JSON format for the number of characters appearing in most films.
    '''
    characters = json_data['results']
    characters.sort(key=lambda x:len(x['films']), reverse=True)
    
    df = pd.DataFrame(characters)
    df['height'] = pd.to_numeric(df['height'])
    df = df.sort_values(by=["height"], ascending=False) 

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

def show_data(selected_characters, max_characters=None):
    '''
    Show json data for exported data.
    '''
    if not max_characters:
        max_characters = int(selected_characters.shape[0])

    print(selected_characters.head(max_characters))
    return None


def write_data(selected_characters, filename='Exported.csv'):
    '''
    Storing the extracted data in a csv file.
    If the file name is passed, it's named as "Exported.csv".
    The file is saved in the same folder as the script.

    Returns
    -------
    The filename.
    '''
    export_columns = ['name', 'species', 'height', 'appearances']
    selected_characters.to_csv(
        filename,
        index=False,
        header=False,
        columns=export_columns,
        sep=',',
        encoding='utf-8'
        )
    return filename

def post_data(url, filename=''):
    '''
    Uploading the files to the server.

    Parameters
    ----------
    url      : server URL
    filename : Name of the file to be uploaded

    Returns
    -------
    The tuple containing response object from the request and the status code.
    '''
   
    files = {}

    if not filename:
        return None

    files = {'file': open(filename, 'rb')}

    try:
        response = requests.post(url, files)
    except:
        print("Couldn't reach URL")
        return None
    else:
        if response.status_code == 200  :
            print("Success : File(s) uploaded successfully!")
        else:
            print(
                "Error :" 
                + str(response.status_code)
                + ": Couldn't upload file(s)!"
                )
        print(response.text)
        print(response.status_code)
    return response.text, response.status_code


if __name__ == '__main__':
    url    = r'https://swapi.dev/api/people/'
    server = r'http://httpbin.org/anything'

    results = get_data(url)
    if results:
        selected_characters = get_top_characters(results)
        if selected_characters is not None:
           show_data(selected_characters)
           write_data(selected_characters)
           post_data(server, 'Exported.csv')