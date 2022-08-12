from urllib import request, error
#import urllib
import json,csv
from os import path,startfile
from pprint import pprint



def get_data(url, using_std_lib=True):

    ''' Retriveing data from the server '''

    try:
        if using_std_lib : response = request.urlopen(url)
        else             : response = requests.get(url)

    except Exception: #error.URLError:
        print("Error : Couldn't reach the URL")
        return None
    else:
        is_received = response.status == 200
        
        if is_received:
            print('Success: ' + str(response.status))
            if using_std_lib : data = response.read().decode()
            else             : data = response.content.decode() 
            json_data = json.loads(data)
        else:
            print("Error :" + str(response.status) + ": Couldn't find the data")
    return json_data




def get_top_characters(json_data, max_characters=10):
    '''

       Extracting requreed data into a json object.

       json_data -> The json file containing the data from server.
       
       max_characters -> Number of characters for which the data should be filtered.
                         By default, extracts data for 10 characters if no value is passed.

    '''
    
    try:
        int(max_characters)
    except Exception:
        print("Error : Max characters should be entered as a integet number")
        return None

    try:
        characters = json_data['results']
    except:
        print('"Error : Required fields not found.')
        return None
    else:
        characters.sort(key=lambda x: len(x['films']),reverse=True)

        selected_characters = characters[:max_characters]

        selected_characters.sort(key=lambda x: int(x['height']),reverse=True)

        species_type = []

        for character in selected_characters:
            link = character['species']
            
            if link:
                link = link[0]
                sp_type = json.loads(request.urlopen(link).read().decode())
                species_type.append(sp_type['name'])
            else:
                species_type.append('')

        appearances = [len(x['films']) for x in selected_characters]

        for ind,character in enumerate(selected_characters):
            character['species_name'] = species_type[ind]
            character['appearances'] = appearances[ind]
    return selected_characters

    


def write_data(selected_characters, filename = 'Exported.csv'):
    '''
        Storing the extracted data in a csv file.

        If the file name is passed, it's named as Exported.csv

        The file is saved in the same folder as the script.
    '''
    
    with open(filename,'w',newline="") as export:
        csv_writer = csv.writer(export)
        for row in selected_characters:
            line = [row['name'],row['species_name'],row['height'],row['appearances']]
            csv_writer.writerow(line)
    print('Success : File Saved!')
    #startfile(exported_file)


def post_data(url, filename=''):
    '''

    Uploading the files to the server.

    url      -> server URL.
    filename -> Name of the file to be uploaded.

    '''
    files = {}
    files['file'] = files
    
    if not filename: return
    post_data = {
        'title': '10 Characters that appeared in most Star Wars movie',
        'files': filename
    }
    
    try:
        
        json_string = json.dumps(post_data)
        post_data = json_string.encode("utf-8")
        headers = {"Content-Type":"applicatoin/json"}

        the_request = request.Request( url, data=post_data, headers=headers)
        response = request.urlopen(the_request)      
    except Exception as e:
        print("Error: Couldn't reach URL")
        print(e)
        return None
    else:
        is_uploaded = response.status == 200
        if is_uploaded : print("Success : File(s) uploaded successfully!")
        else           : print("Error :" + str(response.status) + ": Couldn't upload file(s)!")
        print(response.read().decode('utf-8'))
        print(response.status)
    return


    
def show_data(selected_characters,max_characters=3):
    ''' Show json data for exported data. '''
    
    for num,character in enumerate(selected_characters):
        if num >= max_characters:break
        print('-'*50,end='\n')
        print('Character ' + str(num) + ': ' + character['name'].center(48))
        print('-'*50,end='\n')
        pprint(character)
        print('-'*50,end='\n')
    return



if __name__ == '__main__':

    url = r'https://swapi.dev/api/people/'
    server = r'http://httpbin.org/anything'

    using_std_lib = True
    json_data = get_data(url, using_std_lib)
    if json_data:
        selected_characters = get_top_characters(json_data,5)
        if selected_characters:
            #show_data(selected_characters)
            write_data(selected_characters)
            post_data(server,selected_characters)
