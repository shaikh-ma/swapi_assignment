using_std_libraries = False

try:
    import requests
    import pandas as pd
    import assignment_with_non_std_libraries
except ModuleNotFoundError:
    print('Using standard modules')
    using_std_libraries = True
    from assignment_with_std_libraries import *


if using_std_libraries:
    url = r'https://swapi.dev/api/people/'
    
    json_data = get_data(url)
    if json_data:
        selected_characters = get_top_characters(json_data)
        show_data(selected_characters)
        #write_data(selected_characters)
        #post_data(selected_characters)
    input()
