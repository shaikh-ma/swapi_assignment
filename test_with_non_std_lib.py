import json
import requests
import pandas as pd
import assignment_with_non_std_libraries as script

def run_test():
    url    = r'https://swapi.dev/api/people/'
    server = r'http://httpbin.org/anything'

    fail = False
    try:
        results = script.get_data(url)
        if results is not None:
            selected_characters = script.get_top_characters(results)
            if selected_characters is not None:
               script.show_data(selected_characters)
               filename = script.write_data(selected_characters)
               script.post_data(server,filename)
            else: fail = True
        else: fail = True
    except:
         print('Test Failed')
         return 'Failed'
    if fail:
        print('Test Failed')
        return 'Failed'
    print('Test Passed')
    return 'Passed'   

run_test()
